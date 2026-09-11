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
  const storage={get(k,fallback){try{return JSON.parse(localStorage.getItem(k))??fallback;}catch{return fallback;}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v));return true;}catch{return false;}}};
  const saved=new Set(storage.get('tcs-atlas-saved',[])),notes=storage.get('tcs-atlas-notes',{});
  const statuses={open:'Documented as open',source_open:'Open in the dated source',uncertain:'Current status unverified',resolved:'Resolved / materially changed',excluded:'Retired after review'};
  const evidence={reviewed:'Detailed card',source:'Short draft · source excerpt',index:'Short draft · saved index'};
  const evidenceLabel=c=>c.review_outcome?.complete?'Reviewed disposition':c.textbook_import&&c.evidence!=='reviewed'?(c.textbook_import.kind==='research_direction'?'Short draft · research direction':'Short draft · textbook/survey'):c.proposal_import&&c.evidence!=='reviewed'?'Short draft · research proposal':(evidence[c.evidence]||c.evidence);
  const state={areas:new Set(),matches:[],shown:0,batch:16,observer:null,navigation:0};
  const cardsById=new Map(data.cards.map(c=>[c.id,c]));
  let areasByName=new Map(data.areas.map(a=>[a.area,a]));
  const areaLabel=area=>areasByName.get(area)?.label||area||'';
  const cardAreaLabel=c=>areaLabel(c.scope_exclusion?.previous_area||c.area);
  const benchmarks={top100:{label:'Top 100',quotas:{large:5,small:2}},top1000:{label:'Top 1000',quotas:{large:50,small:20}}};
  const inBenchmark=(c,name)=>!c.scope_exclusion&&!['resolved','excluded'].includes(c.status)&&Number.isInteger(c.importance_rank)&&c.importance_rank>0&&c.importance_rank<=(benchmarks[name]?.quotas[areasByName.get(c.area)?.group]||0);
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
  function statementText(c){
    return [c.title_cs||c.title,c.statement_review?c.formal:(c.source_formulation?.text||c.formal),
      c.definitions?'Definitions\n'+c.definitions:'',c.answer_criterion?'Answer criterion\n'+c.answer_criterion:'',
      c.statement_review?.remaining_issue?'Statement needs specification\n'+c.statement_review.remaining_issue:'',
      'Status: '+(c.status_note||statuses[c.status]||c.status),...(c.references||[]).map(r=>r.url)].filter(Boolean).join('\n\n');
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
  function importanceBadge(c){
    if(c.scope_exclusion)return `<span class="importance-badge provisional" title="${esc(c.scope_exclusion.reason)}">${c.scope_exclusion.kind==='preliminary_quality'?'Preliminarily removed':'Outside selection scope'} · archived</span>`;
    const provisional=c.importance?.method!=='editorial';
    return `<span class="importance-badge ${provisional?'provisional':''}" title="${esc(c.importance?.reason||'Importance assessment pending')}">Category #${num(c.importance_rank||1)} · ${provisional?'provisional':'editorial'}</span>`;
  }
  function importanceReason(c){if(c.scope_exclusion)return `<h3>${c.scope_exclusion.kind==='preliminary_quality'?'Preliminary removal':'Selection scope'}</h3><p>${esc(c.scope_exclusion.reason)}</p>${c.scope_exclusion.previous_area?`<p>Previous category: ${esc(areaLabel(c.scope_exclusion.previous_area))}. The full record is preserved and can be reinstated.</p>`:''}`;return `<h3>Importance in this category</h3><p>${esc(c.importance?.reason||'Importance assessment pending')} ${c.importance_rank?`Position ${num(c.importance_rank)} of ${num(c.importance_count)} candidates. The focus prefix balances importance and diversity; remaining ties use the stable card ID.`:''}</p>${c.benchmark_focus?`<h3>Top 100 selection · ${esc(c.benchmark_focus.topic)}</h3><p>${esc(c.benchmark_focus.reason)}</p>`:''}`;}
  function privateNote(c){
    return `<label class="note-label" for="note-${esc(c.id)}">My private note</label><textarea class="note-box" id="note-${esc(c.id)}" data-note="${esc(c.id)}" placeholder="An idea, correction or source to keep privately…">${esc(notes[c.id]||'')}</textarea><p class="note-save-status small muted" id="note-status-${esc(c.id)}" role="status">${notes[c.id]?'Saved in this browser. Included in Export selection.':'Private to this browser. Saves automatically; included in Export selection.'}</p>`;
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
    const expanded=draft?`${c.answer_criterion?'<h3>Answer criterion</h3>'+paragraphs(c.answer_criterion):''}${c.source_formulation?paragraphs(c.formal):''}${c.context?'<h3>Saved context</h3>'+paragraphs(c.context):''}${c.why?'<h3>Saved selection note</h3>'+paragraphs(c.why):''}`:`<h3>Full statement</h3>${paragraphs(c.formal,'formal')}<h3>What would settle it</h3>${paragraphs(c.answer_criterion)}<h3>Context</h3>${paragraphs(c.context)}<h3>Why it matters</h3>${paragraphs(c.why)}`;
    return `<article class="problem-card compact-card" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><a href="#${encodeURIComponent(c.id)}" data-action="permalink">${esc(c.id)}</a><span class="pill ${draft?'uncertain':'reviewed'}">${esc(evidenceLabel(c))}</span><span>${esc(cardAreaLabel(c))}</span>${importanceBadge(c)}</div><div class="card-heading"><h2>${esc(c.title)}</h2><button type="button" class="save" data-action="save" aria-pressed="${saved.has(c.id)}" aria-label="${saved.has(c.id)?'Unsave problem':'Save problem'}">${saved.has(c.id)?'Saved':'Save +'}</button></div>${statementNotice(c)}${c.statement_review?paragraphs(text,'formal'):c.working_summary?workingSummary(c):duplicated?'':paragraphs(text,c.source_formulation?'source-statement':'compact-question')}<div class="compact-caption">${source}<p class="compact-status">${esc(note)}</p></div><details class="card-details"><summary>Details</summary><div class="details-body">${savedQuestion}${expanded}${importanceReason(c)}${c.definitions?'<h3>Model & notation</h3>'+paragraphs(c.definitions,'formal'):''}${progress?'<h3>Saved progress</h3>'+progress:''}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}<p class="small muted">${esc(c.status_note||'')} ${esc(c.review_note||'')}</p>${privateNote(c)}</div></details>${publicNotes(c)}<div class="card-footer"><button type="button" data-public-note="${esc(c.id)}">Add public note</button><button data-action="note">My private note</button><button data-action="copy">Copy statement</button>${canonicalLink(c)}</div></article>`;
  }
  function renderCard(c){
    if($('view').value==='compact')return renderCompactCard(c);
    const mainRef=c.references?.[0];
    const formal=paragraphs(c.formal,'formal').replace(/<\/p>$/,c.evidence==='reviewed'?cite(c,mainRef?.id)+'</p>':'</p>');
    const source=c.source_formulation?`<blockquote class="source-statement">${esc(c.source_formulation.text)}<span class="source-caption">${esc(c.source_formulation.caption||'Original source wording')}${cite(c,c.source_formulation.citation)}</span></blockquote>`:'';
    const progress=(c.progress||[]).map(p=>`<div class="progress-item"><time>${esc(p.date)}</time><p>${esc(p.text)}${cite(c,p.citation)}</p></div>`).join('');
    const refs=(c.references||[]).map((r,i)=>`<li id="${c.id}-ref-${i+1}">${esc(r.authors||'')} ${r.year?`(${esc(r.year)}). `:''}${link(r)}.${r.locator?` <span>${esc(r.locator)}.</span>`:''}${r.pdf_url?` <a href="${esc(safeURL(r.pdf_url))}" target="_blank" rel="noopener noreferrer">PDF ↗</a>`:''}${r.license?` <span class="muted">${esc(r.license)}</span>`:''}</li>`).join('');
    const related=(c.related||[]).length?`<h3>Later related literature</h3><p class="muted">Related papers; these references do not by themselves establish progress or resolution.</p><ol class="references">${c.related.map(r=>`<li>${esc(r.year)} · ${link(r)}</li>`).join('')}</ol>`:'';
    const context=c.context_blocks?.length?c.context_blocks.map(b=>`<p>${esc(b.text)}${b.citation?cite(c,b.citation):''}</p>`).join(''):paragraphs(c.context);
    const resolution=c.answer_criterion?`<section class="card-section resolution"><h3>What would settle it · ${c.question_type==='asymptotic_complexity'?'Asymptotic complexity':c.question_type==='exact_value'?'Exact value':'Yes / no'}</h3>${paragraphs(c.answer_criterion)}</section>`:'';
    return `<article class="problem-card" id="${esc(c.id)}" data-id="${esc(c.id)}"><div class="card-meta"><span>${esc(c.id)}</span>${c.is_new?'<span class="pill new">NEW</span>':''}<span class="pill ${c.evidence==='reviewed'?'reviewed':''}">${esc(evidenceLabel(c))}</span><span>${esc(cardAreaLabel(c))}</span></div>${importanceBadge(c)}<div class="card-heading"><h2>${esc(c.title_cs||c.title)}</h2><button type="button" class="save" data-action="save" aria-pressed="${saved.has(c.id)}" aria-label="${saved.has(c.id)?'Unsave problem':'Save problem'}">${saved.has(c.id)?'Saved':'Save +'}</button></div><p class="subtitle">${c.title_cs?esc(c.title)+' · ':''}${esc(c.year||'Undated')}${mainRef?.authors?' · '+esc(mainRef.authors):''}</p>${statementNotice(c)}${workingSummary(c)}<section class="card-section"><h3>${c.review_outcome?.complete?'Review outcome':c.evidence==='index'?'Legacy statement':'Problem statement'}</h3>${formal}${source}</section>${resolution}<section class="card-section"><h3>Context</h3>${context}</section><section class="card-section why"><h3>Why it matters</h3>${paragraphs(c.why)}${importanceReason(c)}</section><div class="status-line"><strong>${statuses[c.status]||esc(c.status)}</strong> · ${esc(c.status_note||'')}</div><details class="card-details"><summary>Progress, definitions & references</summary><div class="details-body">${c.definitions?'<h3>Model & notation</h3>'+paragraphs(c.definitions,'formal'):''}${c.context_excerpt?`<blockquote class="source-statement">${esc(c.context_excerpt.text)}<span class="source-caption">${esc(c.context_excerpt.caption)}${cite(c,c.context_excerpt.citation)}</span></blockquote>`:''}<h3>Documented progress</h3><div class="progress">${progress||'<p>An individual progress review has not yet been completed.</p>'}</div>${related}<h3>References</h3><ol class="references">${refs}</ol>${textbookNotes(c)}${c.review_note?'<p class="small muted">'+esc(c.review_note)+'</p>':''}${privateNote(c)}</div></details>${publicNotes(c)}<div class="card-footer"><button type="button" data-public-note="${esc(c.id)}">Add public note</button><button data-action="note">My private note</button><a href="#${encodeURIComponent(c.id)}" data-action="permalink">Link to card ↗</a><button data-action="copy">Copy statement</button>${canonicalLink(c)}${mainRef?link(mainRef,'Primary source ↗'):''}<span>${esc(c.criterion_label||'')}</span></div></article>`;
  }
  function math(root){if(typeof renderMathInElement==='function')renderMathInElement(root,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false},{left:'$',right:'$',display:false}],throwOnError:false,trust:false,strict:'ignore',ignoredClasses:['source-statement','references','note-box']});}
  function loadMore(){const batch=state.matches.slice(state.shown,state.shown+state.batch);if(!batch.length)return;const wrap=document.createElement('div');wrap.innerHTML=batch.filter(c=>!document.getElementById(c.id)).map(renderCard).join('');while(wrap.firstChild){const c=wrap.firstChild;$('cards').appendChild(c);math(c);}state.shown+=batch.length;$('more').hidden=state.shown>=state.matches.length;}
  function filter(scroll=false){
    const terms=norm($('search').value).trim().split(/\s+/).filter(Boolean),ev=$('evidence').value,status=$('status').value,reason=$('reason').value,yr=Number($('year').value)||0,group=$('group').value;
    // Category ranks come from the full publication; filtering never fills a
    // vacated benchmark place with a lower-ranked matching card.
    const benchmark=$('benchmark').value,b=benchmarks[benchmark],pool=b?data.cards.filter(c=>inBenchmark(c,benchmark)):data.cards;
    state.matches=pool.filter(c=>($('scope').value==='all'||($('scope').value==='archived'?!!c.scope_exclusion:!c.scope_exclusion))&&(!$('new-only').checked||c.is_new)&&(!$('saved-only').checked||saved.has(c.id))&&(!$('textbook-only').checked||c.textbook_notes?.length)&&(!state.areas.size||state.areas.has(c.area))&&(!group||areasByName.get(c.area)?.group===group)&&(!ev||(ev==='drafts'?(c.evidence!=='reviewed'&&!c.review_outcome?.complete):c.evidence===ev))&&(!status||c.status===status)&&(!reason||c.criterion===reason)&&(!yr||c.year>=yr)&&terms.every(t=>searchIndex.get(c.id).includes(t)));
    const sort=$('sort').value;state.matches.sort((a,b)=>(sort==='recent'?(b.updated_at||b.published_at||'').localeCompare(a.updated_at||a.published_at||''):sort==='newest'?(b.year||0)-(a.year||0):sort==='oldest'?(a.year||9999)-(b.year||9999):sort==='title'?(a.title_cs||a.title).localeCompare(b.title_cs||b.title,'en'):0)||importanceOrder(a,b));
    state.shown=0;$('cards').replaceChildren();$('result-count').textContent=b?`${num(state.matches.length)} of ${num(pool.length)} problems · ${b.label}`:`${num(state.matches.length)} problems`;$('empty').hidden=state.matches.length>0;$('more').hidden=!state.matches.length;$('collapse').hidden=true;
    $('benchmark-note').hidden=!b;
    if(b){
      const summary=benchmarkSummary(benchmark);
      $('benchmark-note').innerHTML=`<strong>${b.label} · ${num(pool.length)}/${num(summary.target)} places filled</strong><span>First ${b.quotas.large} per large category + first ${b.quotas.small} per small category. The first 5/2 places balance importance and diversity. Other filters narrow this selection.${summary.reserved_target?` ${num(summary.reserved_target)} places are reserved for future categories.`:''}${pool.length<summary.target?' Unfilled places remain visible in the selection review.':''} <a href="benchmark-selection.md">Selection review</a></span>`;
    }
    const url=new URL(location.href),requestedBenchmark=b?benchmark:null;
    if(url.searchParams.get('benchmark')!==requestedBenchmark){if(b)url.searchParams.set('benchmark',benchmark);else url.searchParams.delete('benchmark');history.replaceState(null,'',url);}
    const chips=data.areas.filter(a=>state.areas.has(a.area)).map(a=>`<button class="filter-chip" data-area="${esc(a.area)}" aria-label="Remove area filter: ${esc(areaLabel(a.area))}">${esc(areaLabel(a.area))} ×</button>`);
    for(const id of ['benchmark','evidence','status','reason','year','group','scope'])if($(id).value)chips.push(`<button class="filter-chip" data-filter="${id}">${esc($(id).tagName==='SELECT'?$(id).selectedOptions[0].textContent:'From '+$(id).value)} ×</button>`);
    for(const [id,label] of [['new-only','New additions'],['saved-only','Saved problems'],['textbook-only','Textbook and survey questions']])if($(id).checked)chips.push(`<button class="filter-chip" data-filter="${id}">${label} ×</button>`);
    $('active-filters').innerHTML=chips.join('');
    const advanced=['evidence','status','reason','year','group','scope'].filter(id=>$(id).value).length+Number($('new-only').checked)+Number($('textbook-only').checked)+Number($('view').value!=='compact');
    $('advanced-count').textContent=advanced?`(${advanced})`:'';
    $('quality-note').textContent=ev==='reviewed'?'Individually written statements and progress notes. Review dates and source limitations are recorded on each card.':'The Selection scope filter switches between candidates, the archive (including preliminary removals) and all saved records. Working summaries give five-sentence explanations based on saved sources. Short drafts also retain their source questions or topic labels; some excerpts are incomplete. Their precise formulations and current open status still need review. Add a public note to share feedback, or keep a private note in this browser.';
    if(sort==='importance')$('quality-note').textContent+=` Ordered by editorial importance: ${num(state.matches.filter(c=>c.importance?.method==='editorial').length)} assessed, ${num(state.matches.filter(c=>c.importance?.method!=='editorial').length)} provisional in this view. Shared scores are ties; provisional drafts still need an importance assessment. Resolved records appear last.`;
    loadMore();if(scroll)$('feed').scrollIntoView({behavior:'smooth',block:'start'});
  }
  function clear(){state.areas.clear();for(const id of ['benchmark','search','evidence','status','reason','year','area-search','group','scope'])$(id).value='';renderAreas();$('new-only').checked=false;$('saved-only').checked=false;$('textbook-only').checked=false;$('sort').value='importance';filter();}
  async function go(id){
    const c=cardsById.get(id);if(!c){toast('This card is not in the catalogue.');return;}
    if(!state.matches.some(x=>x.id===id))clear();
    let el=document.getElementById(id);
    if(!el){
      // Direct links reveal the requested card without changing the sorted result
      // set (and therefore the export). Pagination skips an already revealed ID.
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
  function updateStats(){$('stats').textContent=`${num(data.meta.taxonomy?.candidate_count??data.cards.length)} candidates · ${data.areas.length} categories`;}
  function updateAreaVisibility(){
    const q=norm($('area-search').value),group=$('group').value;
    document.querySelectorAll('.area-group').forEach(section=>{
      section.querySelectorAll('.area-option').forEach(el=>el.hidden=!!((group&&section.dataset.group!==group)||!norm(el.textContent).includes(q)));
      section.hidden=![...section.querySelectorAll('.area-option')].some(el=>!el.hidden);
    });
  }
  function renderAreas(){
    $('area-count').textContent=data.areas.length;
    $('group').options[0].textContent=`All ${data.areas.length} groups`;
    const benchmark=$('benchmark').value,b=benchmarks[benchmark],counts=new Map();
    if(b)for(const c of data.cards.filter(c=>inBenchmark(c,benchmark)))counts.set(c.area,(counts.get(c.area)||0)+1);
    for(const group of ['large','small'])$('group').querySelector(`[value="${group}"]`).textContent=`${group==='large'?'Large':'Small'} · ${b?b.quotas[group]:group==='large'?50:20} each`;
    $('areas').innerHTML=['large','small'].map(group=>{
      const areas=data.areas.filter(a=>a.group===group),target=b?b.quotas[group]:group==='large'?50:20;
      return `<section class="area-group" data-group="${group}" aria-label="${group==='large'?'Large':'Small'} selection groups"><h3>${group==='large'?'Large groups':'Small groups'} <span>${areas.length} × ${target}</span></h3>${areas.map(a=>`<label class="area-option"><input type="checkbox" value="${esc(a.area)}" ${state.areas.has(a.area)?'checked':''}><span>${a.position}. ${esc(a.label)}</span><span class="count" title="${b?`${counts.get(a.area)||0} selected for ${b.label}; `:''}${num(a.count)} available candidates; selection target ${a.target}">${num(b?(counts.get(a.area)||0):a.count)}</span></label>`).join('')}</section>`;
    }).join('');
    updateAreaVisibility();
  }
  updateStats();renderAreas();
  $('reason').innerHTML+=Object.entries(data.criteria||{}).map(([k,v])=>`<option value="${esc(k)}">${esc(v.label||v)}</option>`).join('');
  $('method-copy').innerHTML=(data.meta.methodology||[]).map(p=>`<p>${esc(p)}</p>`).join('');
  function updateCoverage(){
    $('coverage-table').innerHTML=`<table><thead><tr><th>Category</th><th>Target</th><th>Available candidates</th><th>Detailed cards</th></tr></thead><tbody>${['large','small'].map(group=>`<tr class="coverage-group"><th colspan="4" scope="rowgroup">${data.areas.filter(a=>a.group===group).length} ${group==='large'?'large groups · 50 each':'small groups · 20 each'}</th></tr>${data.areas.filter(a=>a.group===group).map(a=>`<tr><th scope="row"><button class="category-link" data-area="${esc(a.area)}">${a.position}. ${esc(a.label)}</button></th><td>${a.target}</td><td>${num(a.count)}</td><td>${num(a.reviewed||0)}</td></tr>`).join('')}`).join('')}</tbody><tfoot><tr><th scope="row">Total · ${data.areas.length} named categories</th><td>${num(data.areas.reduce((n,a)=>n+a.target,0))}</td><td>${num(data.meta.taxonomy?.candidate_count??data.cards.length)}</td><td>${num(data.cards.filter(c=>!c.scope_exclusion&&c.evidence==='reviewed').length)}</td></tr>${data.meta.taxonomy?.reserved_target?`<tr><th scope="row">Reserved small category · to be chosen</th><td>${data.meta.taxonomy.reserved_target}</td><td>—</td><td>—</td></tr>`:""}<tr><th scope="row">Preliminarily removed · archived</th><td>0</td><td>${num(data.meta.taxonomy?.preliminary_removal_count||0)}</td><td>—</td></tr><tr><th scope="row">Outside subject scope · archived</th><td>0</td><td>${num(data.meta.taxonomy?.subject_exclusion_count??data.meta.taxonomy?.scope_excluded_count??0)}</td><td>—</td></tr></tfoot></table>`;
  }
  updateCoverage();
  $('coverage-table').addEventListener('click',e=>{const b=e.target.closest('[data-area]');if(!b)return;clear();state.areas.add(b.dataset.area);renderAreas();filter(true);});
  $('area-search').addEventListener('input',updateAreaVisibility);
  $('active-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.area){state.areas.delete(b.dataset.area);document.querySelectorAll('#areas input').forEach(el=>{if(el.value===b.dataset.area)el.checked=false;});}if(b.dataset.filter){const control=$(b.dataset.filter);if(control.type==='checkbox')control.checked=false;else control.value='';}if(b.dataset.filter==='benchmark')renderAreas();updateAreaVisibility();filter();});
  $('benchmark').addEventListener('change',()=>{if(benchmarks[$('benchmark').value])$('scope').value='';renderAreas();filter();});
  $('areas').addEventListener('change',event=>{const e=event.target;if(!e.matches('input[type=checkbox]'))return;e.checked?state.areas.add(e.value):state.areas.delete(e.value);filter();});
  let debounce;$('search').addEventListener('input',()=>{clearTimeout(debounce);debounce=setTimeout(()=>filter(),160);});
  for(const id of ['sort','view','new-only','saved-only','textbook-only','evidence','status','reason','year','group','scope'])$(id).addEventListener('change',()=>{updateAreaVisibility();filter();});
  $('clear').onclick=clear;$('empty-reset').onclick=clear;$('more').onclick=loadMore;
  $('random').onclick=()=>{if(!state.matches.length)return;const c=state.matches[Math.floor(Math.random()*state.matches.length)];history.replaceState(null,'','#'+encodeURIComponent(c.id));go(c.id);};
  $('filters-toggle').onclick=()=>{const opened=$('filters').classList.toggle('visible');$('filters-toggle').setAttribute('aria-expanded',String(opened));};
  $('collapse').onclick=()=>document.querySelectorAll('.card-details[open]').forEach(d=>d.open=false);
  $('top').onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
  $('cards').addEventListener('click',async e=>{const button=e.target.closest('[data-action]');if(!button)return;const card=button.closest('.problem-card'),c=cardsById.get(card.dataset.id),act=button.dataset.action;
    if(act==='save'){saved.has(c.id)?saved.delete(c.id):saved.add(c.id);const ok=storage.set('tcs-atlas-saved',[...saved]);button.setAttribute('aria-pressed',String(saved.has(c.id)));button.textContent=saved.has(c.id)?'Saved':'Save +';button.setAttribute('aria-label',saved.has(c.id)?'Unsave problem':'Save problem');if(!ok)toast('Your browser could not save this change permanently.');if($('saved-only').checked)filter();}
    if(act==='permalink'){e.preventDefault();history.replaceState(null,'','#'+encodeURIComponent(c.id));toast('The address bar now contains a direct link to this card.');}
    if(act==='note'){card.querySelector('details').open=true;card.querySelector('textarea').focus();}
    if(act==='copy'){const text=statementText(c);try{await navigator.clipboard.writeText(text);toast('Statement and references copied.');}catch{const a=document.createElement('textarea');a.value=text;document.body.appendChild(a);a.select();const ok=document.execCommand('copy');a.remove();toast(ok?'Statement and references copied.':'Copying is unavailable. Use Export selection instead.');}}
  });
  $('cards').addEventListener('input',e=>{
    if(!e.target.matches('[data-note]'))return;
    const id=e.target.dataset.note;
    if(e.target.value)notes[id]=e.target.value;else delete notes[id];
    const ok=storage.set('tcs-atlas-notes',notes),status=$(`note-status-${id}`);
    if(status)status.textContent=ok?'Saved in this browser. Included in Export selection.':'This browser could not save your note. Keep it open or export your selection.';
  });
  $('cards').addEventListener('toggle',e=>{if(e.target.matches('.card-details')){if(e.target.open)math(e.target);$('collapse').hidden=!document.querySelector('.card-details[open]');}},true);
  $('export').onclick=()=>{const benchmark=$('benchmark').value,b=benchmarks[benchmark];const blob=new Blob([JSON.stringify({exported:new Date().toISOString(),meta:data.meta,areas:data.areas,...(b?{subbenchmark:benchmarkSummary(benchmark)}:{}),cards:state.matches.map(c=>({...c,area_label:areaLabel(c.area),...(c.original_area?{original_area_label:areaLabel(c.original_area)}:{}),...(c.scope_exclusion?{scope_exclusion:{...c.scope_exclusion,...(c.scope_exclusion.previous_area?{previous_area_label:areaLabel(c.scope_exclusion.previous_area)}:{})}}:{}),personal_note:notes[c.id]||'',saved:saved.has(c.id)}))},null,2)],{type:'application/json;charset=utf-8'});const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=b?`tcs-atlas-${benchmark}.json`:'tcs-atlas-selection.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){e.preventDefault();$('search').focus();}if(e.key==='Escape')$('search').blur();});
  const revealSection=id=>{const el=$(id);if(el?.matches('details.methodology'))el.open=true;};
  document.querySelectorAll('header .about-link').forEach(link=>link.addEventListener('click',()=>revealSection(link.hash.slice(1))));
  window.addEventListener('hashchange',()=>{const id=decodeURIComponent(location.hash.slice(1));if(cardsById.has(id))go(id);else revealSection(id);});
  // Load further cards only on request. Jumping to the footer or restoring a
  // reading position must not start an automatic chain of additional batches.
  const params=new URLSearchParams(location.search),requestedDetail=params.get('detail');if(['reviewed','source','index','drafts'].includes(requestedDetail))$('evidence').value=requestedDetail;
  if(benchmarks[params.get('benchmark')]){$('benchmark').value=params.get('benchmark');renderAreas();}
  if(['small','large'].includes(params.get('group'))){$('group').value=params.get('group');updateAreaVisibility();}
  if(params.get('collection')==='textbooks'){$('textbook-only').checked=true;$('advanced-filters').open=true;}
  $('view').value=params.get('view')==='full'||(requestedDetail==='reviewed'&&params.get('view')!=='compact')?'full':'compact';
  filter();const hash=decodeURIComponent(location.hash.slice(1));if(cardsById.has(hash))go(hash);else revealSection(hash);
  let currentVersion=data.meta.version||'',polling=false;
  const live=document.createElement('div');live.id='live-status';live.setAttribute('role','status');live.title='The catalogue updates automatically';live.innerHTML='<span>Live</span><button hidden>View update ↗</button>';document.querySelector('header nav').appendChild(live);
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
    if(!changes.length&&!areasChanged&&!removed.size){data.meta=update.meta;$('method-copy').innerHTML=(data.meta.methodology||[]).map(p=>`<p>${esc(p)}</p>`).join('');return;}
    const shown=state.shown,scrollY=window.scrollY,toolbarBottom=document.querySelector('.toolbar').getBoundingClientRect().bottom,visible=[...document.querySelectorAll('.problem-card')].find(el=>el.getBoundingClientRect().bottom>toolbarBottom&&el.getBoundingClientRect().top<innerHeight);
    const anchor=visible?{id:visible.id,top:visible.getBoundingClientRect().top}:null;
    const open=[...document.querySelectorAll('.card-details[open]')].map(el=>el.closest('.problem-card').id);
    const focused=document.activeElement,edit=focused.matches?.('[data-note]')?{id:focused.id,start:focused.selectionStart,end:focused.selectionEnd}:null;
    if(removed.size){data.cards=data.cards.filter(c=>!removed.has(c.id));for(const id of removed){cardsById.delete(id);searchIndex.delete(id);}}
    const positions=new Map(data.cards.map((c,i)=>[c.id,i]));
    for(const c of changes){if(positions.has(c.id))data.cards[positions.get(c.id)]=c;else data.cards.push(c);cardsById.set(c.id,c);}
    data.meta=update.meta;data.areas=update.areas;areasByName=new Map(data.areas.map(a=>[a.area,a]));
    // A metadata-only rename changes search terms even when every card is unchanged.
    for(const c of areasChanged?data.cards:changes)searchIndex.set(c.id,searchable(c));
    $('method-copy').innerHTML=(data.meta.methodology||[]).map(p=>`<p>${esc(p)}</p>`).join('');
    for(const a of state.areas)if(!areasByName.has(a))state.areas.delete(a);
    updateStats();renderAreas();updateCoverage();
    $('cards').classList.add('publishing');
    // Publication size must not determine the number of DOM cards. Inserting
    // thousands of changed cards here used to freeze the page on bulk updates.
    filter();while(state.shown<Math.min(state.matches.length,shown))loadMore();
    // A direct-linked or newly re-ranked card may lie outside that prefix.
    // Retain only the reading/editing cards, rather than rendering the entire
    // result set up to their new positions.
    const retained=new Set([anchor?.id,...open,edit?.id.replace(/^note-/, '')].filter(Boolean));
    for(const id of retained){
      if(document.getElementById(id)||!cardsById.has(id))continue;
      if($('benchmark').value==='top100'&&!state.matches.some(c=>c.id===id))continue;
      const wrap=document.createElement('div');wrap.innerHTML=renderCard(cardsById.get(id));
      const el=wrap.firstChild;$('cards').appendChild(el);math(el);
    }
    for(const id of open){const el=document.getElementById(id)?.querySelector('details');if(el){el.open=true;math(el);}}
    // Seed off-screen size estimates with the measured content height. Newly
    // inserted long cards otherwise fall back to 570px after virtualization
    // resumes, moving the reading anchor again after the initial restoration.
    const measureCards=()=>{
      const heights=[...$('cards').children].map(el=>{const style=getComputedStyle(el),padding=parseFloat(style.paddingTop)+parseFloat(style.paddingBottom),border=parseFloat(style.borderTopWidth)+parseFloat(style.borderBottomWidth);return [el,Math.max(0,el.getBoundingClientRect().height-padding-border)];});
      for(const [el,height] of heights)el.style.containIntrinsicBlockSize=`auto ${height}px`;
    };
    measureCards();
    if(document.fonts){await document.fonts.ready;measureCards();}
    if(edit){const el=document.getElementById(edit.id);if(el){el.focus({preventScroll:true});el.setSelectionRange(edit.start,edit.end);}}
    live.querySelector('span').textContent='Updated';live.title=removed.size?`${num(removed.size)} cards removed; ${num(changes.length)} added or updated`:changes.length?`${num(changes.length)} cards added or updated`:'Categories updated';
    const newest=[...changes].sort((a,b)=>(b.updated_at||b.published_at||'').localeCompare(a.updated_at||a.published_at||'')||importanceOrder(a,b))[0],button=live.querySelector('button');button.hidden=!newest;if(newest)button.onclick=()=>{history.replaceState(null,'','#'+newest.id);go(newest.id);};
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
      if(!update){const fullResponse=await fetch('updates.json',{cache:'no-store'});if(!fullResponse.ok)throw new Error('Unavailable');update=await fullResponse.json();}
      await applyPublication(update);
    }if(live.dataset.disconnected){live.querySelector('span').textContent='Live';live.title='The catalogue updates automatically';delete live.dataset.disconnected;}}
    catch{live.querySelector('span').textContent='Offline';live.title='Live updates unavailable; keeping the current catalogue';live.dataset.disconnected='true';}
    finally{polling=false;}
  }
  if(['http:','https:'].includes(location.protocol)){setInterval(checkUpdates,4000);checkUpdates();document.addEventListener('visibilitychange',()=>{if(!document.hidden)checkUpdates();});}
  else {live.querySelector('span').textContent='Offline';live.title='Downloaded catalogue snapshot';}
  window.ATLAS_DEBUG={filter,go,state,data,checkUpdates,applyPublication};
})();
