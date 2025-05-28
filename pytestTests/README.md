# AireLogic Cookie Clicker Pytest-BDD Test Suite

This repository contains a test suite for the Cookie Clicker application, using [pytest-bdd](https://pytest-bdd.readthedocs.io/) for behavior-driven development.

## Installation

1. **Requirements**:  
    - Python (recommended: 3.8+)
    - All dependencies listed in `requirements.txt`

2. **Install Dependencies**:  
    Navigate to the `pytestTests` directory and run:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

- **features/**  
  Contains three different `.feature` files describing the BDD scenarios.

- **steps/**  
  Houses the step definitions that implement the scenarios from the feature files.

- **steps/functions/**  
  Contains setup utilities, including context management for passing the WebDriver instance between steps.

- **steps/pom/**  
  Implements the Page Object Model (POM) classes for structured and maintainable UI interactions.

- **config.py**  
  Located in the root directory, this file holds configuration information.  
  > **Note:** It is recommended to update `config.py` to load sensitive variables from a secure location (e.g., environment variables or a secrets manager).

## Running the Tests

From the `pytestTests` directory, execute:
```
pytest steps -m {TEST_TAGS} --gherkin-terminal-reporter --cucumberjson=./testresults.json -vvvv -rP
```
Where TEST_TAGS is the tag you wish to run.
Information on the tags available can be found in pytest.ini

For the full test suite use the tag full_suite.

---

## TODO

- Improve waits so that they wait for a certain criteria to be met, instead of using sleeps
- Improve the configuration so that it can load from an encrypted file, or from a secure storage platform
- Implement a teardown step that will take a screenshot and close the browser upon erroring
- Update the way that the usernames are generated to allow for parallelization. Currently the tests can run in parallel, but will error due to all tests using the username Test_User. The context is setup to allow this to be randomly generated, and the driver will be unique for each instance.
