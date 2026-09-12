/* Related-problem springs, repulsion, and weak pairwise category attraction. */
(() => {
  'use strict';
  const $=id=>document.getElementById(id),canvas=$('map-canvas'),stage=$('map-stage');
  if(!window.TCS_ATLAS||!window.d3||!window.ATLAS_MATH){$('map-loading').textContent='The map could not load. Reload the page or open the catalogue.';return;}
  const ctx=canvas.getContext('2d');
  if(!ctx){$('map-loading').textContent='This browser cannot display the map. Please use the catalogue.';return;}
  const math=window.ATLAS_MATH,esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const norm=s=>math.plain(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const active=c=>c&&!c.scope_exclusion&&!['resolved','excluded'].includes(c.status);
  const number=n=>n.toLocaleString('en');
  let data=window.TCS_ATLAS,nodes=[],links=[],byId=new Map(),areas=new Map(),neighbors=new Map();
  let width=1,height=1,transform=d3.zoomIdentity,simulation=null,hovered=null,pinned=false,dragging=false;
  let paused=matchMedia('(prefers-reduced-motion: reduce)').matches,frame=0,hideTimer=0,initial=true,warming=false;
  let category='',query='',matches=new Set(),resultsLimit=25,fetching=false,disposed=false;
  const selection=d3.select(canvas),preview=$('map-preview');
  const colorAt=i=>d3.hcl((i*137.508+145)%360,43,48+(i%3)*7).formatHex();

  function savedDescription(card){
    const sentences=card.working_summary?.sentences;
    if(sentences?.length)return {label:'',text:sentences.join(' ')};
    const text=(card.statement_review?card.formal:card.source_formulation?.text)||card.formal||card.title;
    return {label:'Saved question',text:math.excerpt(text,700)};
  }
  function categoryForce(){
    let members=[];
    function force(alpha){
      const strength=Number($('map-attraction').value)*0.0003;
      if(!strength)return;
      for(const group of members){
        let x=0,y=0;
        for(const n of group){x+=n.x;y+=n.y;}
        x/=group.length;y/=group.length;
        // (centroid - position) equals the sum of all same-category pair
        // attractions divided by category size. No artificial graph edges.
        for(const n of group){n.vx+=(x-n.x)*strength*alpha;n.vy+=(y-n.y)*strength*alpha;}
      }
    }
    force.initialize=values=>{members=Array.from(d3.group(values,n=>n.card.area).values());};
    return force;
  }
  function schedule(){if(!frame&&!disposed)frame=requestAnimationFrame(draw);}
  function resume(){if(!paused&&!document.hidden&&!hovered&&!warming)simulation?.restart();}
  function stopForPreview(){simulation?.stop();}
  function setHash(id){
    try{history.replaceState(null,'',location.pathname+location.search+(id?'#'+encodeURIComponent(id):''));}catch(_){/* file: still works without history support */}
  }
  function hidePreview(){
    clearTimeout(hideTimer);const focused=preview.contains(document.activeElement);
    hovered=null;pinned=false;preview.hidden=true;setHash('');schedule();resume();
    if(focused)canvas.focus({preventScroll:true});
  }
  function deferHide(){
    if(pinned||dragging)return;
    clearTimeout(hideTimer);hideTimer=setTimeout(()=>{if(!preview.matches(':hover')&&!preview.contains(document.activeElement))hidePreview();},180);
  }
  function placePreview(){
    if(!hovered||preview.hidden)return;
    if(width<=760&&matchMedia('(max-width:760px)').matches){preview.style.left='12px';preview.style.top='auto';preview.style.bottom='12px';return;}
    preview.style.bottom='auto';
    const x=transform.applyX(hovered.x),y=transform.applyY(hovered.y),w=preview.offsetWidth,h=preview.offsetHeight;
    const left=x+w+28<width?x+20:x-w-20;
    preview.style.left=Math.max(12,Math.min(width-w-12,left))+'px';
    preview.style.top=Math.max(12,Math.min(height-h-12,y-28))+'px';
  }
  function showPreview(node,keep=false){
    if(!node)return;
    clearTimeout(hideTimer);
    const changed=hovered!==node;hovered=node;pinned=keep;stopForPreview();
    if(changed||preview.hidden){
      const c=node.card,a=areas.get(c.area),description=savedDescription(c);
      preview.dataset.id=c.id;preview.style.setProperty('--category-color',node.color);
      $('map-preview-meta').textContent=c.id+' · '+(a?.label||c.area);
      $('map-preview-title').textContent=c.title;
      $('map-preview-text').innerHTML=(description.label?'<p class="map-text-origin">'+esc(description.label)+'</p>':'')+math.paragraphs(description.text);
      $('map-preview-degree').textContent=number(neighbors.get(c.id)?.size||0)+' related problems';
      $('map-preview-link').href='index.html#'+encodeURIComponent(c.id);
      preview.hidden=false;math.render(preview);preview.scrollTop=0;
    }
    if(keep)setHash(node.id);
    placePreview();schedule();
  }
  function hit(x,y){
    let closest=null,distance=Infinity;
    for(const n of nodes){
      const d=Math.hypot(transform.applyX(n.x)-x,transform.applyY(n.y)-y);
      if(d<=Math.max(8,n.r*transform.k+4)&&d<distance){closest=n;distance=d;}
    }
    return closest;
  }
  function emphasis(n){
    if(hovered)return n===hovered||neighbors.get(hovered.id)?.has(n.id);
    return !category&&!query||matches.has(n.id);
  }
  function draw(){
    frame=0;const ratio=Math.min(devicePixelRatio||1,2);
    ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,width,height);
    const focused=!!hovered||!!category||!!query;
    ctx.save();ctx.translate(transform.x,transform.y);ctx.scale(transform.k,transform.k);
    for(const edge of links){
      const highlighted=hovered?edge.source===hovered||edge.target===hovered:emphasis(edge.source)&&emphasis(edge.target);
      ctx.strokeStyle=highlighted&&focused?'#38664c99':focused?'#697b6c12':'#6e84743a';
      ctx.lineWidth=(highlighted&&focused?1.35:.65)/transform.k;
      ctx.beginPath();ctx.moveTo(edge.source.x,edge.source.y);ctx.lineTo(edge.target.x,edge.target.y);ctx.stroke();
    }
    for(const n of nodes){
      const x=transform.applyX(n.x),y=transform.applyY(n.y);
      if(x < -30||y < -30||x>width+30||y>height+30)continue;
      ctx.globalAlpha=emphasis(n)?1:.12;
      ctx.beginPath();ctx.arc(n.x,n.y,Math.max(n.r,3/transform.k),0,Math.PI*2);
      ctx.fillStyle=n.color;ctx.fill();
      ctx.strokeStyle='#ffffff';ctx.lineWidth=.7/transform.k;ctx.stroke();
      if(n===hovered){ctx.beginPath();ctx.arc(n.x,n.y,Math.max(n.r,3/transform.k)+3/transform.k,0,Math.PI*2);ctx.strokeStyle='#1c3929';ctx.lineWidth=1.7/transform.k;ctx.stroke();}
    }
    ctx.restore();ctx.globalAlpha=1;
    // Collision-cull category labels so dense central regions remain legible.
    if(!hovered&&!query){
      const boxes=[];
      ctx.font='500 11px Inter, system-ui, sans-serif';ctx.textAlign='center';
      for(const [key,group] of d3.group(nodes,n=>n.card.area)){
        if(category&&category!==key)continue;
        const x=transform.applyX(d3.mean(group,n=>n.x)),y=transform.applyY(d3.mean(group,n=>n.y))-15;
        const label=areas.get(key)?.label||key,w=ctx.measureText(label).width+12;
        if(x-w/2<8||x+w/2>width-8||y<75||y>height-50)continue;
        const box={x:x-w/2,y:y-12,w,h:21};
        if(boxes.some(b=>box.x<b.x+b.w+10&&box.x+box.w>b.x-10&&box.y<b.y+b.h+12&&box.y+box.h>b.y-12))continue;
        boxes.push(box);ctx.fillStyle='#fafbf8d9';ctx.fillRect(box.x,box.y,w,19);ctx.fillStyle='#42594bc4';ctx.fillText(label,x,y+1);
      }
    }
    if(hovered){
      const adjacent=neighbors.get(hovered.id)||new Set();ctx.font='11px Inter, system-ui, sans-serif';ctx.textAlign='left';
      for(const n of nodes){
        if(!adjacent.has(n.id)||transform.k<.65)continue;
        const x=transform.applyX(n.x)+9,y=transform.applyY(n.y)+3;
        if(x<0||x>width-90||y<0||y>height)continue;
        ctx.fillStyle='#fafbf8e8';ctx.fillRect(x-2,y-11,68,15);ctx.fillStyle='#566459';ctx.fillText(n.id,x,y);
      }
    }
    placePreview();
  }
  const zoom=d3.zoom().scaleExtent([.08,8]).filter(event=>{
    if(event.type==='wheel')return !event.button;
    if(event.touches?.length>1)return true;
    return !event.button&&!hit(...d3.pointer(event.touches?.[0]||event,canvas));
  }).on('start',event=>{if(event.sourceEvent&&!pinned)hidePreview();}).on('zoom',event=>{transform=event.transform;schedule();});
  selection.call(zoom).on('dblclick.zoom',null);
  selection.call(d3.drag().clickDistance(4).filter(event=>!event.button&&(!event.touches||event.touches.length===1))
    .subject(event=>{const n=hit(event.x,event.y);return n?{x:transform.applyX(n.x),y:transform.applyY(n.y),node:n}:null;})
    .on('start',event=>{dragging=true;const n=event.subject.node;n.fx=n.x;n.fy=n.y;showPreview(n,true);if(!paused)simulation.alphaTarget(.12).restart();})
    .on('drag',event=>{const n=event.subject.node;[n.fx,n.fy]=transform.invert([event.x,event.y]);n.x=n.fx;n.y=n.fy;schedule();})
    .on('end',event=>{dragging=false;const n=event.subject.node;n.fx=null;n.fy=null;simulation.alphaTarget(0);if(paused||hovered)simulation.stop();schedule();}));

  function fit(targets=nodes){
    if(!targets.length){selection.call(zoom.transform,d3.zoomIdentity.translate(width/2,height/2));return;}
    const minX=d3.min(targets,n=>n.x)-35,maxX=d3.max(targets,n=>n.x)+35;
    const minY=d3.min(targets,n=>n.y)-35,maxY=d3.max(targets,n=>n.y)+35;
    const k=Math.max(.08,Math.min(1.8,(width-80)/Math.max(100,maxX-minX),(height-130)/Math.max(100,maxY-minY)));
    selection.call(zoom.transform,d3.zoomIdentity.translate(width/2-k*(minX+maxX)/2,height/2+10-k*(minY+maxY)/2).scale(k));
  }
  function focusProblem(id){
    const n=byId.get(id);if(!n)return false;
    const k=Math.max(transform.k,1.35);
    const x=width>760?width*.35:width*.5,y=height*.4;
    selection.call(zoom.transform,d3.zoomIdentity.translate(x-k*n.x,y-k*n.y).scale(k));
    showPreview(n,true);return true;
  }
  function resize(){
    const oldWidth=width,oldHeight=height;({width,height}=stage.getBoundingClientRect());
    const ratio=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);
    zoom.extent([[0,0],[width,height]]);
    if(initial)selection.call(zoom.transform,d3.zoomIdentity.translate(width/2,height/2));
    else selection.call(zoom.transform,d3.zoomIdentity.translate(transform.x+(width-oldWidth)/2,transform.y+(height-oldHeight)/2).scale(transform.k));
    schedule();
  }
  function resultList(){
    const filtered=nodes.filter(n=>matches.has(n.id));
    $('map-results-panel').hidden=!query&&!category;
    $('map-result-count').textContent=number(filtered.length)+' matching problems'+(filtered.length?'':' — try another search.');
    $('map-results').innerHTML=filtered.slice(0,resultsLimit).map(n=>'<li><button type="button" data-problem="'+esc(n.id)+'"><small>'+esc(n.id)+'</small>'+esc(n.card.title)+'</button></li>').join('');
    $('map-more').hidden=filtered.length<=resultsLimit;
    $('map-legend').hidden=!!query;
  }
  function filter(){
    category=$('map-category').value;query=norm($('map-search').value.trim());resultsLimit=25;
    matches=new Set(nodes.filter(n=>(!category||n.card.area===category)&&(!query||n.search.includes(query))).map(n=>n.id));
    for(const b of $('map-legend').querySelectorAll('button'))b.setAttribute('aria-pressed',String(b.dataset.category===category));
    resultList();hidePreview();schedule();
  }
  function buildControls(){
    const counts=d3.rollup(nodes,v=>v.length,n=>n.card.area);
    $('map-category').innerHTML='<option value="">All categories</option>'+Array.from(areas.values()).filter(a=>counts.has(a.area)).map(a=>'<option value="'+esc(a.area)+'">'+esc(a.label)+'</option>').join('');
    $('map-category').value=areas.has(category)?category:'';category=$('map-category').value;
    $('map-legend').innerHTML=Array.from(areas.values()).filter(a=>counts.has(a.area)).map(a=>'<button class="map-category" type="button" data-category="'+esc(a.area)+'" aria-pressed="'+(a.area===category)+'"><span class="map-swatch" style="--category-color:'+a.color+'"></span><span>'+esc(a.label)+'</span><small>'+number(counts.get(a.area))+'</small></button>').join('');
    $('map-stats').textContent=number(nodes.length)+' problems · '+number(links.length)+' connections';
    canvas.setAttribute('aria-label',`Interactive network of ${nodes.length} problems and ${links.length} related-problem connections`);
    matches=new Set(nodes.filter(n=>(!category||n.card.area===category)&&(!query||n.search.includes(query))).map(n=>n.id));resultList();
  }
  function applyCatalogue(next){
    if(!Array.isArray(next?.cards)||!Array.isArray(next?.areas))return false;
    const old=byId,selected=pinned?hovered?.id:null;simulation?.stop();
    data=next;areas=new Map(next.areas.map((a,i)=>[a.area,{...a,color:colorAt(i)}]));
    const cardList=next.cards.filter(active).sort((a,b)=>a.id.localeCompare(b.id));
    const offsets=new Map();
    nodes=cardList.map(c=>{
      const before=old.get(c.id),a=areas.get(c.area),i=next.areas.findIndex(a=>a.area===c.area);
      const j=offsets.get(c.area)||0;offsets.set(c.area,j+1);
      const angle=i*2.39996323,ring=210*Math.sqrt(i+1),local=j*2.39996323,spread=13*Math.sqrt(j+1);
      return {id:c.id,card:c,color:a?.color||'#61776b',r:4.4,x:before?.x??Math.cos(angle)*ring+Math.cos(local)*spread,y:before?.y??Math.sin(angle)*ring+Math.sin(local)*spread,
        search:norm([c.id,c.title,a?.label||c.area,...(c.working_summary?.sentences||[]),c.formal].join(' '))};
    });
    byId=new Map(nodes.map(n=>[n.id,n]));neighbors=new Map(nodes.map(n=>[n.id,new Set()]));
    const seen=new Set();links=[];
    for(const n of nodes)for(const target of n.card.related_problem_ids||[]){
      if(target===n.id||!byId.has(target))continue;
      const key=[n.id,target].sort().join('|');if(seen.has(key))continue;seen.add(key);
      links.push({source:n.id,target});neighbors.get(n.id).add(target);neighbors.get(target).add(n.id);
    }
    simulation=d3.forceSimulation(nodes).stop().randomSource(d3.randomLcg(.42)).alphaDecay(.025).velocityDecay(.4)
      .force('links',d3.forceLink(links).id(n=>n.id).distance(65).strength(.16))
      .force('repulsion',d3.forceManyBody().strength(-38).distanceMax(1100))
      .force('collision',d3.forceCollide(8).iterations(2))
      .force('category',categoryForce()).force('x',d3.forceX(0).strength(.002)).force('y',d3.forceY(0).strength(.002))
      .on('tick',schedule);
    buildControls();
    hovered=null;preview.hidden=true;
    if(selected&&byId.has(selected))showPreview(byId.get(selected),true);
    else if(selected){hidePreview();}
    $('map-loading').hidden=nodes.length>0;
    if(!nodes.length)$('map-loading').textContent='No active problems in this catalogue.';
    if(!initial){simulation.alpha(.35);resume();schedule();}
    return true;
  }
  async function checkUpdates(){
    if(fetching||disposed||document.hidden||location.protocol==='file:')return;
    fetching=true;
    try{
      const response=await fetch('version.json',{cache:'no-store'});if(!response.ok)return;
      const marker=await response.json();if(!marker.version||marker.version===data.meta.version)return;
      const full=await fetch('catalog.json',{cache:'no-store'});if(!full.ok)return;
      const next=await full.json();if(next.meta?.version!==marker.version)return;
      applyCatalogue(next);
    }catch(_){/* The bundled catalogue remains usable offline; retry next time. */}
    finally{fetching=false;}
  }
  canvas.addEventListener('pointermove',event=>{
    if(dragging||event.buttons||event.pointerType==='touch')return;
    const n=hit(...d3.pointer(event,canvas));canvas.style.cursor=n?'pointer':'grab';
    if(pinned)return;
    if(n)showPreview(n);else deferHide();
  });
  canvas.addEventListener('pointerleave',deferHide);
  canvas.addEventListener('click',event=>{const n=hit(...d3.pointer(event,canvas));if(n)showPreview(n,true);else hidePreview();});
  preview.addEventListener('pointerenter',()=>clearTimeout(hideTimer));preview.addEventListener('pointerleave',deferHide);
  preview.addEventListener('focusin',()=>{pinned=true;if(hovered)setHash(hovered.id);});
  $('map-preview-close').addEventListener('click',hidePreview);
  $('map-search').addEventListener('input',filter);$('map-category').addEventListener('change',filter);
  $('map-clear').addEventListener('click',()=>{$('map-search').value='';$('map-category').value='';filter();});
  $('map-legend').addEventListener('click',event=>{const b=event.target.closest('[data-category]');if(b){$('map-category').value=category===b.dataset.category?'':b.dataset.category;filter();}});
  $('map-results').addEventListener('click',event=>{const b=event.target.closest('[data-problem]');if(b)focusProblem(b.dataset.problem);});
  $('map-more').addEventListener('click',()=>{resultsLimit+=25;resultList();});
  $('map-search').addEventListener('keydown',event=>{if(event.key==='Enter'){const id=matches.values().next().value;if(id){event.preventDefault();focusProblem(id);$('map-preview-link').focus();}}});
  $('map-fit').addEventListener('click',()=>{hidePreview();fit();});
  $('map-zoom-in').addEventListener('click',()=>selection.call(zoom.scaleBy,1.4));
  $('map-zoom-out').addEventListener('click',()=>selection.call(zoom.scaleBy,1/1.4));
  function motionButton(){const b=$('map-pause');b.textContent=paused?'Resume motion':'Pause motion';b.setAttribute('aria-pressed',String(paused));}
  $('map-pause').addEventListener('click',()=>{paused=!paused;motionButton();if(paused)simulation.stop();else{simulation.alpha(Math.max(simulation.alpha(),.2));resume();}});
  $('map-attraction').addEventListener('input',()=>{
    const value=Number($('map-attraction').value);$('map-attraction-value').textContent=value===0?'Off':value<40?'Weak':value<75?'Medium':'Strong';
    simulation.alpha(.45);resume();schedule();
  });
  canvas.addEventListener('keydown',event=>{
    if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(event.key)){
      event.preventDefault();const list=nodes.filter(n=>matches.has(n.id));if(!list.length)return;
      let i=list.indexOf(hovered),step=['ArrowLeft','ArrowUp'].includes(event.key)?-1:1;
      i=i<0?(step<0?list.length-1:0):(i+step+list.length)%list.length;focusProblem(list[i].id);
    }else if(event.key==='Enter'&&hovered){event.preventDefault();showPreview(hovered,true);$('map-preview-link').focus();}
    else if(event.key==='+'||event.key==='='){event.preventDefault();selection.call(zoom.scaleBy,1.4);}
    else if(event.key==='-'){event.preventDefault();selection.call(zoom.scaleBy,1/1.4);}
    else if(event.key==='Home'){event.preventDefault();hidePreview();fit();}
  });
  document.addEventListener('keydown',event=>{if(event.key==='Escape')hidePreview();});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)simulation.stop();else{resume();checkUpdates();}});
  window.addEventListener('hashchange',()=>{const id=decodeURIComponent(location.hash.slice(1));if(id)focusProblem(id);else hidePreview();});
  new ResizeObserver(resize).observe(stage);
  applyCatalogue(data);resize();motionButton();
  // A short, frame-budgeted warm-up avoids displaying a collapsed initial cloud.
  warming=true;let ticks=0;$('map-loading').hidden=!nodes.length;
  function warm(){
    if(disposed)return;
    const start=performance.now();do{simulation.tick();ticks++;}while(ticks<100&&performance.now()-start<10);
    if(ticks<100){requestAnimationFrame(warm);return;}
    warming=false;initial=false;$('map-loading').hidden=nodes.length>0;fit();
    const id=decodeURIComponent(location.hash.slice(1));if(id&&!focusProblem(id))setHash('');
    resume();schedule();
  }
  requestAnimationFrame(warm);
  const interval=setInterval(checkUpdates,60000);checkUpdates();
  window.addEventListener('pagehide',()=>{simulation.stop();});
  window.addEventListener('pageshow',()=>{resume();checkUpdates();});
  window.ATLAS_MAP={get data(){return data;},get nodes(){return nodes;},get links(){return links;},get simulation(){return simulation;},
    get ready(){return !warming;},get transform(){return transform;},get paused(){return paused;},savedDescription,focusProblem,applyCatalogue,checkUpdates,
    dispose(){disposed=true;clearInterval(interval);simulation.stop();cancelAnimationFrame(frame);}};
})();
