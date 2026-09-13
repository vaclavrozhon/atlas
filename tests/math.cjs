const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const katex=require('../web/vendor/katex.min.js');
const math=require('../web/math.js');

const source='A formula \\(x^{2}+y^{2}=z^{2}\\) and $$a+b=c$$.';
assert.deepEqual(math.parts(source).filter(p=>p.math).map(p=>p.formula),['x^{2}+y^{2}=z^{2}','a+b=c']);
const paragraph='Before.\n\n\\[\\begin{aligned}a&=b\\\\\n\nc&=d\\end{aligned}\\]\n\nAfter.';
assert.equal((math.paragraphs(paragraph).match(/<p>/g)||[]).length,3,'Blank lines inside a formula do not split its delimiters across HTML nodes');
assert(math.paragraphs('<img src=x onerror=alert(1)>').includes('&lt;img'));
const nearCut='x '.repeat(345)+'\\(\\frac{a+b}{c+d}\\) after the expression.';
const excerpt=math.excerpt(nearCut);
assert.equal(math.parts(excerpt).filter(p=>p.math).length,1,'A compact preview retains the whole formula at its boundary');
assert(!excerpt.includes('\\frac{a+b} […]'));
assert.equal(math.parts('The price is \\$2, while \\(x=2\\).').filter(p=>p.math).length,1);
assert.equal(math.plain('\\(\\mathrm{P}\\ne\\mathrm{NP}\\)'),'P≠NP','Search preserves operators between formatted names');

const top=new Set(['title','title_cs','formal','definitions','answer_criterion','context','why','status_note','review_note','source_formulation','context_excerpt','statement_review','working_summary','progress','context_blocks','references','related','textbook_notes']);
let cards=0,expressions=0;const errors=[];
function walk(value,location){
 if(typeof value==='string'){
  if(/(?:^|\.)(?:url|pdf_url|source_url|id|citation|key)$/.test(location))return;
  const parts=math.parts(value);
  for(const part of parts){
   if(part.math){
    expressions++;
    try{katex.renderToString(part.formula,{displayMode:part.display,throwOnError:true,trust:false,strict:'ignore'});}
    catch(error){errors.push({location,formula:part.formula,error:error.message});}
   }else if(/\\[()[\]]|(?<!\\)\$/.test(part.text))errors.push({location,text:part.text,error:'Unmatched math delimiter'});
  }
 }else if(Array.isArray(value))value.forEach((item,i)=>walk(item,location+'.'+i));
 else if(value&&typeof value==='object')for(const [key,item] of Object.entries(value))walk(item,location+'.'+key);
}
for(const file of fs.readdirSync(path.resolve(__dirname,'../data/cards'))){
 if(!file.endsWith('.json'))continue;
 const card=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../data/cards',file)));
 if(card.scope_exclusion||['resolved','excluded'].includes(card.status))continue;
 cards++;
 for(const [key,value] of Object.entries(card))if(top.has(key))walk(value,card.id+'.'+key);
}
assert.deepEqual(errors,[],'Every active card formula must parse with the bundled KaTeX');
console.log(JSON.stringify({cards,expressions,checks:['all active card LaTeX parses','balanced math delimiters','paragraphs retain multiline formulas','compact previews retain complete formulas','HTML remains escaped']}));
