/* Local, dependency-light reader. All source-derived text is escaped before rendering. */
(() => {
  'use strict';
  const data=window.TCS_ATLAS;
  if(!data){document.getElementById('cards').textContent='The catalogue data could not be loaded.';return;}
  const $=id=>document.getElementById(id);
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const norm=s=>String(s??'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const safeURL=s=>{try{const u=new URL(s);return ['https:','http:'].includes(u.protocol)?u.href:'#';}catch{return '#';}};
  const num=n=>n.toLocaleString('en-US');
  const statuses={open:'Documented as open',source_open:'Open in the dated source',uncertain:'Current status unverified',resolved:'Resolved / materially changed',excluded:'Retired after review'};
  const state={areas:new Set(),matches:[],shown:0,batch:16,navigation:0};
  const cardsById=new Map(data.cards.map(c=>[c.id,c]));
  let areasByName=new Map(data.areas.map(a=>[a.area,a]));
  const areaLabel=area=>areasByName.get(area)?.label||area||'';
  const cardAreaLabel=c=>areaLabel(c.area);
  const benchmarks={top100:{label:'Top 100',quotas:{large:5,small:2}},top500:{label:'Top 500',quotas:{large:25,small:10}},top1000:{label:'Top 1000',tentative:true,quotas:{large:50,small:20}}};
  const isActive=c=>!!c&&!c.scope_exclusion&&!['resolved','excluded'].includes(c.status);
  let voteRanks=new Map(),areaPositions=new Map();
  const inBenchmark=(c,name)=>isActive(c)&&(voteRanks.get(c.id)||Infinity)<=(benchmarks[name]?.quotas[areasByName.get(c.area)?.group]||0);
  const benchmarkSummary=name=>{
    const b=benchmarks[name],cards=data.cards.filter(c=>inBenchmark(c,name));
    const assigned_target=data.areas.reduce((n,a)=>n+b.quotas[a.group],0);
    const reserved_target=(data.meta.taxonomy?.vacant_small_groups||0)*b.quotas.small;
    return {id:name,quotas:b.quotas,total:cards.length,target:assigned_target+reserved_target,assigned_target,reserved_target,shortfalls:data.areas.map(a=>({area:a.area,label:areaLabel(a.area),target:b.quotas[a.group],selected:cards.filter(c=>c.area===a.area).length})).filter(a=>a.selected<a.target).map(a=>({...a,missing:a.target-a.selected}))};
  };
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
  function paragraphs(text,cls=''){return String(text||'').split(/\n\n+/).filter(Boolean).map(p=>`<p${cls?` class="${cls}"`:''}>${esc(p)}</p>`).join('');}
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
  const importanceOrder=(a,b)=>Number(a.status==='resolved')-Number(b.status==='resolved')||(a.benchmark_focus?.position??Infinity)-(b.benchmark_focus?.position??Infinity)||(b.importance?.score??50)-(a.importance?.score??50)||a.id.localeCompare(b.id,'en');
  const votedOrder=(a,b)=>(window.ATLAS_VOTES?.score(b.id)||0)-(window.ATLAS_VOTES?.score(a.id)||0)||importanceOrder(a,b);
  const catalogueOrder=(a,b)=>(areaPositions.get(a.area)??Infinity)-(areaPositions.get(b.area)??Infinity)||votedOrder(a,b);
  function rebuildVoteRanks(){
    areaPositions=new Map(data.areas.map((a,i)=>[a.area,i]));
    voteRanks=new Map();const counts=new Map();
    for(const c of data.cards.filter(isActive).sort(catalogueOrder)){
      const rank=(counts.get(c.area)||0)+1;counts.set(c.area,rank);voteRanks.set(c.id,rank);
    }
  }
  function importanceBadge(c){
    return voteRanks.has(c.id)?`<span class="importance-badge">#${num(voteRanks.get(c.id))} in category</span>`:'';
  }
  const publicNotes=c=>window.ATLAS_COMMUNITY?.notesHTML(c.id)||'';
  function renderCompactCard(c){
    const r=c.references?.[0],draft=c.evidence!=='reviewed';
    const raw=(c.statement_review?c.formal:c.source_formulation?.text)||c.formal||c.title;
    const text=raw.length>700?raw.slice(0,700).replace(/\s+\S*$/,'')+' […]':raw;
    const duplicated=norm(text)===norm(c.title);
    const truncated=raw.length>700||c.source_excerpt_complete===false||/\[?…\]?|\[\.\.\.\]/.test(text)||c.legacy?.excerpt_truncated;
    const note=c.status==='excluded'?'Retired after review · '+c.review_outcome?.reason:c.status==='resolved'?'Resolved / materially changed · see the recorded update':draft?(truncated?'Incomplete excerpt · formulation and status need review':c.legacy?.statement_form==='index_label'?'Topic label · precise statement still to write':'Saved question · formulation and status need review'):(statuses[c.status]||c.status);
    const source=r?`<p class="compact-source"><a href="${esc(safeURL(r.url))}" target="_blank" rel="noopener noreferrer" title="${esc(r.title)}">Source ↗</a>${(r.year||c.year)?' · '+esc(r.year||c.year):''}</p>`:'';
    const refs=(c.references||[]).map(r=>`<li>${esc(r.authors||'')} ${r.year?'('+esc(r.year)+'). ':''}${link(r)}${r.locator?' · '+esc(r.locator):''}${r.pdf_url?' · '+link({url:r.pdf_url},'PDF ↗'):''}</li>`).join('');
    const progress=(c.progress||[]).map(p=>`<p>${esc(p.date)} · ${esc(p.text)}${cite(c,p.citation)}</p>`).join('');
    const savedQuestion=(c.working_summary||c.statement_review)&&draft?`<h3>Saved question</h3>${paragraphs(raw,c.source_formulation?'source-statement':'compact-question')}`:'';
    const expanded=draft?`${c.answer_criterion?'<h3>Answer criterion</h3>'+paragraphs(c.answer_criterion):''}${c.source_formulation?paragraphs(c.formal):''}${c.context?'<h3>Saved context</h3>'+paragraphs(c.context):''}${c.why?'<h3>Why it matters</h3>'+paragraphs(c.why):''}`:`<h3>Full statement</h3>${paragraphs(c.formal,'formal')}<h3>What would settle it</h3>${paragraphs(c.answer_criterion)}<h3>Context</h3>${paragraphs(c.context)}<h3>Why it matters</h3>${paragraphs(c.why)}`;
    return `<article class="problem-card compact-card" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><a href="#${encodeURIComponent(c.id)}" data-action="permalink">${esc(c.id)}</a><span>${esc(cardAreaLabel(c))}</span>${importanceBadge(c)}</div><div class="card-heading"><h2>${esc(c.title)}</h2></div>${window.ATLAS_VOTES?.html(c.id)||''}${statementNotice(c)}${c.statement_review?paragraphs(text,'formal'):c.working_summary?workingSummary(c):duplicated?'':paragraphs(text,c.source_formulation?'source-statement':'compact-question')}<div class="compact-caption">${source}<p class="compact-status">${esc(note)}</p></div><details class="card-details"><summary>Details</summary><div class="details-body">${savedQuestion}${expanded}${c.definitions?'<h3>Model & notation</h3>'+paragraphs(c.definitions,'formal'):''}${progress?'<h3>Saved progress</h3>'+progress:''}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}<p class="small muted">${esc(c.status_note||'')} ${esc(c.review_note||'')}</p></div></details>${relatedProblems(c)}${publicNotes(c)}<div class="card-footer"><button type="button" data-public-note="${esc(c.id)}">Add public note</button>${canonicalLink(c)}</div></article>`;
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
    const questionLabel=({yes_no:'Yes / no',asymptotic_complexity:'Asymptotic complexity',exact_value:'Exact value',numerical_value:'Numerical value',function:'Function / curve'})[c.question_type]||'Answer';
    const resolution=c.answer_criterion?`<section class="card-section resolution"><h3>What would settle it · ${questionLabel}</h3>${paragraphs(c.answer_criterion)}</section>`:'';
    return `<article class="problem-card" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><span>${esc(c.id)}</span><span>${esc(cardAreaLabel(c))}</span></div>${importanceBadge(c)}<div class="card-heading"><h2>${esc(c.title_cs||c.title)}</h2></div>${window.ATLAS_VOTES?.html(c.id)||''}<p class="subtitle">${c.title_cs?esc(c.title)+' · ':''}${esc(c.year||'Undated')}${mainRef?.authors?' · '+esc(mainRef.authors):''}</p>${statementNotice(c)}${workingSummary(c)}<section class="card-section"><h3>Problem statement</h3>${formal}${source}</section>${resolution}<section class="card-section"><h3>Context</h3>${context}</section><section class="card-section why"><h3>Why it matters</h3>${paragraphs(c.why)}</section><div class="status-line"><strong>${statuses[c.status]||esc(c.status)}</strong> · ${esc(c.status_note||'')}</div><details class="card-details"><summary>Progress, definitions & references</summary><div class="details-body">${c.definitions?'<h3>Model & notation</h3>'+paragraphs(c.definitions,'formal'):''}${c.context_excerpt?`<blockquote class="source-statement">${esc(c.context_excerpt.text)}<span class="source-caption">${esc(c.context_excerpt.caption)}${cite(c,c.context_excerpt.citation)}</span></blockquote>`:''}<h3>Documented progress</h3><div class="progress">${progress||'<p>An individual progress review has not yet been completed.</p>'}</div>${related}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}${c.review_note?'<p class="small muted">'+esc(c.review_note)+'</p>':''}</div></details>${relatedProblems(c)}${publicNotes(c)}<div class="card-footer"><button type="button" data-public-note="${esc(c.id)}">Add public note</button><a href="#${encodeURIComponent(c.id)}" data-action="permalink">Link to card ↗</a>${canonicalLink(c)}${mainRef?link(mainRef,'Primary source ↗'):''}</div></article>`;
  }
  function math(root){if(typeof renderMathInElement==='function')renderMathInElement(root,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false},{left:'$',right:'$',display:false}],throwOnError:false,trust:false,strict:'ignore',ignoredClasses:['source-statement','references','public-notes']});}
  function loadMore(){const batch=state.matches.slice(state.shown,state.shown+state.batch);if(!batch.length)return;const wrap=document.createElement('div');wrap.innerHTML=batch.filter(c=>!document.getElementById(c.id)).map(renderCard).join('');while(wrap.firstChild){const c=wrap.firstChild;$('cards').appendChild(c);math(c);}state.shown+=batch.length;$('more').hidden=state.shown>=state.matches.length;}
  function filter(scroll=false){
    rebuildVoteRanks();
    const terms=norm($('search').value).trim().split(/\s+/).filter(Boolean);
    const benchmark=$('benchmark').value,b=benchmarks[benchmark];
    // Rank the whole category before narrowing by search or category filters.
    const pool=data.cards.filter(c=>isActive(c)&&(!b||inBenchmark(c,benchmark)));
    state.matches=pool.filter(c=>(!state.areas.size||state.areas.has(c.area))&&terms.every(t=>searchIndex.get(c.id).includes(t))).sort(catalogueOrder);
    state.shown=0;$('cards').replaceChildren();
    $('result-count').textContent=b?`${num(state.matches.length)} of ${num(pool.length)} problems · ${b.label}`:`${num(state.matches.length)} problems`;
    $('empty').hidden=state.matches.length>0;$('more').hidden=!state.matches.length;$('collapse').hidden=true;
    const url=new URL(location.href);
    if(b)url.searchParams.set('benchmark',benchmark);else url.searchParams.delete('benchmark');
    if($('view').value==='full')url.searchParams.set('view','full');else url.searchParams.delete('view');
    if(url.href!==location.href)history.replaceState(null,'',url);
    const chips=data.areas.filter(a=>state.areas.has(a.area)).map(a=>`<button class="filter-chip" data-area="${esc(a.area)}" aria-label="Remove category filter: ${esc(a.label)}">${esc(a.label)} ×</button>`);
    if(b)chips.push(`<button class="filter-chip" data-filter="benchmark">${b.label} ×</button>`);
    $('active-filters').innerHTML=chips.join('');
    loadMore();if(scroll)$('feed').scrollIntoView({behavior:'smooth',block:'start'});
  }
  function clear(){state.areas.clear();$('benchmark').value='';$('search').value='';renderAreas();filter();}
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
  function updateStats(){$('stats').textContent=`${num(data.cards.filter(isActive).length)} problems · ${data.areas.length} categories`;}
  function renderAreas(){
    $('area-count').textContent=data.areas.length;
    const benchmark=$('benchmark').value,counts=new Map();
    for(const c of data.cards)if(isActive(c)&&(!benchmark||inBenchmark(c,benchmark)))counts.set(c.area,(counts.get(c.area)||0)+1);
    $('areas').innerHTML=data.areas.map(a=>`<label class="area-option"><input type="checkbox" value="${esc(a.area)}" ${state.areas.has(a.area)?'checked':''}><span>${esc(a.label)}</span><span class="count">${num(counts.get(a.area)||0)}</span></label>`).join('');
  }
  function updateCoverage(){
    const active=data.cards.filter(isActive),counts=new Map();
    for(const c of active)counts.set(c.area,(counts.get(c.area)||0)+1);
    const selections=Object.keys(benchmarks).map(name=>{const summary=benchmarkSummary(name),b=benchmarks[name];return `${b.tentative?'The legacy '+b.label+' view':b.label} uses the first ${b.quotas.large} problems per large category and ${b.quotas.small} per small category: ${num(summary.total)} of ${num(summary.target)} places filled${summary.reserved_target?`, including ${num(summary.reserved_target)} places reserved for future categories`:''}.`;});
    $('selection-plan').textContent=selections.join(' ')+' Within each category, thumbs up minus thumbs down determines both order and selection; ties use the catalogue priority. Top 100 is contained in Top 500, which is contained in Top 1000. Search and category filters narrow these selections without filling their places with other problems.';
    $('coverage-table').innerHTML=`<table><thead><tr><th>Category</th>${Object.values(benchmarks).map(b=>`<th>${b.tentative?'Possible ':''}${b.label}</th>`).join('')}<th>Active problems</th></tr></thead><tbody>${data.areas.map(a=>`<tr><th scope="row"><button class="category-link" data-area="${esc(a.area)}">${esc(a.label)}</button></th>${Object.values(benchmarks).map(b=>`<td>${b.quotas[a.group]}</td>`).join('')}<td>${num(counts.get(a.area)||0)}</td></tr>`).join('')}</tbody></table>`;
  }
  updateStats();renderAreas();updateCoverage();
  $('coverage-table').addEventListener('click',e=>{const b=e.target.closest('[data-area]');if(!b)return;clear();state.areas.add(b.dataset.area);renderAreas();filter(true);});
  $('active-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.area)state.areas.delete(b.dataset.area);if(b.dataset.filter==='benchmark')$('benchmark').value='';renderAreas();filter();});
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
  $('view').value=params.get('view')==='full'?'full':'compact';
  rebuildVoteRanks();renderAreas();filter();updateCoverage();const hash=decodeURIComponent(location.hash.slice(1));if(cardsById.has(hash))go(hash);else revealSection(hash);
  let voteFrame=0;
  document.addEventListener('atlas:votes',event=>{
    cancelAnimationFrame(voteFrame);
    voteFrame=requestAnimationFrame(()=>{
      const scrollY=window.scrollY,toolbarBottom=document.querySelector('.toolbar').getBoundingClientRect().bottom;
      const visible=document.getElementById(event.detail?.problemId)||[...$('cards').children].find(el=>el.getBoundingClientRect().bottom>toolbarBottom&&el.getBoundingClientRect().top<innerHeight);
      const anchor=visible?{id:visible.id,top:visible.getBoundingClientRect().top}:null;
      const existing=new Map([...$('cards').children].map(el=>[el.id,el])),shown=state.shown;
      const terms=norm($('search').value).trim().split(/\s+/).filter(Boolean),benchmark=$('benchmark').value,b=benchmarks[benchmark];
      rebuildVoteRanks();
      const pool=data.cards.filter(c=>isActive(c)&&(!b||inBenchmark(c,benchmark)));
      state.matches=pool.filter(c=>(!state.areas.size||state.areas.has(c.area))&&terms.every(t=>searchIndex.get(c.id).includes(t))).sort(catalogueOrder);
      state.shown=Math.min(shown||state.batch,state.matches.length);
      const selected=new Set(state.matches.slice(0,state.shown).map(c=>c.id));
      for(const [id,el] of existing)if(id===anchor?.id||el.querySelector('details[open]'))selected.add(id);
      const fragment=document.createDocumentFragment();
      for(const c of state.matches){
        if(!selected.has(c.id))continue;
        let el=existing.get(c.id);
        if(!el){const wrap=document.createElement('div');wrap.innerHTML=renderCard(c);el=wrap.firstChild;math(el);}
        const badge=el.querySelector('.importance-badge');if(badge)badge.textContent=`#${num(voteRanks.get(c.id))} in category`;
        fragment.appendChild(el);
      }
      $('cards').replaceChildren(fragment);
      $('more').hidden=state.shown>=state.matches.length;$('empty').hidden=state.matches.length>0;
      $('result-count').textContent=b?`${num(state.matches.length)} of ${num(pool.length)} problems · ${b.label}`:`${num(state.matches.length)} problems`;
      renderAreas();updateCoverage();
      if(anchor&&document.getElementById(anchor.id))window.scrollBy(0,document.getElementById(anchor.id).getBoundingClientRect().top-anchor.top);else window.scrollTo(0,scrollY);
    });
  });
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
    if(removed.size){data.cards=data.cards.filter(c=>!removed.has(c.id));for(const id of removed){cardsById.delete(id);searchIndex.delete(id);}}
    const positions=new Map(data.cards.map((c,i)=>[c.id,i]));
    for(const c of changes){if(positions.has(c.id))data.cards[positions.get(c.id)]=c;else data.cards.push(c);cardsById.set(c.id,c);}
    data.meta=update.meta;data.areas=update.areas;areasByName=new Map(data.areas.map(a=>[a.area,a]));
    // A metadata-only rename changes search terms even when every card is unchanged.
    for(const c of areasChanged?data.cards:changes)searchIndex.set(c.id,searchable(c));
    for(const a of state.areas)if(!areasByName.has(a))state.areas.delete(a);
    rebuildVoteRanks();updateStats();renderAreas();updateCoverage();
    $('cards').classList.add('publishing');
    // Publication size must not determine the number of DOM cards. Inserting
    // thousands of changed cards here used to freeze the page on bulk updates.
    filter();while(state.shown<Math.min(state.matches.length,shown))loadMore();
    // A direct-linked or newly re-ranked card may lie outside that prefix.
    // Retain only the reading cards, rather than rendering the entire
    // result set up to their new positions.
    const retained=new Set([anchor?.id,...open,...openRelated].filter(Boolean));
    for(const id of retained){
      if(document.getElementById(id)||!cardsById.has(id))continue;
      if(!state.matches.some(c=>c.id===id))continue;
      const wrap=document.createElement('div');wrap.innerHTML=renderCard(cardsById.get(id));
      const el=wrap.firstChild;$('cards').appendChild(el);math(el);
    }
    for(const id of open){const el=document.getElementById(id)?.querySelector('.card-details');if(el){el.open=true;math(el);}}
    for(const id of openRelated){const el=document.getElementById(id)?.querySelector('.related-more');if(el){el.open=true;math(el);}}
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
  window.ATLAS_DEBUG={filter,go,state,data,isActive,checkUpdates,applyPublication};
})();
