*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Library          SeleniumLibrary
Library          CustomLibrary.py
Resource         Keywords.resource
Default Tags      positive

*** Variables ***
${LOGIN URL}      https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
${BROWSER}        Firefox
${EXPECTED_TITLE}    Cookie Clicker!
${SHOWN_VALUE}    0

*** Test Cases ***
Check site can be loaded
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be  ${EXPECTED_TITLE}
    [Teardown]    Close Browser
