import { test, expect } from 'e2e';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const base = process.env.TASTE_LIBRARY_BASE_URL;
async function read(path: string) {
  const response = await fetch(new URL(path, base!.replace(/\/?$/, '/')), {
    signal: AbortSignal.timeout(20000),
  });
  expect(response.status).toBe(200);
  return response.text();
}

async function each<T>(items: T[], visit: (item: T) => Promise<void>) {
  let next = 0;
  await Promise.all(Array.from({ length: Math.min(8, items.length) }, async () => {
    while (next < items.length) await visit(items[next++]);
  }));
}

test('all published raw results and section files preserve the audited TasteLabs data', { timeout: 180000 }, async () => {
  test.skip(!base, 'Set TASTE_LIBRARY_BASE_URL to test the full published collection.');
  const audit = JSON.parse(readFileSync(new URL('../../data/audits/tastelabs-2026-10-14.json', import.meta.url), 'utf8'));
  const catalog = JSON.parse(await read('catalog/index.json'));
  expect(catalog.entries.map((item: any) => item.id).sort())
    .toEqual(audit.records.map((item: any) => item.id).sort());
  const rawResults = new Map<string, any>();
  await each<any>(audit.records, async (record) => {
    expect(record.full_result_matches).toBe(true);
    expect(record.provenance_matches).toBe(true);
    expect(record.section_inventory_matches).toBe(true);
    const rawText = await read(record.raw_file);
    expect(createHash('sha256').update(rawText).digest('hex')).toBe(record.raw_sha256);
    rawResults.set(record.id, JSON.parse(rawText));
  });
  const sections: any[] = [];
  for (const entry of catalog.entries) {
    const system = rawResults.get(entry.id).result.design_system;
    expect(Object.keys(entry.sections).sort()).toEqual(Object.keys(system).sort());
    for (const [name, section] of Object.entries<any>(entry.sections)) sections.push({ entry, name, section });
  }
  expect(sections).toHaveLength(audit.counts.sections);
  await each<any>(sections, async ({ entry, name, section }) => {
    const document = JSON.parse(await read(section.path));
    const raw = rawResults.get(entry.id);
    expect(document.data).toEqual(raw.result.design_system[name]);
    expect(document.id).toBe(entry.id);
    expect(document.has_data).toBe(section.has_data);
    expect(document.source_url).toBe(raw.source_url);
    expect(document.captured_at).toBe(raw.completed_at);
    expect(document.source_file).toBe(entry.paths.raw);
    expect(document.source_pointer).toBe('/result/design_system/' + name);
  });
});
