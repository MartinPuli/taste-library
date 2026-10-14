import type { E2EConfig } from 'e2e';

export default {
  targets: [{ name: 'repository', platform: 'custom' }],
  tests: ['tests/e2e/*.e2e.ts'],
  timeout: 60000,
  retries: 0,
  workers: 2,
  reporters: ['list', 'markdown'],
} satisfies E2EConfig;
