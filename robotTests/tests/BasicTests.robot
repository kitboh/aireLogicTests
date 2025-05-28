*** Settings ***
Documentation     A test suite for basic functionality of the Cookie Clicker site.
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
Check site can be loaded
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be  ${EXPECTED_TITLE}
    [Teardown]    Close Browser

Check a user can be created
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Create User    ${USER_NAME}
    Title Should Be  ${EXPECTED_TITLE}
    Page Should Contain    text=Hello ${USER_NAME}
    [Teardown]    Close Browser

Check clicking a cookie increments counter
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Click Button    Click Cookie!
    Element Text Should Be    cookies    1
    [Teardown]    Close Browser

# This one currently fails due to a bug
Sell a cookie and ensure payment is received
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Click Button    Click Cookie!
    Input Text    cookies-to-sell    1
    Click Button    sell-cookies
    Element Text Should Be    cookies    0
    Element Text Should Be    money    0.25
    [Teardown]    Close Browser

Working version of the above
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Login as Test User
    Add Cookies    2
    Input Text    cookies-to-sell    1
    Click Button    sell-cookies
    Element Text Should Be    cookies    1
    Element Text Should Be    money    0.25
    [Teardown]    Close Browser
