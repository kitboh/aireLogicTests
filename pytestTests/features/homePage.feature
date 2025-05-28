# features/homePage.feature
Feature: Search functionality on a website

    @home_page @full_suite
    Scenario: I can create a new user
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        Then I close the browser

# Technically this isn't a good test when running in parallel, but works when run sequentially
    @home_page @full_suite
    Scenario: A new user has 0 score
        Given the user opens the homepage
        Then the score of 'Test_User' is '0'
        Then I close the browser