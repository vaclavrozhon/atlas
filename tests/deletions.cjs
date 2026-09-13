const {chromium}=require('playwright');
const assert=require('assert');
const path=require('path');
const {pathToFileURL}=require('url');

(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1000}});
    await page.route('https://api.github.com/**', route=>route.fulfill({json:[]}));
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    // The offline reader uses the same publication handler without concurrent polling.
    await page.goto(pathToFileURL(path.resolve(__dirname,'../build/index.html')).href);
    await page.waitForFunction(()=>window.ATLAS_DEBUG);
    const result=await page.evaluate(async()=>{
      const api=ATLAS_DEBUG,d=api.data,id='TCS-DELETION-FIXTURE';
      const fixture={...structuredClone(d.cards.find(c=>c.evidence==='source'&&!c.scope_exclusion)),id,title:'Live deletion regression fixture'};
      const checks=[];
      const expect=(ok,label)=>{if(!ok)throw new Error(label);checks.push(label);};
      const originalCount=d.cards.length;
      const add=async(version)=>{
        await api.applyPublication({version,base_version:'fixture',cards:[fixture],meta:{...d.meta,total:d.cards.length+1},areas:d.areas});
        api.go(id);
        expect(d.cards.some(c=>c.id===id)&&!!document.getElementById(id),'Fixture appears before '+version);
      };
      await add('fixture-add-delta');
      await api.applyPublication({version:'fixture-remove-delta',base_version:'fixture-add-delta',cards:[],removed_ids:[id],meta:{...d.meta,total:originalCount},areas:d.areas});
      expect(!d.cards.some(c=>c.id===id),'Removal-only delta deletes catalogue record');
      expect(!document.getElementById(id)&&!api.state.matches.some(c=>c.id===id),'Removal-only delta clears rendered and filtered records');
      api.go(id);
      expect(!document.getElementById(id),'Removed ID cannot be reopened');
      await add('fixture-add-snapshot');
      await api.applyPublication({version:'fixture-after-missed-deletion',snapshot:true,cards:d.cards.filter(c=>c.id!==id),meta:{...d.meta,total:originalCount},areas:d.areas});
      expect(!d.cards.some(c=>c.id===id)&&!document.getElementById(id),'Full snapshot removes a record whose deletion delta was missed');
      await api.applyPublication({version:'fixture-metadata-only',cards:[],meta:d.meta,areas:d.areas});
      expect(d.cards.length===originalCount,'Partial metadata update retains all other records');
      const relatedSource=d.cards.find(c=>c.related_problem_ids?.length>5);
      const relatedTarget=structuredClone(d.cards.find(c=>c.id===relatedSource.related_problem_ids[0]));
      await api.go(relatedSource.id);
      document.querySelector(`#${relatedSource.id} .related-more`).open=true;
      const relatedSelector=`#${relatedSource.id} .related-problem-link[href="#${relatedTarget.id}"]`;
      await api.applyPublication({version:'fixture-related-rename',cards:[{...relatedTarget,title:'<b>Literal related title</b>'}],meta:d.meta,areas:d.areas});
      expect(document.querySelector(relatedSelector).textContent.includes('<b>Literal related title</b>'),'Target-only edits refresh incoming titles with escaped markup');
      expect(!document.querySelector(relatedSelector+' b'),'Related titles cannot inject HTML');
      expect(document.querySelector(`#${relatedSource.id} .related-more`).open,'Expanded related list survives a publication');
      await api.applyPublication({version:'fixture-related-delete',cards:[],removed_ids:[relatedTarget.id],meta:d.meta,areas:d.areas});
      expect(!document.querySelector(relatedSelector),'Deleting a target removes incoming links without a source-card update');
      await api.applyPublication({version:'fixture-related-restore',cards:[relatedTarget],meta:d.meta,areas:d.areas});
      expect(!!document.querySelector(relatedSelector),'Restoring an active target restores its incoming link');
      const removed=['TCS-7164','TCS-7191','TCS-7205','TCS-7206','TCS-7208','TCS-7209','TCS-7212','TCS-7213'];
      expect(!d.cards.some(c=>removed.includes(c.id)),'All eight requested deletions are absent from the reader');
      return {records:originalCount,checks};
    });
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify(result));
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
