/* Local, dependency-light reader. All source-derived text is escaped before rendering. */
(() => {
  'use strict';
  const data=window.TCS_ATLAS;
  if(!data){document.getElementById('cards').textContent='The catalogue data could not be loaded.';return;}
  const $=id=>document.getElementById(id);
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const norm=s=>window.ATLAS_MATH.plain(String(s??'')).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const safeURL=s=>{try{const u=new URL(s);return ['https:','http:'].includes(u.protocol)?u.href:'#';}catch{return '#';}};
  const num=n=>n.toLocaleString('en-US');
  const statuses={open:'Documented as open',source_open:'Open in the dated source',uncertain:'Current status unverified',resolved:'Resolved / materially changed',excluded:'Retired after review'};
  const state={areas:new Set(),matches:[],shown:0,batch:16,navigation:0};
  const cardsById=new Map(data.cards.map(c=>[c.id,c]));
  let areasByName=new Map(data.areas.map(a=>[a.area,a]));
  const areaLabel=area=>areasByName.get(area)?.label||area||'';
  const publishedArea=c=>c.selection?.area||c.area;
  const cardAreaLabel=c=>areaLabel(publishedArea(c));
  const benchmarks={top100:{label:'Top 100',quotas:{large:5,small:2}},top500:{label:'Top 500',quotas:{large:25,small:10}},top1000:{label:'Top 1000',tentative:true,quotas:{large:50,small:20}}};
  const isActive=c=>!!c&&!c.scope_exclusion&&c.status!=='excluded'&&(c.status!=='resolved'||c.benchmark_eligibility?.open_at_cutoff===true);
  let categoryRanks=new Map(),areaPositions=new Map();
  const inBenchmark=(c,name)=>isActive(c)&&c.importance_rank<=(benchmarks[name]?.quotas[areasByName.get(c.area)?.group]||0);
  const searchable=c=>norm([c.id,c.title,c.title_cs,c.area,areaLabel(c.area),c.original_area,areaLabel(c.original_area),c.scope_exclusion?.previous_area,cardAreaLabel(c),c.formal,c.source_formulation?.text,c.definitions,c.answer_criterion,c.context,c.why,...(c.working_summary?.sentences||[]),...(c.working_summary?.extra_sources||[]).map(r=>r.title),...(c.references||[]).map(r=>r.title+' '+r.authors),...(c.textbook_notes||[]).map(n=>[n.summary,n.kind,n.reference.title,n.reference.authors,n.reference.locator].join(' '))].join(' '));
  const searchIndex=new Map(data.cards.map(c=>[c.id,searchable(c)]));
  function toast(text){$('toast').textContent=text;$('toast').classList.add('visible');clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('toast').classList.remove('visible'),2300);}
  function link(r,label){return `<a href="${esc(safeURL(r.url))}" target="_blank" rel="noopener noreferrer">${esc(label||r.title)}</a>`;}
  function relatedProblems(c){
    const targets=(c.related_problem_ids||[]).map(id=>cardsById.get(id)).filter(isActive)
      .sort((a,b)=>(b.importance?.score??50)-(a.importance?.score??50)||a.id.localeCompare(b.id,'en'));
    if(!targets.length)return '';
    const item=c=>`<li><a href="#${encodeURIComponent(c.id)}" class="related-problem-link"><span class="related-problem-id">${esc(c.id)}</span> ${esc(c.title_cs||c.title)}</a></li>`;
    const extra=targets.slice(5);
    return `<section class="card-section related-problems" aria-label="Related problems"><h3>Related problems</h3><ul>${targets.slice(0,5).map(item).join('')}</ul>${extra.length?`<details class="related-more"><summary>Show ${num(extra.length)} more related problems</summary><ul>${extra.map(item).join('')}</ul></details>`:''}</section>`;
  }
  function canonicalLink(c){
    const id=c.review_outcome?.duplicate_of||c.scope_exclusion?.duplicate_of;
    return id&&cardsById.has(id)?`<a href="#${encodeURIComponent(id)}" class="canonical-card-link">${c.scope_exclusion?.duplicate_of?'Retained question':'Read full card'} · ${esc(id)} →</a>`:'';
  }
  function cite(c,id){let i=c.references.findIndex(r=>r.id===id);return i<0?'':` <a class="citation" href="${esc(safeURL(c.references[i].url))}" target="_blank" rel="noopener noreferrer" title="${esc(c.references[i].title)}">[${i+1}]</a>`;}
  const paragraphs=(text,cls='')=>window.ATLAS_DEFINITIONS.paragraphs(text,cls);
  function statementNotice(c){
    const review=c.statement_review;if(!review)return '';
    return review.status==='needs_specification'
      ?`<div class="status-line statement-review"><strong>Statement needs specification</strong>${paragraphs(review.remaining_issue)}</div>`
      :'<p class="small muted statement-review">Statement wording reviewed · current open status is recorded separately.</p>';
  }
  function workingSummary(c){
    const summary=c.working_summary;if(!summary?.sentences?.length)return '';
    const citations=(summary.source_refs||[]).map(id=>cite(c,id)).join('');
    const extra=(summary.extra_sources||[]).map(r=>link(r)).join(' · ');
    return `<section class="card-section working-summary"><h3>Working summary</h3>${paragraphs(summary.sentences.join(' '))}<div class="small muted">Sources${citations}${extra?' · '+extra:''}</div></section>`;
  }
  function textbookNotes(c){
    if(!c.textbook_notes?.length)return '';
    const kinds={question:'Question',conjecture:'Conjecture',research_direction:'Research direction'};
    return `<section class="textbook-notes"><h3>Questions recorded in textbooks and surveys</h3><p class="small muted">Dated paraphrases; definitions and assumptions are at the cited locations. A source note does not override a later review of this card.</p><ol>${c.textbook_notes.map(n=>`<li><p><strong>${esc(kinds[n.kind]||n.kind)}.</strong> ${esc(n.summary)}</p><p class="small">${esc(n.reference.authors)} · ${esc(n.reference.year)} · ${link(n.reference)} · ${esc(n.reference.locator)} · ${link({url:n.reference.pdf_url},'Original PDF ↗')}</p><p class="small muted">${esc(n.status_note)}</p>${n.caution?`<p class="small muted">Source caveat: ${esc(n.caution)}</p>`:''}</li>`).join('')}</ol></section>`;
  }
  const focusPosition=c=>c.area===publishedArea(c)?(c.benchmark_focus?.position??Infinity):Infinity;
  const importanceOrder=(a,b)=>focusPosition(a)-focusPosition(b)||(b.importance?.score??50)-(a.importance?.score??50)||a.id.localeCompare(b.id,'en');
  const catalogueOrder=(a,b)=>(areaPositions.get(publishedArea(a))??Infinity)-(areaPositions.get(publishedArea(b))??Infinity)||importanceOrder(a,b);
  function rebuildCategoryRanks(){
    areaPositions=new Map(data.areas.map((a,i)=>[a.area,i]));
    categoryRanks=new Map();const counts=new Map();
    for(const c of data.cards.filter(isActive).sort(catalogueOrder)){
      const rank=(counts.get(publishedArea(c))||0)+1;counts.set(publishedArea(c),rank);categoryRanks.set(c.id,rank);
    }
  }
  function importanceBadge(c){
    return categoryRanks.has(c.id)?`<span class="importance-badge">#${num(categoryRanks.get(c.id))} in category</span>`:'';
  }
  const selectionColor=c=>c.selection?.color||'red';
  const selectionNames={green:'Green · selected',yellow:'Yellow · reserve',red:'Red · not selected'};
  const selectionBadge=c=>`<span class="selection-badge ${selectionColor(c)}">${selectionNames[selectionColor(c)]}</span>`;
  const target=a=>data.meta.final_selection?.targets?.[a.group]||(a.group==='large'?25:10);
  function selectedByFilter(c){
    const color=$('selection-filter').value,solution=$('solution-filter').value;
    const subset=data.meta.green_subsets?.member_ids[color.replace('top','')];
    if(subset){
      if(selectionColor(c)!=='green'||!subset.includes(c.id))return false;
    }else if(color&&selectionColor(c)!==color)return false;
    if(!solution)return true;
    if(!c.solution_assessment)return false;
    return c.solution_assessment.solved===({solved:true,open:false,uncertain:null})[solution];
  }
  function solutionAssessment(c){
    const a=c.solution_assessment;
    if(!a)return '';
    const state=a.solved===true?'Public solution likely':a.solved===false?'Likely open':'Uncertain';
    const date=a.public_date?' · First documented '+esc(a.public_date):'';
    const proof=a.solution_url?' · '+link({url:a.solution_url},'Solution ↗'):'';
    const credit=a.attribution;
    const provenance=credit?`<p><strong>${credit.group==='ai_lab'?'AI lab':'Academic or independent researcher'}</strong> · ${link({url:credit.source_url},credit.credit)}. ${esc(credit.basis)}</p>`:'';
    const evidence=a.sources.map(r=>link(r)).join(' · ');
    return `<section class="solution-assessment" aria-label="Solution assessment"><p><strong>${state}</strong>${date}${proof}</p><details><summary>Assessment · ${a.probability_solved_upper_bound!=null?'&lt;'+Math.round(a.probability_solved_upper_bound*100):Math.round(a.probability_solved*100)}% probability that a public solution exists · ${esc(a.reviewed_on)}</summary>${paragraphs(a.reason)}${provenance}<p class="small">${evidence}</p>${a.date_source?'<p class="small">'+link({url:a.date_source},a.date_basis)+'</p>':''}</details></section>`;
  }
  function renderCompactCard(c){
    const r=c.references?.[0],draft=c.evidence!=='reviewed';
    const raw=(c.statement_review?c.formal:c.source_formulation?.text)||c.formal||c.title;
    const text=window.ATLAS_MATH.excerpt(raw);
    const duplicated=norm(text)===norm(c.title);
    const truncated=raw.length>700||c.source_excerpt_complete===false||/\[?…\]?|\[\.\.\.\]/.test(text)||c.legacy?.excerpt_truncated;
    const note=c.status==='excluded'?'Retired after review · '+c.review_outcome?.reason:c.status==='resolved'?'Resolved / materially changed · see the recorded update':draft?(truncated?'Incomplete excerpt · formulation and status need review':c.legacy?.statement_form==='index_label'?'Topic label · precise statement still to write':'Saved question · formulation and status need review'):(statuses[c.status]||c.status);
    const source=r?`<p class="compact-source"><a href="${esc(safeURL(r.url))}" target="_blank" rel="noopener noreferrer" title="${esc(r.title)}">Source ↗</a>${(r.year||c.year)?' · '+esc(r.year||c.year):''}</p>`:'';
    const refs=(c.references||[]).map(r=>`<li>${esc(r.authors||'')} ${r.year?'('+esc(r.year)+'). ':''}${link(r)}${r.locator?' · '+esc(r.locator):''}${r.pdf_url?' · '+link({url:r.pdf_url},'PDF ↗'):''}</li>`).join('');
    const progress=(c.progress||[]).map(p=>`<p>${esc(p.date)} · ${esc(p.text)}${cite(c,p.citation)}</p>`).join('');
    const savedQuestion=(c.working_summary||c.statement_review)&&draft?`<h3>Saved question</h3>${paragraphs(raw,c.source_formulation?'source-statement':'compact-question')}`:'';
    const expanded=draft?`${c.answer_criterion?'<h3>Answer criterion</h3>'+paragraphs(c.answer_criterion):''}${c.source_formulation?paragraphs(c.formal):''}${c.context?'<h3>Saved context</h3>'+paragraphs(c.context):''}${c.why?'<h3>Why it matters</h3>'+paragraphs(c.why):''}`:`<h3>Full statement</h3>${paragraphs(c.formal,'formal')}<h3>What would settle it</h3>${paragraphs(c.answer_criterion)}<h3>Context</h3>${paragraphs(c.context)}<h3>Why it matters</h3>${paragraphs(c.why)}`;
    return `<article class="problem-card compact-card selection-${selectionColor(c)}" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><a href="#${encodeURIComponent(c.id)}" data-action="permalink">${esc(c.id)}</a><span class="card-area">${esc(cardAreaLabel(c))}</span>${importanceBadge(c)}</div><div class="card-heading"><h2>${esc(c.title)}</h2></div>${selectionBadge(c)}${window.ATLAS_PROBLEM_AGE?.html(c)||''}${statementNotice(c)}${c.statement_review?paragraphs(text,'formal'):c.working_summary?workingSummary(c):duplicated?'':paragraphs(text,c.source_formulation?'source-statement':'compact-question')}<div class="compact-caption">${source}${c.solution_assessment?solutionAssessment(c):'<p class="compact-status">'+esc(note)+'</p>'}</div><details class="card-details"><summary>Details</summary><div class="details-body">${savedQuestion}${expanded}${window.ATLAS_DEFINITIONS.model(c)}${progress?'<h3>Saved progress</h3>'+progress:''}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}<p class="small muted">${esc(c.status_note||'')} ${esc(c.review_note||'')}</p></div></details>${relatedProblems(c)}<div class="card-footer">${canonicalLink(c)}</div></article>`;
  }
  function renderCard(c){
    if($('view').value==='compact')return renderCompactCard(c);
    const mainRef=c.references?.[0];
    const formal=paragraphs(c.formal,'formal').replace(/<\/p>$/,c.evidence==='reviewed'?cite(c,mainRef?.id)+'</p>':'</p>');
    const source=c.source_formulation?`<blockquote class="source-statement">${esc(c.source_formulation.text)}<span class="source-caption">${esc(c.source_formulation.caption||'Original source wording')}${cite(c,c.source_formulation.citation)}</span></blockquote>`:'';
    const progress=(c.progress||[]).map(p=>`<div class="progress-item"><time>${esc(p.date)}</time><p>${esc(p.text)}${cite(c,p.citation)}</p></div>`).join('');
    const refs=(c.references||[]).map((r,i)=>`<li id="${c.id}-ref-${i+1}">${esc(r.authors||'')} ${r.year?`(${esc(r.year)}). `:''}${link(r)}.${r.locator?` <span>${esc(r.locator)}.</span>`:''}${r.pdf_url?` <a href="${esc(safeURL(r.pdf_url))}" target="_blank" rel="noopener noreferrer">PDF ↗</a>`:''}${r.license?` <span class="muted">${esc(r.license)}</span>`:''}</li>`).join('');
    const literature=(c.related||[]).filter(r=>r&&typeof r==='object');
    const related=literature.length?`<h3>Later related literature</h3><p class="muted">Related papers; these references do not by themselves establish progress or resolution.</p><ol class="references">${literature.map(r=>`<li>${esc(r.year)} · ${link(r)}</li>`).join('')}</ol>`:'';
    const context=c.context_blocks?.length?c.context_blocks.map(b=>`<p>${esc(b.text)}${b.citation?cite(c,b.citation):''}</p>`).join(''):paragraphs(c.context);
    const questionLabel=c.answer_parts
      ? 'Separate yes/no answers for '+c.answer_parts.map(esc).join(' and ')
      : ({yes_no:'Yes / no',asymptotic_complexity:'Asymptotic complexity',exact_value:'Exact value',numerical_value:'Numerical value',function:'Function / curve'})[c.question_type]||'Answer';
    const resolution=c.answer_criterion?`<section class="card-section resolution"><h3>What would settle it · ${questionLabel}</h3>${paragraphs(c.answer_criterion)}</section>`:'';
    return `<article class="problem-card selection-${selectionColor(c)}" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><span>${esc(c.id)}</span><span class="card-area">${esc(cardAreaLabel(c))}</span></div>${importanceBadge(c)}<div class="card-heading"><h2>${esc(c.title_cs||c.title)}</h2></div>${selectionBadge(c)}<p class="subtitle">${c.title_cs?esc(c.title)+' · ':''}${esc(c.year||'Undated')}${mainRef?.authors?' · '+esc(mainRef.authors):''}</p>${window.ATLAS_PROBLEM_AGE?.html(c)||''}${statementNotice(c)}${workingSummary(c)}<section class="card-section"><h3>Problem statement</h3>${formal}${source}</section>${resolution}<section class="card-section"><h3>Context</h3>${context}</section><section class="card-section why"><h3>Why it matters</h3>${paragraphs(c.why)}</section>${c.solution_assessment?solutionAssessment(c):'<div class="status-line"><strong>'+(statuses[c.status]||esc(c.status))+'</strong> · '+esc(c.status_note||'')+'</div>'}<details class="card-details"><summary>Progress, definitions & references</summary><div class="details-body">${c.solution_assessment&&c.status_note?'<p class="small muted"><strong>Earlier review.</strong> '+esc(c.status_note)+'</p>':''}${window.ATLAS_DEFINITIONS.model(c)}${c.context_excerpt?`<blockquote class="source-statement">${esc(c.context_excerpt.text)}<span class="source-caption">${esc(c.context_excerpt.caption)}${cite(c,c.context_excerpt.citation)}</span></blockquote>`:''}<h3>Documented progress</h3><div class="progress">${progress||'<p>An individual progress review has not yet been completed.</p>'}</div>${related}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}${c.review_note?'<p class="small muted">'+esc(c.review_note)+'</p>':''}</div></details>${relatedProblems(c)}<div class="card-footer"><a href="#${encodeURIComponent(c.id)}" data-action="permalink">Link to card ↗</a>${canonicalLink(c)}${mainRef?link(mainRef,'Primary source ↗'):''}</div></article>`;
  }
  const math=root=>window.ATLAS_MATH.render(root);
  function loadMore(){const batch=state.matches.slice(state.shown,state.shown+state.batch);if(!batch.length)return;const wrap=document.createElement('div');wrap.innerHTML=batch.filter(c=>!document.getElementById(c.id)).map(renderCard).join('');while(wrap.firstChild){const c=wrap.firstChild;$('cards').appendChild(c);math(c);}state.shown+=batch.length;$('more').hidden=state.shown>=state.matches.length;}
  function filter(scroll=false){
    rebuildCategoryRanks();
    const terms=norm($('search').value).trim().split(/\s+/).filter(Boolean);
    const benchmark=$('benchmark').value,b=benchmarks[benchmark];
    // Rank the whole category before narrowing by search or category filters.
    const pool=data.cards.filter(c=>isActive(c)&&selectedByFilter(c)&&(!b||inBenchmark(c,benchmark)));
    state.matches=pool.filter(c=>(!state.areas.size||state.areas.has(publishedArea(c)))&&terms.every(t=>searchIndex.get(c.id).includes(t))).sort(catalogueOrder);
    state.shown=0;$('cards').replaceChildren();
    $('result-count').textContent=b?`${num(state.matches.length)} of ${num(pool.length)} problems · ${b.label}`:`${num(state.matches.length)} problems`;
    $('empty').hidden=state.matches.length>0;$('more').hidden=!state.matches.length;$('collapse').hidden=true;
    const url=new URL(location.href);
    if(b)url.searchParams.set('benchmark',benchmark);else url.searchParams.delete('benchmark');
    if($('selection-filter').value)url.searchParams.set('selection',$('selection-filter').value);else url.searchParams.delete('selection');
    if($('solution-filter').value)url.searchParams.set('solution',$('solution-filter').value);else url.searchParams.delete('solution');
    if($('view').value==='full')url.searchParams.set('view','full');else url.searchParams.delete('view');
    if(url.href!==location.href)history.replaceState(null,'',url);
    const chips=data.areas.filter(a=>state.areas.has(a.area)).map(a=>`<button class="filter-chip" data-area="${esc(a.area)}" aria-label="Remove category filter: ${esc(a.label)}">${esc(a.label)} ×</button>`);
    if($('selection-filter').value)chips.push(`<button class="filter-chip" data-filter="selection">${esc($('selection-filter').selectedOptions[0].textContent)} ×</button>`);
    if($('solution-filter').value)chips.push(`<button class="filter-chip" data-filter="solution">${esc($('solution-filter').selectedOptions[0].textContent)} ×</button>`);
    if(b)chips.push(`<button class="filter-chip" data-filter="benchmark">${b.label} ×</button>`);
    $('active-filters').innerHTML=chips.join('');
    loadMore();if(scroll)$('feed').scrollIntoView({behavior:'smooth',block:'start'});
  }
  function clear(){state.areas.clear();$('benchmark').value='';$('selection-filter').value='';$('solution-filter').value='';$('search').value='';renderAreas();filter();}
  async function go(id){
    const c=cardsById.get(id);if(!isActive(c)){toast('This problem is not in the active catalogue.');return;}
    if(!state.matches.some(x=>x.id===id))clear();
    let el=document.getElementById(id);
    if(!el){
      // Direct links reveal the requested card without changing the sorted result
      // set. Pagination skips an already revealed ID.
      const wrap=document.createElement('div');wrap.innerHTML=renderCard(c);
      el=wrap.firstChild;$('cards').prepend(el);math(el);
    }
    const navigation=++state.navigation;
    // Measure preceding cards before scrolling; virtualized height estimates can
    // otherwise leave a direct link several cards away from its target.
    $('cards').classList.add('navigating');
    await new Promise(requestAnimationFrame);
    if(navigation!==state.navigation)return;
    el.scrollIntoView({behavior:'instant',block:'start'});
    await new Promise(requestAnimationFrame);
    if(navigation!==state.navigation)return;
    $('cards').classList.remove('navigating');
    await new Promise(requestAnimationFrame);
    if(navigation!==state.navigation)return;
    el.scrollIntoView({behavior:'instant',block:'start'});
    el.classList.add('focused');setTimeout(()=>el.classList.remove('focused'),2500);
  }
  function selectionCounts(){
    const green=new Map(),total=new Map();
    for(const c of data.cards)if(isActive(c)){
      total.set(publishedArea(c),(total.get(publishedArea(c))||0)+1);
      if(selectionColor(c)==='green')green.set(publishedArea(c),(green.get(publishedArea(c))||0)+1);
    }
    return {green,total};
  }
  function renderAreas(){
    $('area-count').textContent=data.areas.length;
    const {green,total}=selectionCounts(),selected=[...green.values()].reduce((a,b)=>a+b,0),goal=data.areas.reduce((n,a)=>n+target(a),0);
    const catalogueSize=[...total.values()].reduce((sum,count)=>sum+count,0);
    $('stats').textContent=`${num(selected)} benchmark problems · ${num(catalogueSize)} catalogue cards · ${data.areas.length} categories`;
    $('selection-total').textContent=`${num(selected)} green / target ${num(goal)}`;
    $('areas').innerHTML=data.areas.map(a=>`<label class="area-option"><input type="checkbox" value="${esc(a.area)}" ${state.areas.has(a.area)?'checked':''}><span>${esc(a.label)}</span><span class="count ${(green.get(a.area)||0)===target(a)?'on-target':'off-target'}" title="${green.get(a.area)||0} green / target ${target(a)}; ${total.get(a.area)||0} total cards">${green.get(a.area)||0} / ${target(a)}</span></label>`).join('');
  }
  function updateCoverage(){
    const {green,total}=selectionCounts();
    $('selection-plan').textContent=`${data.areas.filter(a=>a.group==='large').length} large categories × 25 and ${data.areas.filter(a=>a.group==='small').length} small categories × 10. Category counts always include all green cards, even when search or color filters hide some of them.`;
    $('coverage-table').innerHTML=`<table><thead><tr><th>Category</th><th>Green</th><th>Target</th><th>All cards</th></tr></thead><tbody>${data.areas.map(a=>`<tr><th scope="row"><button class="category-link" data-area="${esc(a.area)}">${esc(a.label)}</button></th><td>${green.get(a.area)||0}</td><td>${target(a)}</td><td>${num(total.get(a.area)||0)}</td></tr>`).join('')}</tbody></table>`;
  }
  renderAreas();updateCoverage();
  $('coverage-table').addEventListener('click',e=>{const b=e.target.closest('[data-area]');if(!b)return;clear();state.areas.add(b.dataset.area);renderAreas();filter(true);});
  $('active-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.area)state.areas.delete(b.dataset.area);if(b.dataset.filter==='benchmark')$('benchmark').value='';if(b.dataset.filter==='selection')$('selection-filter').value='';if(b.dataset.filter==='solution')$('solution-filter').value='';renderAreas();filter();});
  $('selection-filter').addEventListener('change',()=>filter());
  $('solution-filter').addEventListener('change',()=>filter());
  $('benchmark').addEventListener('change',()=>{renderAreas();filter();});
  $('areas').addEventListener('change',event=>{const e=event.target;if(!e.matches('input[type=checkbox]'))return;e.checked?state.areas.add(e.value):state.areas.delete(e.value);filter();});
  let debounce;$('search').addEventListener('input',()=>{clearTimeout(debounce);debounce=setTimeout(()=>filter(),160);});
  $('view').addEventListener('change',()=>filter());
  $('clear').onclick=clear;$('empty-reset').onclick=clear;$('more').onclick=loadMore;
  $('filters-toggle').onclick=()=>{const opened=$('filters').classList.toggle('visible');$('filters-toggle').setAttribute('aria-expanded',String(opened));};
  $('collapse').onclick=()=>document.querySelectorAll('.card-details[open]').forEach(d=>d.open=false);
  $('top').onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
  $('cards').addEventListener('click',event=>{
    const related=event.target.closest('.related-problem-link');
    if(related){
      // Searching can hide the current hash target. Clicking its link again
      // does not emit hashchange, so reveal it explicitly in that case.
      if(!event.ctrlKey&&!event.metaKey&&!event.shiftKey&&!event.altKey&&related.hash===location.hash){
        event.preventDefault();go(decodeURIComponent(related.hash.slice(1)));
      }
      return;
    }
    const link=event.target.closest('[data-action="permalink"]');if(!link)return;
    event.preventDefault();history.replaceState(null,'',link.getAttribute('href'));toast('The address bar now contains a direct link to this card.');
  });
  $('cards').addEventListener('toggle',e=>{if(e.target.matches('.card-details')){if(e.target.open)math(e.target);$('collapse').hidden=!document.querySelector('.card-details[open]');}},true);
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!document.querySelector('dialog[open]')&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){e.preventDefault();$('search').focus();}if(e.key==='Escape')$('search').blur();});
  const revealSection=id=>{const el=$(id==='coverage'?'methodology':id);if(el?.matches('details.methodology')){el.open=true;if(id==='coverage')el.scrollIntoView({block:'start'});}};
  document.querySelectorAll('header .about-link').forEach(link=>link.addEventListener('click',()=>revealSection(link.hash.slice(1))));
  window.addEventListener('hashchange',()=>{const id=decodeURIComponent(location.hash.slice(1));if(cardsById.has(id))go(id);else revealSection(id);});
  // Load further cards only on request. Jumping to the footer or restoring a
  // reading position must not start an automatic chain of additional batches.
  const url=new URL(location.href),params=url.searchParams;
  // Old filter links must not reveal retired records or impose invisible filters.
  for(const key of ['detail','group','collection','scope','status','sort','reason','year','saved','new'])params.delete(key);
  history.replaceState(null,'',url);
  if(benchmarks[params.get('benchmark')])$('benchmark').value=params.get('benchmark');
  if(['solved','open','uncertain'].includes(params.get('solution')))$('solution-filter').value=params.get('solution');
  if([...$('selection-filter').options].some(o=>o.value===params.get('selection')))$('selection-filter').value=params.get('selection');
  $('view').value=params.get('view')==='full'?'full':'compact';
  rebuildCategoryRanks();renderAreas();filter();updateCoverage();const hash=decodeURIComponent(location.hash.slice(1));if(cardsById.has(hash))go(hash);else revealSection(hash);
  let currentVersion=data.meta.version||'',polling=false;
  async function applyPublication(update){
    if(!update?.version||!Array.isArray(update.cards)||!Array.isArray(update.areas))throw new Error('Invalid publication');
    const changes=[];
    const removed=new Set(update.removed_ids||[]);
    if(update.snapshot){const publishedIds=new Set(update.cards.map(c=>c.id));for(const c of data.cards)if(!publishedIds.has(c.id))removed.add(c.id);}
    // Full snapshots are needed after missed publications. Compare them in
    // chunks so an update never monopolizes the browser's event loop.
    for(let i=0;i<update.cards.length;i++){
      const c=update.cards[i];
      if(!cardsById.has(c.id)||JSON.stringify(cardsById.get(c.id))!==JSON.stringify(c))changes.push(c);
      if(i>0&&i%128===0)await new Promise(resolve=>setTimeout(resolve,0));
    }
    currentVersion=update.version;
    const areasChanged=JSON.stringify(data.areas)!==JSON.stringify(update.areas);
    if(!changes.length&&!areasChanged&&!removed.size){data.meta=update.meta;updateCoverage();return;}
    const shown=state.shown,scrollY=window.scrollY,toolbarBottom=document.querySelector('.toolbar').getBoundingClientRect().bottom,visible=[...document.querySelectorAll('.problem-card')].find(el=>el.getBoundingClientRect().bottom>toolbarBottom&&el.getBoundingClientRect().top<innerHeight);
    const anchor=visible?{id:visible.id,top:visible.getBoundingClientRect().top}:null;
    const open=[...document.querySelectorAll('.card-details[open]')].map(el=>el.closest('.problem-card').id);
    const openRelated=[...document.querySelectorAll('.related-more[open]')].map(el=>el.closest('.problem-card').id);
    const openAssessments=[...document.querySelectorAll('.solution-assessment details[open]')].map(el=>el.closest('.problem-card').id);
    const openOrigins=[...document.querySelectorAll('.problem-age[open]')].map(el=>el.closest('.problem-card').id);
    if(removed.size){data.cards=data.cards.filter(c=>!removed.has(c.id));for(const id of removed){cardsById.delete(id);searchIndex.delete(id);}}
    const positions=new Map(data.cards.map((c,i)=>[c.id,i]));
    for(const c of changes){if(positions.has(c.id))data.cards[positions.get(c.id)]=c;else data.cards.push(c);cardsById.set(c.id,c);}
    data.meta=update.meta;if(update.shared_definitions)data.shared_definitions=update.shared_definitions;data.areas=update.areas;areasByName=new Map(data.areas.map(a=>[a.area,a]));
    for(const c of data.cards)searchIndex.set(c.id,searchable(c));
    for(const a of state.areas)if(!areasByName.has(a))state.areas.delete(a);
    rebuildCategoryRanks();renderAreas();updateCoverage();
    $('cards').classList.add('publishing');
    // Publication size must not determine the number of DOM cards. Inserting
    // thousands of changed cards here used to freeze the page on bulk updates.
    filter();while(state.shown<Math.min(state.matches.length,shown))loadMore();
    // A direct-linked or newly re-ranked card may lie outside that prefix.
    // Retain only the reading cards, rather than rendering the entire
    // result set up to their new positions.
    const retained=new Set([anchor?.id,...open,...openRelated,...openAssessments,...openOrigins].filter(Boolean));
    for(const id of retained){
      if(document.getElementById(id)||!cardsById.has(id))continue;
      if(!state.matches.some(c=>c.id===id))continue;
      const wrap=document.createElement('div');wrap.innerHTML=renderCard(cardsById.get(id));
      const el=wrap.firstChild;$('cards').appendChild(el);math(el);
    }
    for(const id of open){const el=document.getElementById(id)?.querySelector('.card-details');if(el){el.open=true;math(el);}}
    for(const id of openRelated){const el=document.getElementById(id)?.querySelector('.related-more');if(el){el.open=true;math(el);}}
    for(const id of openAssessments){const el=document.getElementById(id)?.querySelector('.solution-assessment details');if(el)el.open=true;}
    for(const id of openOrigins){const el=document.getElementById(id)?.querySelector('.problem-age');if(el)el.open=true;}
    // Seed off-screen size estimates with the measured content height. Newly
    // inserted long cards otherwise fall back to 570px after virtualization
    // resumes, moving the reading anchor again after the initial restoration.
    const measureCards=()=>{
      const heights=[...$('cards').children].map(el=>{const style=getComputedStyle(el),padding=parseFloat(style.paddingTop)+parseFloat(style.paddingBottom),border=parseFloat(style.borderTopWidth)+parseFloat(style.borderBottomWidth);return [el,Math.max(0,el.getBoundingClientRect().height-padding-border)];});
      for(const [el,height] of heights)el.style.containIntrinsicBlockSize=`auto ${height}px`;
    };
    measureCards();
    if(document.fonts){await document.fonts.ready;measureCards();}
    const restore=()=>{if(anchor&&document.getElementById(anchor.id))window.scrollBy(0,document.getElementById(anchor.id).getBoundingClientRect().top-anchor.top);else window.scrollTo(0,scrollY);};
    restore();
    await new Promise(requestAnimationFrame);
    $('cards').classList.remove('publishing');
    await new Promise(requestAnimationFrame);
    restore();
    document.dispatchEvent(new Event('atlas:publication'));
  }
  async function checkUpdates(){
    if(polling||document.hidden)return;polling=true;
    try{const r=await fetch('version.json',{cache:'no-store'});if(!r.ok)throw new Error('Unavailable');const version=await r.json();if(version.version!==currentVersion){
      let update;
      if(version.delta){
        const deltaResponse=await fetch('updates-delta.json',{cache:'no-store'});
        if(deltaResponse.ok){const delta=await deltaResponse.json();if(delta.base_version===currentVersion&&delta.version===version.version)update=delta;}
      }
      if(!update){
        const fullResponse=await fetch('catalog.json',{cache:'no-store'});if(!fullResponse.ok)throw new Error('Unavailable');
        const catalogue=await fullResponse.json();
        if(catalogue.meta.version!==version.version)throw new Error('Publication in progress');
        update={...catalogue,version:catalogue.meta.version,snapshot:true};
      }
      await applyPublication(update);
    }}
    catch{/* Keep the current catalogue and retry on the next poll. */}
    finally{polling=false;}
  }
  if(['http:','https:'].includes(location.protocol)){setInterval(checkUpdates,4000);checkUpdates();document.addEventListener('visibilitychange',()=>{if(!document.hidden)checkUpdates();});}
  window.ATLAS_DEBUG={filter,go,state,data,isActive,checkUpdates,applyPublication,renderCard,math};
})();
