*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://app.qure.ai/
${BROWSER}   chrome
${USERNAME}  interview@mailinator.com
${PASSWORD}  Qure@12345

*** Test Cases ***
Valid User Can Login Successfully
    Open Browser    ${URL}    ${BROWSER}
    Click Button    class=Sign-up / Log-in via Email
    Input Text      id=email        ${USERNAME}
    Input Text      id=password     ${PASSWORD}
    Click Button    id=kc-login
    Title Should Be    Dashboard - Example.com
    Close Browser

*** Keywords ***
Wait Until Element Is Visible
    [Arguments]    ${locator}
    Wait Until Keyword Succeeds    5 times    1 second    Element Should Be Visible    ${locator}
