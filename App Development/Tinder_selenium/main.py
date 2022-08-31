from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import time

chrome_driver_path = "C:/Users/Jay/Python/venv/Lib/site-packages/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://tinder.com/app/recs")

time.sleep(2)
login = driver.find_element(By.XPATH, "//*[@id='s2097736098']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, "//*[@id='s369355022']/div/div/div[1]/div/div/div[3]/span/div[2]/button")
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)
email_id = driver.find_element(By.ID, "email")
email_id.send_keys("lathaec8@gmail.com")

time.sleep(2)
password = driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys("Latha@27")

login_button = driver.find_element(By.NAME, "login")
login_button.click()

allow_location_access = driver.find_element(By.XPATH, "//*[@id='s369355022']/div/div/div/div/div[3]/button[1]")
allow_location_access.click()

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
