/* Shared LaTeX boundaries for rendering, paragraphs and compact previews. */
(() => {
  'use strict';
  const delimiters=[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false},{left:'$',right:'$',display:false}];
  function parts(text){
    text=String(text||'');const result=[];let start=0,i=0;
    while(i<text.length){
      if(text[i]==='\\'&&text[i+1]==='$'){i+=2;continue;}
      const delimiter=delimiters.find(d=>text.startsWith(d.left,i));
      if(!delimiter){i++;continue;}
      let j=i+delimiter.left.length,braces=0,end=-1;
      for(;j<text.length;j++){
        if(braces<=0&&text.startsWith(delimiter.right,j)){end=j+delimiter.right.length;break;}
        if(text[j]==='\\'){j++;continue;}
        if(text[j]==='{')braces++;else if(text[j]==='}')braces--;
      }
      if(end<0){i+=delimiter.left.length;continue;}
      if(start<i)result.push({math:false,text:text.slice(start,i),start,end:i});
      result.push({math:true,text:text.slice(i,end),formula:text.slice(i+delimiter.left.length,end-delimiter.right.length),display:delimiter.display,start:i,end});
      i=end;start=end;
    }
    if(start<text.length)result.push({math:false,text:text.slice(start),start,end:text.length});
    return result;
  }
  const escape=text=>String(text).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function plain(text){
    const symbols={alpha:'α',beta:'β',gamma:'γ',delta:'δ',varepsilon:'ε',epsilon:'ϵ',theta:'θ',lambda:'λ',mu:'μ',nu:'ν',pi:'π',rho:'ρ',sigma:'σ',tau:'τ',phi:'φ',varphi:'φ',chi:'χ',psi:'ψ',omega:'ω',Gamma:'Γ',Delta:'Δ',Theta:'Θ',Sigma:'Σ',Pi:'Π',Omega:'Ω',ell:'ℓ',le:'≤',leq:'≤',ge:'≥',geq:'≥',ne:'≠',neq:'≠',in:'∈',notin:'∉',subseteq:'⊆',to:'→',infty:'∞',sum:'Σ',prod:'Π',int:'∫',sqrt:'√',cdot:'·',times:'×',ldots:'…',cdots:'⋯'};
    return parts(text).map(part=>{
      if(!part.math)return part.text;
      let value=part.formula.replace(/\\(?:mathrm|mathbb|mathcal|operatorname|text)\s*\{([^{}]*)\}/g,'{$1}');
      value=value.replace(/\\(?:mathrm|mathbb|mathcal)\s+([A-Za-z])/g,'{$1}');
      value=value.replace(/\\([A-Za-z]+)\s*/g,(_,name)=>symbols[name]||name).replace(/\\([{}|,;! ])/g,'$1').replace(/[{}]/g,'');
      return value;
    }).join('');
  }
  function paragraphs(text,cls=''){
    const paragraphs=[''];
    for(const part of parts(text)){
      if(part.math){paragraphs[paragraphs.length-1]+=escape(part.text.replace(/\n\s*\n/g,'\n'));continue;}
      const chunks=part.text.split(/\n\n+/);
      paragraphs[paragraphs.length-1]+=escape(chunks.shift());paragraphs.push(...chunks.map(escape));
    }
    return paragraphs.filter(p=>p.trim()).map(p=>`<p${cls?` class="${escape(cls)}"`:''}>${p}</p>`).join('');
  }
  function excerpt(text,limit=700){
    text=String(text||'');if(text.length<=limit)return text;
    let cut=limit;
    const formula=parts(text).find(part=>part.math&&part.start<cut&&part.end>=cut);
    if(formula)cut=formula.end;
    else{
      const space=text.lastIndexOf(' ',cut);
      if(space>0)cut=space;
    }
    return text.slice(0,cut).trimEnd()+(cut<text.length?' […]':'');
  }
  let frame=0;
  function fit(){
    frame=0;
    for(const expression of document.querySelectorAll('.problem-card .katex,.community-problem .katex')){
      if(expression.closest('.katex-display'))continue;
      const wrapper=expression.parentElement,card=expression.closest('.problem-card,.community-problem');
      wrapper.classList.remove('math-overflow');
      const style=getComputedStyle(card),available=card.clientWidth-parseFloat(style.paddingLeft)-parseFloat(style.paddingRight);
      if(available>0&&expression.getBoundingClientRect().width>available)wrapper.classList.add('math-overflow');
    }
  }
  function render(root){
    if(typeof renderMathInElement!=='function')return;
    renderMathInElement(root,{delimiters,throwOnError:false,trust:false,strict:'ignore',ignoredClasses:['katex','public-notes','problem-votes']});
    if(!frame)frame=requestAnimationFrame(fit);
  }
  const api={parts,plain,paragraphs,excerpt,render};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  if(typeof window!=='undefined'){
    window.ATLAS_MATH=api;
    window.addEventListener('resize',()=>{if(!frame)frame=requestAnimationFrame(fit);});
  }
})();
