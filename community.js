/* Account-free comments and suggestions, plus legacy GitHub contributions. */
(() => {
  'use strict';
  const repository='vaclavrozhon/atlas';
  const github=`https://github.com/${repository}`;
  const api=`https://api.github.com/repos/${repository}/issues`;
  const notesAPI='https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/notes';
  const proposalsAPI='https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/proposals';
  const proposalIdPattern=/^P-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
  const fields=['title','category','statement','sources','author'];
  const data=window.TCS_ATLAS;
  const $=id=>document.getElementById(id);
  const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
  const write=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch{return false;}};
  const draftKey='tcs-atlas-contribution-drafts';
  const cacheKey='tcs-atlas-community-cache-v1';
  const notesCacheKey='tcs-atlas-public-notes-cache-v1';
  const ownershipKey='tcs-atlas-note-ownership-v1';
  const proposalsCacheKey='tcs-atlas-proposals-cache-v1';
  let directProposals=read(proposalsCacheKey,[]),proposalsRevision=0;
  if(!Array.isArray(directProposals))directProposals=[];
  directProposals=directProposals.filter(validProposal);
  const savedCache=read(cacheKey,{});
  let anonymousNotes=read(notesCacheKey,[]),ownership=read(ownershipKey,{}),githubContributions=[];
  if(!Array.isArray(anonymousNotes))anonymousNotes=[];
  anonymousNotes=anonymousNotes.filter(validNote);
  if(!ownership||typeof ownership!=='object'||Array.isArray(ownership))ownership={};
  let drafts=read(draftKey,{});
  if(!drafts||typeof drafts!=='object'||Array.isArray(drafts))drafts={};
  let contributions=[],loadedAt=0,loading=false,lastAttempt=0,current=null,posting=false,notesRevision=0;
  let displayed=20;
  const openThreads=new Set();
  const sectionNames={statement:'Problem statement',definitions:'Definitions and model',answer:'What would settle it?',why:'Why it matters',sources:'Sources'};

  function sections(body){
    const result={};
    const parts=body.split(/^### (Problem statement|Definitions and model|What would settle it\?|Why it matters|Sources)\s*$/m);
    for(let i=1;i<parts.length;i+=2){
      const key=Object.keys(sectionNames).find(key=>sectionNames[key]===parts[i]);
      if(key)result[key]=(result[key]?result[key]+'\n\n':'')+parts[i+1].trim();
    }
    return result;
  }
  function parseIssue(issue){
    if(!issue||issue.pull_request||issue.state!=='open'||!Number.isSafeInteger(issue.number)||issue.number<=0||typeof issue.body!=='string')return null;
    const body=issue.body.replace(/\r\n/g,'\n');
    const marker=body.match(/^<!-- atlas-(note|problem):v1 ([A-Za-z0-9-]+) -->\n/);
    if(!marker)return null;
    const base={number:issue.number,url:`${github}/issues/${issue.number}`,author:String(issue.user?.login||'Unknown contributor'),created_at:issue.created_at,updated_at:issue.updated_at,original_body:issue.body};
    const text=body.slice(marker[0].length).trim();
    if(marker[1]==='note')return /^(TCS-\d{4,}|GH-\d+)$/.test(marker[2])&&text?{...base,kind:'note',problem_id:marker[2],text}:null;
    const values=sections(text);
    const title=String(issue.title||'').replace(/^\[Problem\]\s*/, '').trim();
    return title&&values.statement?{...base,kind:'problem',id:`GH-${issue.number}`,title,category:marker[2],...values}:null;
  }
  function adopt(issues,time){
    githubContributions=issues.map(parseIssue).filter(Boolean);
    combine();
    loadedAt=time;
  }
  function validNote(note){return note&&typeof note.id==='string'&&/^[0-9a-f-]{36}$/i.test(note.id)&&(/^(TCS-\d{4,}|GH-\d+)$/.test(note.problem_id)||proposalIdPattern.test(note.problem_id))&&typeof note.text==='string'&&typeof note.author==='string';}
  function validProposal(item){return item&&proposalIdPattern.test(item.id)&&fields.every(key=>typeof item[key]==='string')&&item.title.trim()&&item.statement.trim();}
  function combine(){contributions=[...directProposals.map(item=>({...item,kind:'problem',source:'direct'})),...githubContributions,...anonymousNotes.map(note=>({...note,kind:'note',source:'direct'}))];}
  combine();
  if(Array.isArray(savedCache.issues)&&Number.isFinite(savedCache.loadedAt))adopt(savedCache.issues,savedCache.loadedAt);
  const categoryLabel=id=>data.areas.find(area=>area.id===id)?.label||'Category awaiting review';
  const problem=id=>data.cards.find(card=>card.id===id)||contributions.find(item=>item.kind==='problem'&&item.id===id);
  const date=value=>{const parsed=new Date(value);return Number.isNaN(parsed.valueOf())?'':parsed.toLocaleDateString('en',{year:'numeric',month:'short',day:'numeric'});};
  const byAuthor=item=>item.source==='direct'?`${esc(item.author)} · ${esc(date(item.created_at))} <span title="No account is required; names are not verified.">· unverified</span>`:`<a href="${esc(item.url)}" target="_blank" rel="noopener noreferrer">${esc(item.author)} · ${esc(date(item.created_at))} ↗</a>`;

  function reviewFor(item){
    const source=item.source==='direct'?'direct':'github',id=source==='direct'?(item.kind==='problem'?item.id.slice(2):item.id):String(item.number);
    const original=source==='direct'?(item.kind==='problem'?proposalText(item):item.text):item.original_body;
    for(const card of data.cards){
      if(['resolved','excluded'].includes(card.status))continue;
      const review=card.community_reviews?.find(review=>review.source===source&&review.id===id&&review.original_problem_id===(item.kind==='problem'?item.id:item.problem_id)&&review.original_text===original);
      if(review)return {card,review};
    }
    return null;
  }
  function reviewHTML(item){
    const result=reviewFor(item);if(!result)return '';
    const {card,review}=result;
    return `<p class="community-review"><strong>[${esc(review.status)}]</strong> ${esc(review.response)} <span class="small">Editorial review · ${esc(date(review.reviewed_on))} · <a href="#${esc(card.id)}">${esc(card.id)}</a></span></p>`;
  }
  function notesContent(id){
    const notes=contributions.filter(item=>item.kind==='note'&&(item.problem_id===id||reviewFor(item)?.card.id===id));
    if(!notes.length)return '';
    return `<details class="community-thread" data-thread="${esc(id)}" ${openThreads.has(id)?'open':''}><summary>Comments (${notes.length})</summary>${notes.map(item=>`<article class="public-note"><p class="public-note-author">${byAuthor(item)}${item.problem_id!==id?` · Originally on ${esc(item.problem_id)}`:''}</p><p class="public-note-text">${esc(item.text)}</p>${reviewHTML(item)}${item.source==='direct'?(ownership[item.id]?`<button type="button" class="text-button" data-delete-note="${esc(item.id)}">Delete my comment</button>`:''):`<a class="small" href="${esc(item.url)}" target="_blank" rel="noopener noreferrer">Original comment on GitHub ↗</a>`}</article>`).join('')}</details>`;
  }
  function notesHTML(id){return `<div class="public-notes" data-public-notes="${esc(id)}">${notesContent(id)}</div>`;}
  function render(){
    const problems=contributions.filter(item=>item.kind==='problem');
    $('community-count').textContent=problems.length?`(${problems.length})`:'';
    $('community-problem-count').textContent=`(${problems.length})`;
    $('community-problems').innerHTML=problems.length?problems.slice(0,displayed).map(item=>`<article class="community-problem" id="${item.id}"><div class="card-meta"><span>${item.source==='direct'?'Reader suggestion':item.id}</span><span class="proposal-status">${reviewFor(item)?'Reviewed community proposal':'Awaiting review'}</span><span>${esc(categoryLabel(item.category))}</span></div><h2>${esc(item.title)}</h2>${window.ATLAS_VOTES?.html(item.id)||''}<p class="community-author">${byAuthor(item)}</p><p class="community-statement">${esc(item.statement)}</p>${Object.keys(sectionNames).filter(key=>key!=='statement'&&item[key]).map(key=>`<section><h3>${esc(sectionNames[key])}</h3><p class="community-text">${esc(item[key])}</p></section>`).join('')}${reviewHTML(item)}${notesHTML(item.id)}<div class="community-actions"><button type="button" data-public-note="${item.id}">Add a comment</button><a href="#${item.id}">Link to suggestion</a>${item.source==='direct'?(ownership[item.id]?`<button type="button" class="text-button" data-delete-proposal="${item.id}">Delete my suggestion</button>`:''):`<a href="${item.url}" target="_blank" rel="noopener noreferrer">Original suggestion on GitHub ↗</a>`}</div></article>`).join('')+(problems.length>displayed?'<button type="button" id="more-community">Load more community problems</button>':''):`<p class="community-empty">${loadedAt?'Have a problem in mind? Suggest it here to start the discussion.':'Shared problems will appear here after contributions load.'}</p>`;
    for(const slot of document.querySelectorAll('[data-public-notes]'))slot.innerHTML=notesContent(slot.dataset.publicNotes);
    revealHash();
  }
  function status(text){$('community-status').textContent=text;}
  async function refresh(force=false){
    if(loading)return;
    if(!force&&Date.now()-lastAttempt<60000)return;
    if(!force&&loadedAt&&Date.now()-loadedAt<300000){status(`Shared contributions checked ${new Date(loadedAt).toLocaleString('en')}.`);return;}
    if(location.protocol==='file:'){status('Offline snapshot. Public contributions saved in this browser are shown; use the online atlas to refresh them.');return;}
    loading=true;lastAttempt=Date.now();$('refresh-community').disabled=true;status('Loading shared contributions…');
    const results=await Promise.allSettled([(async()=>{
      const issues=[];
      for(let page=1;;page++){
        const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),15000);
        try{
          const response=await fetch(`${api}?state=open&sort=created&direction=desc&per_page=100&page=${page}`,{headers:{Accept:'application/vnd.github+json'},signal:controller.signal});
          if(!response.ok)throw new Error(response.status===403||response.status===429?'GitHub’s request limit was reached.':'GitHub is currently unavailable.');
          const batch=await response.json();if(!Array.isArray(batch))throw new Error('GitHub returned an unexpected response.');
          issues.push(...batch);
          if(!/rel="next"/.test(response.headers.get('link')||''))break;
        }finally{clearTimeout(timeout);}
      }
      const kept=issues.filter(issue=>parseIssue(issue));
      adopt(kept,Date.now());write(cacheKey,{loadedAt,issues:kept});render();
    })(),(async()=>{
      const notes=[],revision=notesRevision;
      let before=null;
      do{
        const result=await notesRequest(before?`?before=${before}`:'');
        if(!Array.isArray(result.notes)||!result.notes.every(validNote)||!(result.next===null||Number.isSafeInteger(result.next)&&result.next>0&&(!before||result.next<before)))throw new Error('The notes service returned an unexpected response.');
        notes.push(...result.notes);before=result.next;
      }while(before);
      // A refresh started before a submission must not hide the newly posted note.
      if(revision===notesRevision){anonymousNotes=notes;write(notesCacheKey,notes);combine();render();}
    })(),(async()=>{
      const proposals=[],revision=proposalsRevision;
      let before=null;
      do{
        const result=await notesRequest(before?`?before=${before}`:'',{},proposalsAPI);
        if(!Array.isArray(result.proposals)||!result.proposals.every(validProposal)||!(result.next===null||Number.isSafeInteger(result.next)&&result.next>0&&(!before||result.next<before)))throw new Error('Could not load suggestions. Please try again.');
        proposals.push(...result.proposals);before=result.next;
      }while(before);
      if(revision===proposalsRevision){directProposals=proposals;write(proposalsCacheKey,proposals);combine();render();}
    })()]);
    const failures=results.map((result,index)=>result.status==='rejected'?['Earlier contributions','Comments','Suggestions'][index]+': '+(result.reason.name==='AbortError'?'The request timed out.':result.reason.message):'').filter(Boolean);
    status(failures.length?failures.join(' ')+' Previously saved contributions are still shown. Try refreshing later.':`Shared contributions checked ${new Date().toLocaleString('en')}.`);
    loading=false;$('refresh-community').disabled=false;
  }
  async function notesRequest(path='',options={},endpoint=notesAPI){
    const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await fetch(endpoint+path,{...options,credentials:'omit',signal:controller.signal,headers:{'Content-Type':'application/json',...options.headers}});
      let result;try{result=await response.json();}catch{throw new Error('Contributions are temporarily unavailable.');}
      if(!response.ok)throw Object.assign(new Error(result.error||'Contributions are temporarily unavailable.'),{status:response.status});
      return result;
    }finally{clearTimeout(timeout);}
  }
  function values(){
    return current.kind==='note'?{text:$('public-note-text').value,author:$('public-note-author').value}:Object.fromEntries(fields.map(key=>[key,$(`proposal-${key}`).value]));
  }
  function saveDraft(){
    if(!current)return;
    drafts[current.key]={...drafts[current.key],...values()};
    if(current.kind==='problem')for(const key of ['definitions','answer','why'])delete drafts[current.key][key];
    $('contribution-draft-status').textContent=write(draftKey,drafts)?'Draft saved in this browser. Nothing has been published yet.':'This browser could not save your draft. Keep the form open or copy your text.';
  }
  function categoryOptions(selected){
    $('proposal-category').innerHTML='<option value="">Not sure / let us choose</option>'+data.areas.map(area=>`<option value="${esc(area.id)}">${esc(area.label)}</option>`).join('');
    $('proposal-category').value=selected||'';
  }
  function open(kind,id){
    if(posting)return;
    const target=kind==='note'?problem(id):null;
    if(kind==='note'&&!target)return;
    current={kind,id,key:kind==='note'?`note:${id}`:'problem'};
    const draft={...(drafts[current.key]||{})};
    // Fold previously saved optional fields into the statement so the shorter
    // form does not lose any unfinished contribution. Saving replaces the old shape.
    if(kind==='problem'){
      const extra=['definitions','answer','why'].filter(key=>draft[key]).map(key=>`${sectionNames[key]}:\n${draft[key]}`);
      draft.statement=[draft.statement,...extra].filter(Boolean).join('\n\n');
    }
    $('contribution-title').textContent=kind==='note'?'Add a comment':'Suggest a problem';
    $('contribution-help').textContent=kind==='note'?'Share a correction, source, question or idea — no account needed. Your comment will be public. Your name is optional, and you can delete your comment from this browser.':'A rough formulation is welcome — no account needed. Your suggestion appears publicly right away for discussion. We review it before adding it to the catalogue. You can delete it from this browser.';
    $('submit-contribution').textContent=kind==='note'?'Post comment':'Publish suggestion';
    $('problem-fields').hidden=kind!=='problem';$('public-note-fields').hidden=kind!=='note';
    $('contribution-target').hidden=!target;$('contribution-target').textContent=target?`${id} · ${target.title}`:'';
    for(const key of fields){const el=$(`proposal-${key}`);el.disabled=kind!=='problem';el.required=kind==='problem'&&['title','statement'].includes(key);if(key!=='category')el.value=String(draft[key]||'');}
    categoryOptions(draft.category);
    $('public-note-text').disabled=kind!=='note';$('public-note-text').required=kind==='note';$('public-note-text').value=String(draft.text||'');
    $('public-note-author').disabled=kind!=='note';$('public-note-author').value=String(draft.author||'');
    $('public-note-website').disabled=false;$('public-note-website').value='';
    $('contribution-result').textContent='';
    $('contribution-draft-status').textContent=drafts[current.key]?'Your saved draft has been restored.':kind==='note'?'Nothing is published until you click “Post comment”.':'Nothing is published until you click “Publish suggestion”.';
    $('contribution-dialog').showModal();(kind==='note'?$('public-note-text'):$('proposal-title')).focus();
  }
  // Stable text used to match an editorial response to this exact suggestion.
  function proposalText(item){return JSON.stringify(Object.fromEntries(fields.map(key=>[key,item[key]])));}
  $('contribution-form').addEventListener('input',()=>{saveDraft();$('contribution-result').textContent='';});
  async function postContribution(){
    if(posting)return;
    saveDraft();
    const key=current.key,problemId=current.id,draft=drafts[key],isNote=current.kind==='note';
    const sentFields=isNote?['text','author']:fields;
    // Persist the exact request before sending so a lost response can be retried.
    if(!draft.pending){
      const token=[...crypto.getRandomValues(new Uint8Array(32))].map(byte=>byte.toString(16).padStart(2,'0')).join('');
      draft.pending={id:crypto.randomUUID(),edit_token:token,...(isNote?{problem_id:problemId}:{}),...Object.fromEntries(sentFields.map(field=>[field,draft[field]]))};
    }
    const pending=draft.pending,ownedId=isNote?pending.id:'P-'+pending.id;
    ownership[ownedId]=pending.edit_token;
    if(!write(draftKey,drafts)||!write(ownershipKey,ownership)){
      $('contribution-result').textContent='Enable browser storage before posting so you can retry safely and delete your contribution. Your text is still in the form.';return;
    }
    posting=true;
    const controls=[...$('contribution-form').querySelectorAll('button,input,textarea,select')].filter(el=>!el.disabled);
    controls.forEach(el=>el.disabled=true);$('submit-contribution').textContent='Posting…';
    $('contribution-result').textContent='';
    try{
      const result=await notesRequest('',{method:'POST',body:JSON.stringify({...pending,website:$('public-note-website').value})},isNote?notesAPI:proposalsAPI);
      const saved=isNote?result.note:result.proposal;
      if(!(isNote?validNote(saved):validProposal(saved))||saved.id!==ownedId)throw new Error('Could not confirm your contribution. Please retry.');
      if(isNote){
        anonymousNotes=[saved,...anonymousNotes.filter(note=>note.id!==saved.id)];notesRevision++;
        write(notesCacheKey,anonymousNotes);openThreads.add(problemId);
      }else{
        directProposals=[saved,...directProposals.filter(item=>item.id!==saved.id)];proposalsRevision++;
        write(proposalsCacheKey,directProposals);
      }
      combine();render();
      if(sentFields.every(field=>draft[field]===pending[field])){
        delete drafts[key];write(draftKey,drafts);$('contribution-dialog').close();
        if(!isNote){$('community').open=true;location.hash=saved.id;document.getElementById(saved.id)?.scrollIntoView({block:'start'});}
        announce(isNote?'Your comment is now public. Thank you!':'Thank you! Your suggestion is now public and awaiting review.');
      }else{
        delete draft.pending;write(draftKey,drafts);
        $('contribution-result').textContent='Your earlier submission was published. Your later changes are still here as a new draft.';
        $('contribution-draft-status').textContent='Draft saved in this browser.';
      }
    }catch(error){
      const rejected=error.status>=400&&error.status<500;
      if(rejected){delete draft.pending;write(draftKey,drafts);}
      $('contribution-result').textContent=(error.name==='AbortError'?'The request timed out.':error.message)+(rejected?' Your draft is kept.':' Your draft is kept. Retry to check and complete the same submission.');
    }finally{
      posting=false;controls.forEach(el=>el.disabled=false);$('submit-contribution').textContent=isNote?'Post comment':'Publish suggestion';
    }
  }
  function announce(message){
    $('contribution-feedback').textContent=message;
  }
  $('contribution-form').addEventListener('submit',async event=>{
    event.preventDefault();
    if(posting)return;
    const required=current.kind==='note'?[$('public-note-text')]:[$('proposal-title'),$('proposal-statement')];
    for(const field of required){field.setCustomValidity(field.value.trim()?'':'Please enter some text.');if(!field.reportValidity())return;}
    if(!$('contribution-form').reportValidity())return;
    await postContribution();
  });
  for(const id of ['public-note-text','proposal-title','proposal-statement'])$(id).addEventListener('input',event=>event.target.setCustomValidity(''));
  $('close-contribution').onclick=()=>$('contribution-dialog').close();
  $('contribution-dialog').addEventListener('cancel',event=>{if(posting)event.preventDefault();});
  $('discard-contribution').onclick=()=>{
    if(!confirm('Discard this saved draft?'))return;
    const previous=drafts[current.key];delete drafts[current.key];
    if(!write(draftKey,drafts)){drafts[current.key]=previous;$('contribution-draft-status').textContent='This browser could not remove the saved draft. Please try again.';return;}
    $('contribution-dialog').close();
  };
  $('new-problem').onclick=()=>open('problem');
  $('refresh-community').onclick=()=>refresh(true);
  document.addEventListener('click',async event=>{
    const note=event.target.closest('[data-public-note]');if(note)open('note',note.dataset.publicNote);
    const remove=event.target.closest('[data-delete-note]');
    if(remove&&confirm('Delete this public comment?')){
      const id=remove.dataset.deleteNote;remove.disabled=true;
      try{
        await notesRequest('/'+id,{method:'DELETE',headers:{Authorization:'Bearer '+ownership[id]}});
        anonymousNotes=anonymousNotes.filter(note=>note.id!==id);notesRevision++;delete ownership[id];
        write(ownershipKey,ownership);write(notesCacheKey,anonymousNotes);combine();render();
      }catch(error){remove.disabled=false;alert('Could not delete the note. '+error.message);}
    }
    const removeProposal=event.target.closest('[data-delete-proposal]');
    if(removeProposal&&confirm('Delete this public suggestion?')){
      const id=removeProposal.dataset.deleteProposal;removeProposal.disabled=true;
      try{
        await notesRequest('/'+id,{method:'DELETE',headers:{Authorization:'Bearer '+ownership[id]}},proposalsAPI);
        directProposals=directProposals.filter(item=>item.id!==id);proposalsRevision++;delete ownership[id];
        write(ownershipKey,ownership);write(proposalsCacheKey,directProposals);combine();render();announce('Your suggestion was deleted.');
      }catch(error){removeProposal.disabled=false;alert('Could not delete the suggestion. '+error.message);}
    }
    if(event.target.closest('[data-new-problem]'))open('problem');
    if(event.target.closest('#more-community')){displayed+=20;render();}
  });
  document.addEventListener('toggle',event=>{
    const id=event.target.dataset?.thread;if(!id)return;
    event.target.open?openThreads.add(id):openThreads.delete(id);
  },true);
  function revealHash(){
    const id=decodeURIComponent(location.hash.slice(1));
    if(id==='community')$('community').open=true;
    if(/^GH-\d+$/.test(id)||proposalIdPattern.test(id)){
      const problems=contributions.filter(item=>item.kind==='problem'),position=problems.findIndex(item=>item.id===id);
      if(position<0)return;
      $('community').open=true;
      if(position>=displayed){displayed=position+1;render();return;}
      document.getElementById(id)?.scrollIntoView({block:'start'});
    }
  }
  window.addEventListener('hashchange',revealHash);
  document.addEventListener('atlas:publication',render);
  window.addEventListener('focus',()=>refresh());
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
  document.addEventListener('atlas:votes',()=>window.ATLAS_VOTES?.render());
  window.ATLAS_COMMUNITY={notesHTML,refresh,parseIssue,proposalText,get contributions(){return contributions;},get loadedAt(){return loadedAt;}};
  render();refresh();
})();
