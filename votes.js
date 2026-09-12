/* Shared votes; one durable browser identity, no account required. */
(() => {
  'use strict';
  const api='https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes';
  const identityKey='tcs-atlas-voter-v1',cacheKey='tcs-atlas-votes-v1',pendingPrefix='tcs-atlas-vote-pending-v1:';
  const validId=id=>/^(TCS-\d{4,}|GH-\d+)$/.test(id);
  const validVote=v=>v&&validId(v.problem_id)&&[-1,0,1].includes(v.value)&&Number.isSafeInteger(v.revision)&&v.revision>=0;
  const validTotal=v=>v&&validId(v.problem_id)&&[v.up,v.down].every(n=>Number.isSafeInteger(n)&&n>=0)&&v.score===v.up-v.down;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const online=['http:','https:'].includes(location.protocol);
  let token='',storageAvailable=true,loaded=false,loading=null,generation=0,lastClick=0,rankingSignature=null;
  let totals=new Map(),mine=new Map();
  const busy=new Set(),errors=new Map();
  const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
  const write=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch{return false;}};
  try{
    token=localStorage.getItem(identityKey)||'';
    if(!/^[0-9a-f]{64}$/.test(token)){
      token=Array.from(crypto.getRandomValues(new Uint8Array(32)),n=>n.toString(16).padStart(2,'0')).join('');
      localStorage.setItem(identityKey,token);
    }
  }catch{storageAvailable=false;token='';}
  const cache=read(cacheKey,null);
  if(cache&&Array.isArray(cache.votes)&&cache.votes.every(validTotal)){
    totals=new Map(cache.votes.map(v=>[v.problem_id,v]));loaded=true;
    if(cache.identity===token&&Array.isArray(cache.mine)&&cache.mine.every(validVote))mine=new Map(cache.mine.map(v=>[v.problem_id,v]));
  }
  const own=id=>mine.get(id)||{problem_id:id,value:0,revision:0};
  const pending=id=>{const v=read(pendingPrefix+id,null);return validVote(v)&&v.problem_id===id&&v.revision>0?v:null;};
  const forget=id=>{try{localStorage.removeItem(pendingPrefix+id);}catch{/* A repeated request is safe. */}};
  function persist(){write(cacheKey,{identity:token,votes:[...totals.values()],mine:[...mine.values()]});}
  function controls(id){
    const v=totals.get(id)||{up:0,down:0,score:0},value=own(id).value,waiting=pending(id);
    const disabled=!online||!storageAvailable||busy.has(id)||!!waiting;
    const button=(direction,label,count)=>`<button type="button" class="vote-button" data-vote="${direction}" aria-label="${label}${value===direction?' (click to remove your vote)':''}" aria-pressed="${value===direction}" ${disabled?'disabled':''}><span aria-hidden="true">${direction===1?'👍':'👎'}</span><span class="vote-count">${loaded?count:'–'}</span></button>`;
    const message=!online?'Voting is available on the live website.':!storageAvailable?'Allow browser storage to vote.':busy.has(id)?'Saving…':waiting?'Vote not confirmed.':errors.get(id)||'';
    return button(1,'Thumbs up',v.up)+button(-1,'Thumbs down',v.down)+`<span class="vote-score" title="Thumbs up minus thumbs down">Score ${loaded?(v.score>0?'+':'')+v.score:'–'}</span><span class="vote-status" role="status">${esc(message)}</span>${waiting&&!busy.has(id)&&online&&storageAvailable?'<button type="button" class="vote-retry" data-vote-retry>Retry</button>':''}`;
  }
  function html(id){return validId(id)?`<div class="problem-votes" data-problem-votes="${id}" role="group" aria-label="Vote on this problem">${controls(id)}</div>`:'';}
  function render(id){
    for(const slot of document.querySelectorAll('[data-problem-votes]')){
      if(id&&slot.dataset.problemVotes!==id)continue;
      const selected=document.activeElement?.closest('[data-vote]');
      const focus=selected&&slot.contains(selected)?selected.dataset.vote:null;
      slot.innerHTML=controls(slot.dataset.problemVotes);
      if(focus)slot.querySelector(`[data-vote="${focus}"]`)?.focus({preventScroll:true});
    }
  }
  function changed(id){
    persist();render(id);
    const signature=JSON.stringify([...totals.values()].filter(v=>v.score).map(v=>[v.problem_id,v.score]).sort());
    if(signature!==rankingSignature){rankingSignature=signature;document.dispatchEvent(new CustomEvent('atlas:votes',{detail:{problemId:id}}));}
  }
  async function request(options={}){
    const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),12000);
    try{
      const response=await fetch(api,{...options,credentials:'omit',cache:'no-store',signal:controller.signal,
        headers:{...(token?{Authorization:'Bearer '+token}:{}),...(options.body?{'Content-Type':'application/json'}:{})}});
      const result=await response.json();
      if(!response.ok)throw Object.assign(new Error(result.error||'Voting is unavailable.'),{status:response.status,result});
      return result;
    }finally{clearTimeout(timer);}
  }
  function accept(result,id){
    if(!validVote(result.vote)||!validTotal(result.totals)||result.vote.problem_id!==id||result.totals.problem_id!==id)throw new Error('Invalid vote response.');
    mine.set(id,result.vote);totals.set(id,result.totals);loaded=true;
  }
  async function send(id,payload){
    if(busy.has(id))return;
    const focused=document.activeElement?.closest('[data-vote]');
    const focus=focused?.closest('[data-problem-votes]')?.dataset.problemVotes===id?focused.dataset.vote:null;
    busy.add(id);generation++;errors.delete(id);render(id);
    try{
      const result=await request({method:'POST',body:JSON.stringify(payload)});
      accept(result,id);forget(id);
    }catch(error){
      if(error.status===409){accept(error.result,id);forget(id);errors.set(id,'Vote updated in another tab. Please try again.');}
      else errors.set(id,'Vote not confirmed. Please retry.');
    }finally{
      busy.delete(id);generation++;changed(id);
      if(focus&&document.activeElement===document.body)document.querySelector(`[data-problem-votes="${id}"] [data-vote="${focus}"]`)?.focus({preventScroll:true});
    }
  }
  async function refresh(){
    if(!online||document.hidden)return;
    if(loading)return loading;
    const revision=generation;
    loading=(async()=>{
      try{
        const result=await request();
        if(!Array.isArray(result.votes)||!result.votes.every(validTotal)||!Array.isArray(result.mine)||!result.mine.every(validVote))throw new Error('Invalid vote response.');
        if(revision!==generation||busy.size)return;
        totals=new Map(result.votes.map(v=>[v.problem_id,v]));mine=new Map(result.mine.map(v=>[v.problem_id,v]));loaded=true;
        for(const [id,v] of mine){const p=pending(id);if(p&&v.revision>=p.revision)forget(id);}
        errors.clear();changed();
        const status=document.getElementById('voting-status');if(status)status.textContent='';
      }catch{
        const status=document.getElementById('voting-status');if(status)status.textContent=loaded?'Votes could not be refreshed. Showing last loaded counts.':'Votes are unavailable. Using the catalogue order for now.';
      }finally{loading=null;}
    })();
    return loading;
  }
  document.addEventListener('click',event=>{
    const button=event.target.closest('[data-vote],[data-vote-retry]'),slot=button?.closest('[data-problem-votes]');
    if(!slot||button.disabled||!storageAvailable||!online)return;
    // One physical double-click is one action, even with a very fast response.
    if(event.detail>1||Date.now()-lastClick<500)return;
    lastClick=Date.now();const id=slot.dataset.problemVotes;
    if(!validId(id)||busy.has(id))return;
    const previous=pending(id);
    if(previous){send(id,previous);return;}
    const direction=Number(button.dataset.vote);if(![-1,1].includes(direction))return;
    const payload={problem_id:id,value:own(id).value===direction?0:direction,revision:own(id).revision+1};
    // Save the exact request before sending, so reloads and lost responses can retry it.
    if(!write(pendingPrefix+id,payload)){errors.set(id,'Your vote was not sent: browser storage is unavailable.');render(id);return;}
    send(id,payload);
  });
  window.addEventListener('storage',event=>{
    if(event.key===identityKey){token=localStorage.getItem(identityKey)||'';mine.clear();generation++;}
    if(event.key===identityKey||event.key===cacheKey||event.key?.startsWith(pendingPrefix)){render();refresh();}
  });
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
  window.addEventListener('online',()=>refresh());
  document.addEventListener('atlas:publication',()=>render());
  window.ATLAS_VOTES={html,refresh,render,score:id=>totals.get(id)?.score||0,get loaded(){return loaded;},get own(){return [...mine.values()];}};
  if(online){setInterval(refresh,30000);refresh();}
})();
