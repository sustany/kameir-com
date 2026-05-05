import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://kameir.com',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      filter: (page) => ![
        'https://kameir.com/thanks',
        'https://kameir.com/ai-ethics-book-a-call',
        'https://kameir.com/ai-ethics-lead-magnet',
        'https://kameir.com/ai-ethics-template',
      ].includes(pag