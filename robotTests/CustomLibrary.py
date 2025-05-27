
from robot.api.logger import info, debug, trace, console

class CustomLibrary:

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        return None

    def test_custom(self, test):
        assert test == test
        info(f'Value: {test}')
