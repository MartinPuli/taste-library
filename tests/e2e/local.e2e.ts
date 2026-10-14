import { test, expect } from 'e2e';
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../../', import.meta.url));
const read = (path: string) => readFileSync(new URL('../../' + path, import.meta.url), 'utf8');
const data = (path: string) => JSON.parse(read(path));

function run(...args: string[]) {
  return spawnSync('python3', ['scripts/query.py', ...args], {
    cwd: root, encoding: 'utf8', timeout: 10000, maxBuffer: 4 * 1024 * 1024,
  });
}

function query(...args: string[]) {
  const result = run(...args);
  expect(result.status).toBe(0);
  expect(result.stderr).toBe('');
  return JSON.parse(result.stdout);
}

function trace(section: any) {
  const raw = data(section.source_file);
  let original = raw;
  for (const key of section.source_pointer.slice(1).split('/')) original = original[key];
  expect(section.data).toEqual(original);
  expect(section.source_url).toBe(raw.source_url);
  expect(section.captured_at).toBe(raw.completed_at);
  const review = data(section.review_file);
  expect(review.not_checked).toContain('Responsive layouts');
  return section;
}

test('developer brief: discover, read, compare, and trace the primary reference', async () => {
  const matches = query('search', '--use-case', 'developer-tools', '--component', 'buttons', '--limit', '40', '--json');
  expect(matches.map((item: any) => item.id)).toEqual(expect.arrayContaining(['cursor', 'linear']));
  const profile = run('show', 'cursor');
  expect(profile.status).toBe(0);
  expect(profile.stdout).toContain('data/sections/cursor/layout.json');
  expect(profile.stdout).toContain('Content to bring');
  const compared = query('compare', 'cursor', 'linear', '--section', 'layout', '--json');
  const [cursor, linear] = compared.references.map(trace);
  expect(cursor.data.grid.columns).toBe(24);
  expect(linear.data.grid.columns).toBe(12);
  expect(cursor.data.grid.max_width).toBe('1300px');
  expect(read('guides/worked-examples.md')).toContain('/data/grid');
});

test('research brief: filter editorial references and retain CSS expressions', async () => {
  const matches = query('search', '--use-case', 'editorial-research', '--style', 'warm-editorial', '--limit', '40', '--json');
  expect(matches.map((item: any) => item.id)).toEqual(expect.arrayContaining(['anthropic', 'pangram']));
  const compared = query('compare', 'anthropic', 'pangram', '--section', 'typography', '--json');
  for (const section of compared.references) trace(section);
  const layout = trace(query('show', 'anthropic', '--section', 'layout'));
  expect(layout.data.grid.gutter).toContain('var(');
  expect(run('show', 'anthropic').stdout).toContain('Content to bring');
});

test('counts, limited opt-in, and absent evidence survive the CLI boundary', async () => {
  const catalog = data('catalog/index.json');
  const defaults = query('search', '--limit', '40', '--json');
  const all = query('search', '--include-limited', '--limit', '40', '--json');
  expect(defaults.length).toBe(catalog.counts.default_references);
  expect(all.length).toBe(catalog.counts.records);
  expect(all.map((item: any) => item.id)).toEqual(catalog.entries.map((item: any) => item.id));
  const limited = all.find((item: any) => item.quality === 'limited' && !item.sections.colors.has_data);
  expect(limited).toBeDefined();
  expect(defaults.map((item: any) => item.id)).not.toContain(limited.id);
  const section = trace(query('show', limited.id, '--section', 'colors'));
  expect(section.has_data).toBe(false);
  expect(section.data.baseline).toEqual([]);
});

test('empty searches and invalid comparisons produce distinct outcomes', async () => {
  expect(query('search', 'zzzzzz_no_match', '--json')).toEqual([]);
  for (const args of [
    ['compare', 'linear', 'linear', '--section', 'layout', '--json'],
    ['compare', 'linear', 'cursor', '--section', 'missing', '--json'],
    ['show', '../../README'],
    ['search', '--component', 'imaginary'],
  ]) {
    const result = run(...args);
    expect(result.status).toBe(2);
    expect(result.stdout).toBe('');
    expect(result.stderr).toContain('error:');
  }
});

test('component search yields inspectable records, and four references compare', async () => {
  const matches = query('search', '--component', 'forms', '--limit', '40', '--json');
  expect(matches.length).toBeGreaterThan(0);
  for (const candidate of matches) {
    for (const evidence of candidate.component_evidence.forms) {
      const section = query('show', candidate.id, '--section', evidence.section);
      let value = section.data;
      for (const key of evidence.pointer.slice(1).split('/')) value = value[key];
      expect(value.type).toBe('form');
    }
  }
  const result = query('compare', 'linear', 'cursor', 'anthropic', 'pangram', '--section', 'actions', '--json');
  expect(result.references).toHaveLength(4);
  for (const section of result.references) trace(section);
});
