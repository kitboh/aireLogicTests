# Aire Logic Cookie Clicker Cypress Test Suite

This repository contains a Cypress test suite for the Aire Logic Cookie Clicker site.

## Prerequisites

- [Node.js](https://nodejs.org/) installed

## Installation

1. Clone this repository.
2. Install Cypress and dependencies:

    ```bash
    npm install cypress
    ```

## Running the Test Suite

To open the Cypress Test Runner, run:

```bash
npx cypress open
```

This will launch the Cypress UI where you can run and view the tests.

## Project Structure

- `cypress/` - Contains test specifications and support files.
- `cypress.config.js` - Cypress configuration file. Contains Base URL and config item to allow multiple specs to run at once
- `cypress/e2e/` - Contains the test files which get run
- `cypress/e2e/pom/` - Contains files for the POM

## More Information

- [Cypress Documentation](https://docs.cypress.io/)
- [Aire Logic Cookie Clicker](https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/)
