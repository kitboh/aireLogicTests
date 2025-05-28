import pytest
from steps.functions.context import Context

def log_test_summary(step, request) -> None:
    print(f"Step Summary: {step}")

def pytest_bdd_step_error(step, request) -> None:
    log_test_summary(step, request)

def pytest_bdd_after_step(step, request) -> None:
    log_test_summary(step, request)

@pytest.fixture(autouse=True)
def context() -> Context:
    """Fixture to create a context object for each test. This allows us to pass data between steps.
    This is particularly useful for sharing the WebDriver allowing for parallel execution of tests.
    """
    return Context()
