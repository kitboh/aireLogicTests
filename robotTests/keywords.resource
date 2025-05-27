*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           SeleniumLibrary
Library           CustomLibrary.py


*** Keywords ***
Test
   [Arguments]    ${url}
    Open Browser    ${url}    Firefox
    Maximize Browser Window
    Click Button    input