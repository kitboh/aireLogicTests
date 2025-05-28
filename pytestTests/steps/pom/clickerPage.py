from selenium.webdriver.common.by import By

class clickerPage():
    
    def clickCookie(self, context):
        """
        Click the cookie button on the clicker page.
        
        :param context: The context object containing the WebDriver.
        """
        driver = context.getWebDriver()
        driver.find_element(By.ID, "click").click()

    def getCurrentCookies(self, context):
        """
        Get the current number of cookies displayed on the clicker page.
        
        :return: The current number of cookies as an integer.
        """
        driver = context.getWebDriver()
        return int(driver.find_element(By.ID, "cookies").text)
    
    def getCurrentFactories(self, context):
        """
        Get the current number of factories displayed on the clicker page.
        
        :return: The current number of factories as an integer.
        """
        driver = context.getWebDriver()
        return int(driver.find_element(By.ID, "factories").text)
    
    def sellCookie(self, cookie_count, context):
        """
        Sell a specified number of cookies.
        
        :param cookie_count: The number of cookies to sell.
        :param context: The context object containing the WebDriver.
        """
        driver = context.getWebDriver()
        driver.find_element(By.ID, "cookies-to-sell").send_keys(str(cookie_count))
        driver.find_element(By.ID, "sell-cookies").click()
    
    def checkCurrentCookies(self, expected_cookies, context):
        """
        Check if the current number of cookies matches the expected number.
        
        :param expected_cookies: The expected number of cookies.
        """
        assert self.getCurrentCookies(context) == expected_cookies, f"Expected {expected_cookies} cookies, but got {self.getCurrentCookies(context)}."

    def checkCurrentFactories(self, expected_factories, context):
        """
        Check if the current number of factories matches the expected number.
        
        :param expected_cookies: The expected number of factories.
        """
        assert self.getCurrentFactories(context) == expected_factories, f"Expected {expected_factories} cookies, but got {self.getCurrentFactories(context)}."

    def checkCurrentMoney(self, expected_money, context):
        """
        Check if the current money matches the expected amount.
        
        :param expected_money: The expected amount of money.
        """
        driver = context.getWebDriver()
        current_money = driver.find_element(By.ID, "money").text
        if current_money != expected_money:
            current_money = driver.find_element(By.ID, "money").text
        assert current_money == expected_money, f"Expected {expected_money} money, but got {current_money}."

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
    
    def purchaseFactory(self, amount, context):
        """
        Purchase a specified number of factories.
        
        :param amount: The number of factories to purchase.
        :param context: The context object containing the WebDriver.
        """
        driver = context.getWebDriver()
        driver.find_element(By.ID, "factories-to-buy").send_keys(str(amount))
        driver.find_element(By.ID, "buy-factories").click()
    
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