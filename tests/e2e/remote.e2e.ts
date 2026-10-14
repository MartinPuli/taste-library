import { test, expect } from 'e2e';

// Supply a local file-server URL or an immutable raw GitHub commit URL.
const base = process.env.TASTE_LIBRARY_BASE_URL;
async function read(path: string, json = false): Promise<any> {
  const response = await fetch(new URL(path, base!.replace(/\/?$/, '/')), {
    signal: AbortSignal.timeout(15000),
  });
  expect(response.status).toBe(200);
  return json ? response.json() : response.text();
}

test('public entry points let an agent discover the collection and standalone skill', async () => {
  test.skip(!base, 'Set TASTE_LIBRARY_BASE_URL to test published files.');
  const [guide, catalog, skill, access] = await Promise.all([
    read('AGENTS.md'), read('catalog/search.json', true),
    read('skills/taste-library/SKILL.md'), read('skills/taste-library/references/access.md'),
  ]);
  expect(guide).toContain('catalog/search.json');
  expect(catalog.entries).toHaveLength(catalog.counts.records);
  expect(catalog.entries.filter((item: any) => item.quality !== 'limited')).toHaveLength(catalog.counts.default_references);
  expect(skill).toContain('references/access.md');
  expect(access).toContain('raw.githubusercontent.com/MartinPuli/taste-library/main/');
});

for (const brief of [
  { name: 'developer', useCase: 'developer-tools', component: 'buttons', ids: ['cursor', 'linear'], section: 'layout' },
  { name: 'research', useCase: 'editorial-research', style: 'warm-editorial', ids: ['anthropic', 'pangram'], section: 'typography' },
]) {
  test(brief.name + ' brief follows public catalog, profiles, sections, and original evidence', async () => {
    test.skip(!base, 'Set TASTE_LIBRARY_BASE_URL to test published files.');
    const catalog = await read('catalog/search.json', true);
    const candidates = catalog.entries.filter((item: any) => item.quality !== 'limited'
      && item.use_cases.includes(brief.useCase)
      && (!brief.component || item.components.includes(brief.component))
      && (!brief.style || item.styles.includes(brief.style)));
    expect(candidates.map((item: any) => item.id)).toEqual(expect.arrayContaining(brief.ids));
    for (const id of brief.ids) {
      const candidate = candidates.find((item: any) => item.id === id);
      const profileUrl = new URL(candidate.profile, base!.replace(/\/?$/, '/'));
      const profile = await read(candidate.profile);
      const link = [...profile.matchAll(/\]\(([^)]+)\)/g)]
        .map((match) => match[1]).find((path) => path.endsWith('/' + brief.section + '.json'));
      expect(link).toBeDefined();
      const response = await fetch(new URL(link!, profileUrl), { signal: AbortSignal.timeout(15000) });
      expect(response.status).toBe(200);
      const section = await response.json();
      const [raw, review] = await Promise.all([read(section.source_file, true), read(section.review_file, true)]);
      let original = raw;
      for (const key of section.source_pointer.slice(1).split('/')) original = original[key];
      expect(section.data).toEqual(original);
      expect(section.captured_at).toBe(raw.completed_at);
      expect(section.source_url).toBe(raw.source_url);
      expect(review.visual_observation.length).toBeGreaterThan(20);
      expect(review.not_checked).toContain('Responsive layouts');
    }
  });
}
