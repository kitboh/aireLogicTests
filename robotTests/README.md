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

## Alternative Installation

For users on Windows, you can alternatively install this repository by initiating a virtual environment with:
```
python -m venv venv/
```

Then enabling the virtual environment with:
```
venv\Scripts\activate.bat
```

Then installing the requirements.txt contents with:
```
pip install -r requirements.txt
```

Note: These instructions are suitable for CMD terminals, rather than Powershell which will use different commands and permissions enabled.

## Running the Tests

From the `robotTests` folder, run all tests with:
```bash
robot --outputdir output tests/
```

Test results will be available in the `output` directory.

## Test Failures

Currently 2 tests are failing in this suite due to bugs in the Cookie Clicker application.