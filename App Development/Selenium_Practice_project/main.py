from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Jay/Python/venv/Lib/site-packages/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

data = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(data.text)

driver.quit()