from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse
from selenium import webdriver

from functions.context import Context
from config import Config

from pom.homePage import homePage
from pom.clickerPage import clickerPage

scenarios(
    "../features/homePage.feature",
    "../features/clickerPage.feature",
    "../features/factories.feature"
)

USER_NAME = Config.user_name

@given("the user opens the homepage", target_fixture="context")
def step_given_homepage(context: Context) -> Context:
    driver = context.getWebDriver()
    return context

@when(parse("a user is created with the name '{username}'"))
def step_when_create_user(context: Context, username: str) -> Context:
    home_page = homePage()
    home_page.createNewUser(username, context)
    return context

@when("I click the cookie")
def step_when_click_cookie(context: Context) -> Context:
    clicker_page = clickerPage()
    clicker_page.clickCookie(context)
    return context

@when(parse("I click the cookie '{amount}' times"))
def step_when_click_cookie_multiple(context: Context, amount: str) -> Context:
    clicker_page = clickerPage()
    for i in range(0, int(amount)):
        clicker_page.clickCookie(context)
    return context

@when(parse("I sell '{cookie_count}' cookie"))
def step_when_sell_cookie(context: Context, cookie_count: str) -> Context:
    clicker_page = clickerPage()
    clicker_page.sellCookie(int(cookie_count), context)   
    return context

@when(parse("I purchase '{amount}' factory"))
def step_when_purchase_factory(context: Context, amount: str) -> Context:
    clicker_page = clickerPage()
    clicker_page.purchaseFactory(int(amount), context)
    return context

@when(parse("I wait for '{seconds}' seconds"))
def step_when_wait_seconds(context: Context, seconds: str) -> Context:
    import time
    time.sleep(int(seconds))
    return context

@then(parse("the money count is '{expected_money}'"))
def step_then_check_money(context: Context, expected_money: str) -> Context:
    clicker_page = clickerPage()
    clicker_page.checkCurrentMoney(expected_money, context)
    return context

@then(parse("the cookie count is '{expected_score}'"))
def step_then_check_cookies(context: Context, expected_score: str) -> Context:
    clicker_page = clickerPage()
    clicker_page.checkCurrentCookies(int(expected_score), context)
    return context

@then(parse("the factory count is '{expected_factories}'"))
def step_then_check_factories(context: Context, expected_factories: str) -> Context:
    clicker_page = clickerPage()
    clicker_page.checkCurrentFactories(int(expected_factories), context)
    return context

@then(parse("the score of '{username}' is '{expected_score}'"))
def step_then_check_user_score(context: Context, username: str, expected_score: str) -> Context:
    home_page = homePage()
    home_page.checkUserExists(username, context)
    home_page.checkUserScore(username, int(expected_score), context)
    return context

@then("I close the browser")
def step_then_search_results(context: Context) -> Context:
    context.closeBrowser()
    return context
