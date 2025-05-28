*** Settings ***
Documentation     A test suite for basic functionality of the Factories functionality.
...
...               Keywords are imported from the resource file
Library          SeleniumLibrary
Resource         ../Keywords.resource
Default Tags      positive

*** Variables ***
# ${LOGIN URL}      https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
${LOGIN URL}      https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
${BROWSER}        Firefox
${EXPECTED_TITLE}    Cookie Clicker!
${SHOWN_VALUE}    0
${USER_NAME}    Test_User

*** Test Cases ***
Buy a factory and ensure it operates
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Add Cookies    21
    Sell Cookies    20
    Buy Factories    1
    Element Text Should Be    factories    1
    Element Text Should Be    money    2
    Wait Until Element Contains    cookies    4
    [Teardown]    Close Browser

Ensure a factory cannot be bought with no money
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Element Text Should Be    money    0.0
    Buy Factories    1
    Element Text Should Be    factories    0
    Element Text Should Be    money    0.0
    Page Should Contain    text=You do not have enough money to buy a factory!
    [Teardown]    Close Browser

Ensure a user cannot buy negative factories
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Element Text Should Be    money    0.0
    Buy Factories    -1
    Element Text Should Be    factories    0
    Element Text Should Be    money    0.0
    [Teardown]    Close Browser

Validate factory production speed
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Buy Factories    1
    Sleep    25ms
    Element Text Should Be    factories    1
    Sleep    5s
    Element Text Should Be    cookies    5
    [Teardown]    Close Browser