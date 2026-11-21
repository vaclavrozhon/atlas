/* Shared mathematical vocabulary. Only local, known glossary links are rendered. */
(() => {
  'use strict';
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const data=()=>window.TCS_ATLAS?.shared_definitions||window.ATLAS_DEFINITIONS_DATA;
  const entries=()=>new Map((data()?.entries||[]).map(e=>[e.id,e]));
  function paragraphs(text,cls=''){
    const known=entries();
    return window.ATLAS_MATH.paragraphs(text,cls).replace(/\[([^\]\n]+)\]\(definitions\.html#([a-z-]+)\)/g,(match,label,id)=>
      known.has(id)?`<a href="definitions.html#${id}">${label}</a>`:match);
  }
  function links(card){
    const known=entries(),refs=(card.definition_refs||[]).filter(id=>known.has(id));
    if(!refs.length)return '';
    return `<nav class="shared-definitions" aria-label="Shared definitions"><span>Shared definitions</span> ${refs.map(id=>`<a href="definitions.html#${id}">${esc(known.get(id).title)}</a>`).join(' · ')}</nav>`;
  }
  function model(card){
    if(!card.definitions&&!card.definition_refs?.length)return '';
    const issue=card.definition_revision?.remaining_issue;
    return '<h3>Model & notation</h3>'+links(card)+(card.definitions?paragraphs(card.definitions,'formal'):'')+
      (issue?`<p class="small muted"><strong>Definition review pending.</strong> ${esc(issue)}</p>`:'');
  }
  function renderGlossary(){
    const root=document.getElementById('definition-entries');if(!root)return;
    const all=[...entries().values()];
    document.getElementById('definition-index').innerHTML=all.map(e=>`<li><a href="#${e.id}">${esc(e.title)}</a></li>`).join('');
    root.innerHTML=all.map(e=>`<section id="${e.id}" class="definition-entry"><h2>${esc(e.title)}</h2>${paragraphs(e.text)}${e.sources?.length?`<p class="small muted">Reference: ${e.sources.map(url=>{
      try{const parsed=new URL(url);return ['http:','https:'].includes(parsed.protocol)?`<a href="${esc(parsed.href)}" target="_blank" rel="noopener noreferrer">${esc(parsed.hostname)}</a>`:'';}catch{return '';}
    }).join(' · ')}</p>`:''}</section>`).join('');
    window.ATLAS_MATH.render(root);
    const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if(target)requestAnimationFrame(()=>target.scrollIntoView());
  }
  window.ATLAS_DEFINITIONS={paragraphs,links,model};
  renderGlossary();
})();
