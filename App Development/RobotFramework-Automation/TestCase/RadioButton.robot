*** settings ***
Library  SeleniumLibrary

*** variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
Testing Radio Buttons and check Boxes
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
