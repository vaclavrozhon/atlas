/* Shared editorial choices. The server stores overrides; the catalogue stores the initial proposal. */
(() => {
  'use strict';
  const data=window.TCS_ATLAS,api='https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/selection';
  const keyName='tcs-atlas-selection-editor-v1',cacheName='tcs-atlas-selection-cache-v1',pendingPrefix='tcs-atlas-selection-pending-v1:';
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const $=id=>document.getElementById(id),online=['http:','https:'].includes(location.protocol);
  const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
  const write=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch{return false;}};
  let token='',editing=false,loaded=false,loading=null,generation=0,compatible=true;
  let choices=new Map();
  const busy=new Set(),errors=new Map();
  const version=()=>data.meta.final_selection?.version||'';
  const card=id=>data.cards.find(c=>c.id===id);
  const valid=v=>v&&/^TCS-\d{4,}$/.test(v.problem_id)&&['green','red'].includes(v.color)&&typeof v.area==='string'&&Number.isSafeInteger(v.revision)&&v.revision>=0;
  const initial=c=>({problem_id:c.id,color:c.selection?.color||'red',area:c.selection?.area||c.area,revision:0});
  const choice=id=>choices.get(id)||initial(card(id));
  const color=c=>choices.get(c.id)?.color||c.selection?.color||'red';
  const pending=id=>{const value=read(pendingPrefix+id,null);return valid(value)&&value.problem_id===id&&value.revision>0?value:null;};
  const forget=id=>{try{localStorage.removeItem(pendingPrefix+id);}catch{}}
  const notice=text=>{if($('selection-status'))$('selection-status').textContent=text;};
  try{token=sessionStorage.getItem(keyName)||'';}catch{}
  const cached=read(cacheName,null);
  if(cached?.version===version()&&Array.isArray(cached.choices)&&cached.choices.every(valid))choices=new Map(cached.choices.map(v=>[v.problem_id,v]));

  function applyToData(){
    const areas=new Set(data.areas.map(a=>a.area));
    for(const c of data.cards){
      const saved=choices.get(c.id);
      c.area=saved&&areas.has(saved.area)?saved.area:(c.selection?.area||c.area);
    }
  }
  function persist(){write(cacheName,{version:version(),choices:[...choices.values()]});}
  function controls(c){
    const value=choice(c.id),waiting=pending(c.id),green=value.color==='green';
    const options=c.selection?.area_options||[c.selection?.area||c.area];
    const alternate=options.find(a=>a!==value.area),target=data.areas.find(a=>a.area===alternate);
    const disabled=!editing||!loaded||!compatible||busy.has(c.id)||!!waiting;
    const status=busy.has(c.id)?'Saving…':waiting?'Change not confirmed.':errors.get(c.id)||'';
    const buttons=editing?`<button type="button" data-selection-action="color" ${disabled?'disabled':''}>Mark ${green?'red':'green'}</button>${target?`<button type="button" data-selection-action="move" class="selection-move" ${disabled?'disabled':''} title="Move to ${esc(target.label)}; keep this color">${target.group==='large'?'↑':'↓'} ${esc(target.label)}</button>`:''}`:'';
    const retry=waiting&&editing&&!busy.has(c.id)&&compatible?'<button type="button" data-selection-action="retry">Retry</button>':'';
    const reason=!green&&c.selection?.upvoted_red_reason?`<p class="selection-exception"><strong>Initial proposal · red despite an upvote:</strong> ${esc(c.selection.upvoted_red_reason)}</p>`:'';
    return `<div class="selection-actions"><span class="selection-badge ${value.color}">${green?'Green · selected':'Red · not selected'}</span>${buttons}<span class="selection-card-status" role="status">${esc(status)}</span>${retry}</div>${reason}`;
  }
  function html(c){return `<div class="selection-controls" data-selection-controls="${esc(c.id)}" aria-label="Dataset selection">${controls(c)}</div>`;}
  function render(){
    for(const slot of document.querySelectorAll('[data-selection-controls]')){
      const c=card(slot.dataset.selectionControls);if(!c)continue;
      const action=slot.contains(document.activeElement)?document.activeElement.dataset.selectionAction:null;
      slot.innerHTML=controls(c);
      const article=slot.closest('.problem-card');article?.classList.remove('selection-green','selection-red');article?.classList.add('selection-'+color(c));
      if(action)slot.querySelector(`[data-selection-action="${action}"]`)?.focus({preventScroll:true});
    }
    $('edit-selection').textContent=editing?'Lock editing':'Edit selection';
    $('edit-selection').setAttribute('aria-pressed',String(editing));
  }
  function changed(id){
    applyToData();persist();render();
    document.dispatchEvent(new CustomEvent('atlas:selection',{detail:{problemId:id}}));
  }
  async function request(path='',options={}){
    const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),12000);
    try{
      const response=await fetch(api+path,{...options,cache:'no-store',credentials:'omit',signal:controller.signal,
        headers:{...(options.method==='POST'?{'Content-Type':'application/json',Authorization:'Bearer '+token}:{})}});
      const result=await response.json();
      if(!response.ok)throw Object.assign(new Error(result.error||'Shared selection is unavailable.'),{status:response.status,result});
      return result;
    }finally{clearTimeout(timer);}
  }
  function accept(result,id){
    if(result.version!==version()||!valid(result.choice)||result.choice.problem_id!==id)throw new Error('Invalid selection response.');
    choices.set(id,result.choice);
  }
  async function send(id,payload){
    if(busy.has(id)||!editing)return;
    busy.add(id);generation++;errors.delete(id);render();
    try{
      const result=await request('',{method:'POST',body:JSON.stringify(payload)});
      accept(result,id);forget(id);
    }catch(error){
      if(error.status===409&&error.result?.choice){
        accept(error.result,id);forget(id);errors.set(id,'Changed by another editor. Review the current choice before trying again.');
      }else if(error.status===409){
        compatible=false;forget(id);notice('The catalogue has changed. Reload this page before editing.');
      }else if(error.status===403){
        editing=false;notice('Enable editing again with the shared editor key. Your pending change can then be retried.');
      }else if(error.status===400){forget(id);errors.set(id,error.message);}
      else errors.set(id,'The change was not confirmed. Retry to check and save it.');
    }finally{busy.delete(id);generation++;changed(id);}
  }
  async function refresh(){
    if(!online||document.hidden)return;
    if(loading)return loading;
    const epoch=generation;
    loading=(async()=>{
      try{
        const result=await request();
        if(result.version!==version()){
          compatible=false;notice('The catalogue is being updated. Reload this page before editing.');render();return;
        }
        if(!Array.isArray(result.choices)||!result.choices.every(valid))throw new Error('Invalid shared choices.');
        if(epoch!==generation||busy.size)return;
        const old=JSON.stringify([...choices.values()]);
        choices=new Map(result.choices.map(v=>[v.problem_id,v]));loaded=true;compatible=true;
        for(const [id,v] of choices){
          const p=pending(id);
          if(p&&v.revision>=p.revision){
            if(v.revision!==p.revision||v.color!==p.color||v.area!==p.area)errors.set(id,'Changed by another editor. Showing the shared choice.');
            forget(id);
          }
        }
        notice('');
        if(old!==JSON.stringify([...choices.values()]))changed();else render();
      }catch{notice(loaded?'Shared choices could not be refreshed. Showing the last loaded selection.':'Shared choices are unavailable. Showing the saved proposal; editing will be enabled after synchronization.');}
      finally{loading=null;}
    })();
    return loading;
  }
  async function authenticate(){
    if(!/^[0-9a-f]{64}$/.test(token))throw new Error('Enter the shared editor key.');
    const result=await request('/auth',{method:'POST',body:'{}'});
    if(!result.can_edit)throw new Error('The editor key is not valid.');
    editing=true;
    try{sessionStorage.setItem(keyName,token);}catch{}
    render();await refresh();
  }
  $('edit-selection').addEventListener('click',()=>{
    if(editing){editing=false;token='';try{sessionStorage.removeItem(keyName);}catch{}render();return;}
    $('selection-login-error').textContent='';$('selection-editor-key').value='';$('selection-login').showModal();$('selection-editor-key').focus();
  });
  $('close-selection-login').addEventListener('click',()=>$('selection-login').close());
  $('selection-login-form').addEventListener('submit',async event=>{
    event.preventDefault();token=$('selection-editor-key').value.trim();$('selection-login-submit').disabled=true;
    try{await authenticate();$('selection-editor-key').value='';$('selection-login').close();}
    catch(error){$('selection-login-error').textContent=error.status===403?'The editor key is not valid.':error.message||'Editing could not be enabled.';}
    finally{$('selection-login-submit').disabled=false;}
  });
  document.addEventListener('click',event=>{
    const button=event.target.closest('[data-selection-action]'),slot=button?.closest('[data-selection-controls]');
    if(!slot||button.disabled||event.detail>1||!editing||!loaded||!compatible)return;
    const id=slot.dataset.selectionControls,c=card(id);if(!c||busy.has(id))return;
    const waiting=pending(id);if(waiting){send(id,waiting);return;}
    const current=choice(id),payload={problem_id:id,color:current.color,area:current.area,revision:current.revision+1,version:version()};
    if(button.dataset.selectionAction==='color')payload.color=current.color==='green'?'red':'green';
    else if(button.dataset.selectionAction==='move')payload.area=c.selection.area_options.find(a=>a!==current.area);
    else return;
    if(!payload.area)return;
    if(!write(pendingPrefix+id,payload)){errors.set(id,'Allow browser storage to save a change safely.');render();return;}
    send(id,payload);
  });
  window.addEventListener('storage',event=>{if(event.key===cacheName||event.key?.startsWith(pendingPrefix)){render();refresh();}});
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
  window.addEventListener('online',()=>refresh());
  document.addEventListener('atlas:publication',()=>{applyToData();render();refresh();});
  window.ATLAS_SELECTION={html,color,choice,applyToData,refresh,render,get editing(){return editing;},get loaded(){return loaded;}};
  applyToData();render();
  if(online){setInterval(refresh,15000);refresh();if(token)authenticate().catch(()=>{token='';editing=false;render();});}
  else notice('Offline proposal. Shared editing is available on the live website.');
})();
