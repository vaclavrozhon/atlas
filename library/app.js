(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[łŁ]/g, 'l').toLowerCase();
  const cards = [...document.querySelectorAll('article')].map(el => ({el, text:norm(el.textContent), count:Number(el.dataset.count)}));
  function filter() {
    const terms=norm($('search').value).trim().split(/\s+/).filter(Boolean);
    let sources=0, entries=0;
    for(const c of cards){
      const type=$('type').value;
      const category=$('category').value;
      const ok=(!category||c.el.dataset.categories.split(' ').includes(category))&&(!$('area').value||c.el.dataset.area===$('area').value)&&(!type||(type==='book'?c.el.dataset.kind.includes('book'):c.el.dataset.kind===type))&&terms.every(t=>c.text.includes(t));
      c.el.hidden=!ok;if(ok){sources++;entries+=c.count;}
    }
    $('count').textContent=`${sources} sources · ${entries} annotated entries in these sources`;
    $('empty').hidden=sources>0;
  }
  function clear(){for(const id of ['search','area','type','category'])$(id).value='';filter();}
  $('search').addEventListener('input',filter);
  $('area').addEventListener('change',filter);$('type').addEventListener('change',filter);
  $('category').addEventListener('change',filter);
  $('clear').addEventListener('click',clear);
  function followHash(){if(!location.hash)return;const el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(el?.tagName==='ARTICLE'){if(el.hidden)clear();el.scrollIntoView();}}
  window.addEventListener('hashchange',followHash);
  filter();followHash();
})();
