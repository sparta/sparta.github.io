// Compare how a converted page *looks* against the page it replaces.
//
// parity-check.py compares what the pages say.  It cannot see how they
// say it, and that is where this conversion lost the most: ":c" centring
// dropped on 19 blocks, ":b" line breaks dropped on 1539, and every one
// of the 522 bordered, centred tables rendered as plain text -- none of
// which changes a single word.
//
// So both pages are rendered in a real browser and every run of text is
// compared on the properties a reader would notice: alignment, weight,
// size, style, family, colour and background.  Tables are compared on
// their frame, their cell frame, their cell alignment and whether they
// sit centred on the page.
//
// Blocks are paired by position rather than by string: "GitHub",
// "Tutorials" and "." each appear both inside the centred navigation
// table and again in the left-aligned body.
//
// This is a migration gate, like parity-check.py: it exists to show that
// nothing was lost on the way to reST, and it stops being useful once
// the published txt2html pages are gone.  It needs Node and Playwright,
// which nothing else here does, so it is not wired into CI.
//
// Usage:  node utils/layout-check.mjs OLD_PAGE_URL NEW_PAGE_URL
//   e.g.  node utils/layout-check.mjs \
//           file://$PWD/index.html file://$PWD/html/index.html
//
// Exits 1 if the two differ.

import { chromium } from 'playwright';

const extract = async (browser, url) => {
  const page = await browser.newPage({ viewportSize: { width: 1280, height: 900 } });
  await page.goto(url, { waitUntil: 'load' });
  const data = await page.evaluate(() => {
    const out = [];
    const walk = (el) => {
      for (const child of el.childNodes) {
        if (child.nodeType === 3) {
          const t = child.textContent.replace(/\s+/g, ' ').trim();
          if (t) {
            const cs = getComputedStyle(el);
            const r = el.getBoundingClientRect();
            out.push({
              text: t.slice(0, 60),
              align: cs.textAlign.replace(/^-(webkit|moz)-/, ''),
              weight: cs.fontWeight,
              size: Math.round(parseFloat(cs.fontSize)),
              style: cs.fontStyle,
              font: cs.fontFamily.split(',')[0].replace(/["']/g, ''),
              bg: cs.backgroundColor,
              color: cs.color,
              tag: el.tagName,
              // is the block centred on the page, whatever text-align says?
              centred: Math.abs((r.left + r.right) / 2 - innerWidth / 2) < 25 && r.width < innerWidth * 0.9,
            });
          }
        } else if (child.nodeType === 1) {
          const cs = getComputedStyle(child);
          if (cs.display !== 'none' && cs.visibility !== 'hidden') walk(child);
        }
      }
    };
    walk(document.body);
    const tables = [...document.querySelectorAll('table')].map(t => {
      const cs = getComputedStyle(t);
      const cell = t.querySelector('td, th');
      const ccs = cell ? getComputedStyle(cell) : {};
      const r = t.getBoundingClientRect();
      return {
        rows: t.rows.length,
        border: cs.borderTopWidth + ' ' + cs.borderTopStyle,
        cellBorder: (ccs.borderTopWidth || '') + ' ' + (ccs.borderTopStyle || ''),
        cellAlign: (ccs.textAlign || '').replace(/^-(webkit|moz)-/, ''),
        centred: Math.abs((r.left + r.right) / 2 - innerWidth / 2) < 25,
      };
    });
    return { blocks: out, tables };
  });
  await page.close();
  return data;
};

const browser = await chromium.launch(
  process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const [a, b] = [await extract(browser, process.argv[2]), await extract(browser, process.argv[3])];
await browser.close();

// Pair blocks by position, not by text: "GitHub", "Tutorials" and "."
// each appear both inside the centred navigation table and again in the
// left-aligned body, so keying on the string alone mismatches them.
let ptr = 0;
let diffs = 0;
for (const x of a.blocks) {
  let j = -1;
  for (let k = ptr; k < b.blocks.length; k++) {
    if (b.blocks[k].text === x.text) { j = k; break; }
  }
  if (j < 0) { console.log(`  MISSING  "${x.text}"`); diffs++; continue; }
  ptr = j + 1;
  const y = b.blocks[j];
  const problems = [];
  // text-align inherits, so the computed value on the text's own
  // parent already reflects a <CENTER> or a .center class above it.
  const oldCentred = x.align === 'center';
  const newCentred = y.align === 'center';
  if (oldCentred !== newCentred) problems.push(`centred ${oldCentred} -> ${newCentred}`);
  if (x.weight !== y.weight) problems.push(`weight ${x.weight} -> ${y.weight}`);
  if (Math.abs(x.size - y.size) > 1) problems.push(`size ${x.size} -> ${y.size}`);
  if (x.style !== y.style) problems.push(`style ${x.style} -> ${y.style}`);
  if (x.font !== y.font) problems.push(`font ${x.font} -> ${y.font}`);
  if (x.bg !== y.bg) problems.push(`background ${x.bg} -> ${y.bg}`);
  if (x.color !== y.color) problems.push(`colour ${x.color} -> ${y.color}`);
  if (problems.length) { console.log(`  ${problems.join(', ').padEnd(42)} "${x.text}"`); diffs++; }
}
console.log(`\n  tables: old ${a.tables.length}, new ${b.tables.length}`);
for (let i = 0; i < Math.min(a.tables.length, b.tables.length); i++) {
  const [t, u] = [a.tables[i], b.tables[i]];
  const p = [];
  if (t.border !== u.border) p.push(`border "${t.border}" -> "${u.border}"`);
  if (t.cellBorder !== u.cellBorder) p.push(`cell border "${t.cellBorder}" -> "${u.cellBorder}"`);
  if (t.cellAlign !== u.cellAlign) p.push(`cell align ${t.cellAlign} -> ${u.cellAlign}`);
  if (t.centred !== u.centred) p.push(`centred ${t.centred} -> ${u.centred}`);
  if (p.length) { console.log(`    table ${i + 1}: ${p.join('; ')}`); diffs++; }
}
console.log(`\n  ${diffs} presentation difference(s)`);
process.exit(diffs ? 1 : 0);
