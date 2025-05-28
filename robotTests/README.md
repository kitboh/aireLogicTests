# Aire Logic Cookie Clicker Site - Robot Test Suite

This repository contains automated tests for the Aire Logic Cookie Clicker site using [Robot Framework](https://robotframework.org/) and the [Robot Framework SeleniumLibrary](https://robotframework.org/SeleniumLibrary/).

## Installation

1. Ensure you have [Python 3](https://www.python.org/downloads/) installed.
2. Install Robot Framework:
    ```bash
    pip install robotframework
    ```
3. Install the SeleniumLibrary:
    ```bash
    pip install robotframework-seleniumlibrary
    ```

## Running the Tests

From the `robotTests` folder, run all tests with:
```bash
robot --outputdir output tests/
```

Test results will be available in the `output` directory.
