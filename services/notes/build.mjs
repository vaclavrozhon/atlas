import {mkdir, readFile, writeFile} from 'node:fs/promises';

await mkdir('dist/server', {recursive: true});
const worker = await readFile('worker.mjs', 'utf8');
const manifest = await readFile('selection-manifest.mjs', 'utf8');
const dependency = "import { selectionManifest } from './selection-manifest.mjs';";
if (!worker.includes(dependency)) throw new Error('Missing selection manifest import');
await writeFile('dist/server/index.js', manifest.replace('export const selectionManifest', 'const selectionManifest') +
  '\n' + worker.replace(dependency, ''));
console.log('Built dist/server/index.js');
