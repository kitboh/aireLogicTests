from selenium.webdriver.common.by import By

class homePage():
    
    def createNewUser(self, username, context):
        """
        Create a new user with the given username.
        
        :param username: The username to create.
        :param context: The context object containing the WebDriver.
        """
        driver = context.getWebDriver()
        
        driver.find_element(By.NAME, "name").send_keys(username)
        driver.find_element(By.XPATH, "//button[contains(text(),'Start!')]").click()

    def existingUserLocator(self, username, context):
        """
        Locator for an existing user based on the username.
        
        :param username: The username to locate.
        :return: An element containing the XPath for the existing user.
        """
        driver = context.getWebDriver()
        user_element = driver.find_element(By.XPATH, f"//a[contains(text(),'{username}')]")
        assert user_element is not None, f"User {username} does not exist in the user list."
        return user_element
    
    def getUserScore(self, username, context):
        """
        Get the score of an existing user.
        
        :param username: The username to get the score for.
        :param context: The context object containing the WebDriver.
        :return: The score of the user as an integer.
        """
        driver = context.getWebDriver()
        # I dislike this XPath, but it works considering the structure of the table. I could also use find_elements and loop through
        score_element = driver.find_element(By.XPATH, f"//tr/td/a[contains(text(),'Test_User')]/parent::td/following-sibling::td") 
        return int(score_element.text)
        
    def checkUserExists(self, username, context):
        self.existingUserLocator(username, context)

    def clickExistingUser(self, username, context):
        self.existingUserLocator(username, context).click()

    def checkUserScore(self, username, expected_score, context):
        displayed_score = self.getUserScore(username, context)
        assert displayed_score == expected_score, f"Expected score for {username} is {expected_score}, but got {displayed_score}."