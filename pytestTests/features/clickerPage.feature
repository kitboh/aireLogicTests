# features/clickerPage.feature
Feature: Clicker functionality on a website

    @clicker_page @full_suite
    Scenario: A single click adds 1 to the score
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        And I click the cookie
        Then the cookie count is '1'
        And I close the browser

    @clicker_page @full_suite
    Scenario: 2 clicks will show a score of 2
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        And I click the cookie
        And I click the cookie
        Then the cookie count is '2'
        And I close the browser

# This is ignoring the bug where you cannot sell your last cookie
    @clicker_page @sale_tests @full_suite
    Scenario: A user can sell a cookie
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        And I click the cookie
        And I click the cookie
        And I sell '1' cookie
        Then the cookie count is '1'
        And the money count is '0.25'
        And I close the browser