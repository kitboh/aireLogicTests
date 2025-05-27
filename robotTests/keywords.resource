*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           SeleniumLibrary
Library           CustomLibrary.py


*** Keywords ***
Create User
   [Arguments]    ${test_user}
    Input Text    name=name    ${test_user}
    Click Button    locator=Start!

Login as Test User
    Create User    Test_User
    Page Should Contain    text=Hello Test_User

Add Cookies
      [Arguments]    ${number_of_cookies}
      FOR    ${element}    IN RANGE     0    ${number_of_cookies}
         Click Button    Click Cookie!   
         Sleep    50ms       
      END

Sell Cookies
    [Arguments]    ${number_of_cookies}
    Input Text    cookies-to-sell    ${number_of_cookies}
    Click Button    sell-cookies

Buy Factories
    [Arguments]    ${number_of_factories}
    Input Text    factories-to-buy    ${number_of_factories}
    Click Button    buy-factories