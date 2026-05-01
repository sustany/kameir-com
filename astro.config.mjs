import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://kameir.com',
  trailingSlash: 'never',
  integrations: [
    sitemap(),
  ],
  build: {
    format: 'file', // generates /about.html instead of /about/index.html
    inlineStylesheets: 'always', // inline CSS → no _astro/ subdirectory needed
  },
  vite: {
    cacheDir: '/tmp/vite-cache-build2',
  },
});
