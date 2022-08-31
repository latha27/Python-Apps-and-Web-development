from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/Jay/Python/venv/Lib/site-packages/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName').send_keys("latha")
last_name = driver.find_element(By.NAME, 'lName').send_keys("ss")
email = driver.find_element(By.NAME, 'email').send_keys("email@gmail.com")

driver.find_element(By.CSS_SELECTOR, 'form button').click()
driver.quit()