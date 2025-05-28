const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    experimentalRunAllSpecs: true,
    baseUrl: 'https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
