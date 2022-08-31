*** settings ***
Library  SeleniumLibrary

*** variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
LoginTest
    Open Browser    ${url}   ${browser}
    loginToApplication
    Close Browser

*** Keywords ***
loginToApplication
    Click Link    xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    Input Text    id:Email    pavanoltraining@gmail.com
    Input Text    id:Password    Test@123
    Click Element    xpath:/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button




