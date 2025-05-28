from dataclasses import dataclass
from selenium import webdriver
from config import Config

@dataclass(init=True)
class Context:
    """
    Context for the test, used to pass data between steps. In this suite it is used to pass the WebDriver.
    """
    driver = None
    base_url = Config.base_url

    def __init__(self):
        """
        Initialize the context with a WebDriver instance.
        """
        if Config.driver_type == "firefox" and self.driver is None:
            self.driver = webdriver.Firefox()
            self.driver.get(self.base_url)
        elif Config.driver_type == "chrome" and self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get(self.base_url)
        else:
            raise ValueError(f"Unsupported driver type: {Config.driver_type}")
        
    def getWebDriver(self):
        return self.driver
    
    def closeBrowser(self):
        """
        Close the browser if it is open.
        """
        if self.driver:
            self.driver.quit()
            self.driver = None
        else:
            print("No browser to close.")