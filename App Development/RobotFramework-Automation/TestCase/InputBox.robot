*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store
    Click Link    xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    ${"email_txt"}  Set Variable    id:Email
    Element Should Be Visible    ${"email_txt"}
    Element Should Be Enabled    ${"email_txt"}
    Input Text    ${"email_txt"}    JhonDavid@gmail.com
    sleep   5
    Clear Element Text    ${"email_txt"}
    Sleep    5
    Close Browser

*** Keywords ***