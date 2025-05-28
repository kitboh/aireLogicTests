# features/factories.feature
Feature: Factory functionality on cookie clicker

# This one can be inconsistent due to latency. TODO: Add waits based on criteria
    @clicker_page @factory_tests @full_suite
    Scenario: A user can purchase a factory
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        And I click the cookie '21' times
        And I sell '20' cookie
        Then the money count is '5'
        When I purchase '1' factory
        When I wait for '5' seconds
        Then the factory count is '1'
        And the cookie count is '5'
        And the money count is '2'
        And I close the browser

# This is failing due to a bug where the user can purchase a factory with no money
    @clicker_page @factory_tests @full_suite
    Scenario: A user cannot purchase a factory with no money
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        Then the cookie count is '0'
        When I purchase '1' factory
        Then the factory count is '0'
        And I close the browser

# This is failing due to a bug where on the first refresh, the users money shows as 0.0 and other times as 0
    @clicker_page @factory_tests @full_suite
    Scenario: A user cannot sell a factory
        Given the user opens the homepage
        When a user is created with the name 'Test_User'
        And I purchase '-1' factory
        Then the money count is '0'
        And the factory count is '0'
        And I close the browser