/* New public comments are isolated from archived feedback and private drafts. */
(() => {
  'use strict';
  const repository='vaclavrozhon/atlas';
  const github=`https://github.com/${repository}`;
  const notesAPI='https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/comments';
  const data=window.TCS_ATLAS;
  const $=id=>document.getElementById(id);
  const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
  const write=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch{return false;}};
  const draftKey='tcs-atlas-contribution-drafts';
  const notesCacheKey='tcs-atlas-public-comments-cache-v1';
  const ownershipKey='tcs-atlas-comment-ownership-v1';
  let anonymousNotes=read(notesCacheKey,[]),ownership=read(ownershipKey,{});
  if(!Array.isArray(anonymousNotes))anonymousNotes=[];
  anonymousNotes=anonymousNotes.filter(validNote);
  if(!ownership||typeof ownership!=='object'||Array.isArray(ownership))ownership={};
  let drafts=read(draftKey,{});
  if(!drafts||typeof drafts!=='object'||Array.isArray(drafts))drafts={};
  let contributions=[],loadedAt=0,loading=false,lastAttempt=0,current=null,posting=false,notesRevision=0;
  let notesStatus='Loading comments…';
  const commentsEnabled=()=>data.meta.public_comments===true;
  const openThreads=new Set();
  const fields=['title','category','statement','sources'];
  const sectionNames={statement:'Problem statement',definitions:'Definitions and model',answer:'What would settle it?',why:'Why it matters',sources:'Sources'};

  function validNote(note){return note&&typeof note.id==='string'&&/^[0-9a-f-]{36}$/i.test(note.id)&&/^(TCS-\d{4,}|GH-\d+)$/.test(note.problem_id)&&typeof note.text==='string'&&typeof note.author==='string';}
  function combine(){contributions=anonymousNotes.map(note=>({...note,kind:'note',source:'direct'}));}
  combine();
  const problem=id=>data.cards.find(card=>card.id===id);
  const date=value=>{const parsed=new Date(value);return Number.isNaN(parsed.valueOf())?'':parsed.toLocaleDateString('en',{year:'numeric',month:'short',day:'numeric'});};
  const byAuthor=item=>`${esc(item.author)} · ${esc(date(item.created_at))} <span title="No account is required; names are not verified.">· unverified</span>`;

  function notesContent(id){
    const notes=contributions.filter(item=>item.problem_id===id);
    return `<details class="community-thread" data-thread="${esc(id)}" ${openThreads.has(id)?'open':''}><summary>Comments (${notes.length})</summary>${notes.length?notes.map(item=>`<article class="public-note"><p class="public-note-author">${byAuthor(item)}</p><p class="public-note-text">${esc(item.text)}</p>${ownership[item.id]?`<button type="button" class="text-button" data-delete-note="${esc(item.id)}">Delete my comment</button>`:''}</article>`).join(''):'<p class="small muted">No public comments yet.</p>'}</details><div class="comment-actions"><button type="button" data-public-note="${esc(id)}">Add comment</button><button type="button" class="text-button" data-refresh-notes ${loading?'disabled':''}>Refresh comments</button></div>${notesStatus?`<p class="small muted comment-status" role="status">${esc(notesStatus)}</p>`:''}`;
  }
  function notesHTML(id){return commentsEnabled()?`<section class="public-notes" aria-label="Public comments" data-public-notes="${esc(id)}">${notesContent(id)}</section>`:'';}
  function render(){
    for(const slot of document.querySelectorAll('[data-public-notes]'))slot.innerHTML=commentsEnabled()?notesContent(slot.dataset.publicNotes):'';
  }
  async function refresh(force=false){
    if(!commentsEnabled()||loading)return;
    if(!force&&Date.now()-lastAttempt<60000)return;
    if(!force&&loadedAt&&Date.now()-loadedAt<300000)return;
    if(location.protocol==='file:'){notesStatus='Offline snapshot. Saved public comments are shown; use the online atlas to refresh them.';render();return;}
    loading=true;lastAttempt=Date.now();notesStatus='Loading comments…';render();
    try{
      const notes=[],revision=notesRevision;
      let before=null;
      do{
        const result=await notesRequest(before?`?before=${before}`:'');
        if(!Array.isArray(result.notes)||!result.notes.every(validNote)||!(result.next===null||Number.isSafeInteger(result.next)&&result.next>0&&(!before||result.next<before)))throw new Error('The comments service returned an unexpected response.');
        notes.push(...result.notes);before=result.next;
      }while(before);
      // A refresh started before a submission must not hide the newly posted comment.
      if(revision===notesRevision){anonymousNotes=notes;write(notesCacheKey,notes);combine();}
      loadedAt=Date.now();notesStatus='';
    }catch(error){
      notesStatus=(error.name==='AbortError'?'Loading comments timed out.':error.message)+' Saved comments are still shown. Try refreshing again.';
    }finally{loading=false;render();}
  }
  async function notesRequest(path='',options={}){
    const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await fetch(notesAPI+path,{...options,credentials:'omit',signal:controller.signal,headers:{'Content-Type':'application/json',...options.headers}});
      let result;try{result=await response.json();}catch{throw new Error('The comments service is currently unavailable.');}
      if(!response.ok)throw Object.assign(new Error(result.error||'The comments service is currently unavailable.'),{status:response.status});
      return result;
    }finally{clearTimeout(timeout);}
  }
  function values(){
    return current.kind==='note'?{text:$('public-note-text').value,author:$('public-note-author').value}:Object.fromEntries(fields.map(key=>[key,$(`proposal-${key}`).value]));
  }
  function saveDraft(){
    if(!current)return;
    drafts[current.key]=current.kind==='note'?{...drafts[current.key],...values()}:values();
    $('contribution-draft-status').textContent=write(draftKey,drafts)?'Draft saved in this browser. Nothing has been published yet.':'This browser could not save your draft. Keep the form open or copy your text.';
  }
  function categoryOptions(selected){
    $('proposal-category').innerHTML='<option value="">Choose a category…</option>'+data.areas.map(area=>`<option value="${esc(area.id)}">${esc(area.label)}</option>`).join('');
    $('proposal-category').value=selected||'';
  }
  function open(kind,id){
    if(posting||(kind==='note'&&!commentsEnabled()))return;
    const target=kind==='note'?problem(id):null;
    if(kind==='note'&&!target)return;
    current={kind,id,key:kind==='note'?`comment:${id}`:'problem'};
    const draft={...(drafts[current.key]||{})};
    // Fold previously saved optional fields into the statement so the shorter
    // form does not lose any unfinished contribution. Saving replaces the old shape.
    if(kind==='problem'){
      const extra=['definitions','answer','why'].filter(key=>draft[key]).map(key=>`${sectionNames[key]}:\n${draft[key]}`);
      draft.statement=[draft.statement,...extra].filter(Boolean).join('\n\n');
    }
    $('contribution-title').textContent=kind==='note'?'Add a public comment':'New problem';
    $('contribution-help').textContent=kind==='note'?'Post a public comment directly — no account needed. Your name is optional. You can delete your comment from this browser; moderators can remove unsuitable comments.':'This contribution will be public. Continue to GitHub to sign in and submit it. Your draft is saved in this browser and kept until you discard it.';
    $('submit-contribution').textContent=kind==='note'?'Post comment':'Continue on GitHub ↗';
    $('problem-fields').hidden=kind!=='problem';$('public-note-fields').hidden=kind!=='note';
    $('contribution-target').hidden=!target;$('contribution-target').textContent=target?`${id} · ${target.title}`:'';
    for(const key of fields){const el=$(`proposal-${key}`);el.disabled=kind!=='problem';el.required=kind==='problem'&&['title','category','statement'].includes(key);if(key!=='category')el.value=String(draft[key]||'');}
    categoryOptions(draft.category);
    $('public-note-text').disabled=kind!=='note';$('public-note-text').required=kind==='note';$('public-note-text').value=String(draft.text||'');
    $('public-note-author').disabled=kind!=='note';$('public-note-author').value=String(draft.author||'');
    $('public-note-website').disabled=kind!=='note';$('public-note-website').value='';
    $('contribution-result').textContent='';$('long-contribution').hidden=true;$('refresh-after-submission').hidden=true;
    $('contribution-draft-status').textContent=drafts[current.key]?'Your saved draft has been restored.':kind==='note'?'Nothing is published until you click “Post comment”.':'Nothing is published until you submit on GitHub.';
    $('contribution-dialog').showModal();(kind==='note'?$('public-note-text'):$('proposal-title')).focus();
  }
  function submission(){
    const v=values();
    return {title:`[Problem] ${v.title.trim()}`,body:`<!-- atlas-problem:v1 ${v.category} -->\n\n`+Object.keys(sectionNames).filter(key=>v[key]?.trim()).map(key=>`### ${sectionNames[key]}\n\n${v[key].trim()}`).join('\n\n')};
  }
  function issueURL(title,body){const url=new URL(github+'/issues/new');url.searchParams.set('title',title);if(body)url.searchParams.set('body',body);return url.href;}
  $('contribution-form').addEventListener('input',()=>{saveDraft();$('long-contribution').hidden=true;$('contribution-result').textContent='';});
  async function postNote(){
    if(posting)return;
    saveDraft();
    const key=current.key,problemId=current.id,draft=drafts[key];
    // Persist the exact request before sending. After a lost response, retry it
    // first even if the text has since changed, so a retry cannot create duplicates.
    if(!draft.pending){
      const token=[...crypto.getRandomValues(new Uint8Array(32))].map(byte=>byte.toString(16).padStart(2,'0')).join('');
      draft.pending={id:crypto.randomUUID(),edit_token:token,problem_id:problemId,text:draft.text,author:draft.author};
    }
    const pending=draft.pending;
    ownership[pending.id]=pending.edit_token;
    if(!write(draftKey,drafts)||!write(ownershipKey,ownership)){
      $('contribution-result').textContent='Enable browser storage before posting so you can retry safely and delete your comment. Your text is still in the form.';return;
    }
    posting=true;
    const controls=[...$('contribution-form').querySelectorAll('button,input,textarea,select')].filter(el=>!el.disabled);
    controls.forEach(el=>el.disabled=true);$('submit-contribution').textContent='Posting…';
    $('contribution-result').textContent='';
    try{
      const result=await notesRequest('',{method:'POST',body:JSON.stringify({...pending,website:$('public-note-website').value})});
      if(!validNote(result.note)||result.note.id!==pending.id)throw new Error('Could not confirm the saved comment. Please retry.');
      anonymousNotes=[result.note,...anonymousNotes.filter(note=>note.id!==result.note.id)];notesRevision++;notesStatus='';
      write(notesCacheKey,anonymousNotes);combine();openThreads.add(problemId);render();
      if(draft.text===pending.text&&draft.author===pending.author){
        delete drafts[key];write(draftKey,drafts);$('contribution-dialog').close();
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
      posting=false;controls.forEach(el=>el.disabled=false);$('submit-contribution').textContent='Post comment';
    }
  }
  $('contribution-form').addEventListener('submit',async event=>{
    event.preventDefault();
    if(posting)return;
    const required=current.kind==='note'?[$('public-note-text')]:[$('proposal-title'),$('proposal-statement')];
    for(const field of required){field.setCustomValidity(field.value.trim()?'':'Please enter some text.');if(!field.reportValidity())return;}
    if(!$('contribution-form').reportValidity())return;
    if(current.kind==='note'){await postNote();return;}
    saveDraft();const draft=submission(),url=issueURL(draft.title,draft.body);
    $('refresh-after-submission').hidden=true;
    if(url.length>7500){$('contribution-copy-text').value=draft.body;$('open-long-contribution').href=issueURL(draft.title);$('long-contribution').hidden=false;$('long-contribution').scrollIntoView({block:'nearest'});return;}
    window.open(url,'_blank','noopener,noreferrer');
    $('contribution-result').textContent='Finish by clicking “Submit new issue” on GitHub. Your draft is kept until you discard it.';
  });
  for(const id of ['public-note-text','proposal-title','proposal-statement'])$(id).addEventListener('input',event=>event.target.setCustomValidity(''));
  $('copy-contribution').onclick=async()=>{
    try{await navigator.clipboard.writeText($('contribution-copy-text').value);$('contribution-result').textContent='Copied. Paste the complete text into the GitHub issue description.';}
    catch{$('contribution-copy-text').focus();$('contribution-copy-text').select();$('contribution-result').textContent='Select and copy this text, then paste it into the GitHub issue description.';}
  };
  $('close-contribution').onclick=()=>$('contribution-dialog').close();
  $('contribution-dialog').addEventListener('cancel',event=>{if(posting)event.preventDefault();});
  $('discard-contribution').onclick=()=>{
    if(!confirm('Discard this saved draft?'))return;
    const previous=drafts[current.key];delete drafts[current.key];
    if(!write(draftKey,drafts)){drafts[current.key]=previous;$('contribution-draft-status').textContent='This browser could not remove the saved draft. Please try again.';return;}
    $('contribution-dialog').close();
  };
  $('new-problem').onclick=()=>open('problem');
  document.addEventListener('click',async event=>{
    const note=event.target.closest('[data-public-note]');if(note)open('note',note.dataset.publicNote);
    if(event.target.closest('[data-refresh-notes]'))await refresh(true);
    const remove=event.target.closest('[data-delete-note]');
    if(remove&&confirm('Delete this public comment?')){
      const id=remove.dataset.deleteNote;remove.disabled=true;
      try{
        await notesRequest('/'+id,{method:'DELETE',headers:{Authorization:'Bearer '+ownership[id]}});
        anonymousNotes=anonymousNotes.filter(note=>note.id!==id);notesRevision++;delete ownership[id];
        write(ownershipKey,ownership);write(notesCacheKey,anonymousNotes);combine();render();
      }catch(error){remove.disabled=false;alert('Could not delete the comment. '+error.message);}
    }
    if(event.target.closest('[data-new-problem]'))open('problem');
  });
  document.addEventListener('toggle',event=>{
    const id=event.target.dataset?.thread;if(!id)return;
    event.target.open?openThreads.add(id):openThreads.delete(id);
  },true);
  document.addEventListener('atlas:publication',render);
  window.addEventListener('focus',()=>refresh());
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
  document.addEventListener('atlas:votes',()=>window.ATLAS_VOTES?.render());
  window.ATLAS_COMMUNITY={notesHTML,refresh,submission,get contributions(){return contributions;},get loadedAt(){return loadedAt;}};
  render();refresh();
})();
