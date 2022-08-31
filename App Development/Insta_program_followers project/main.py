import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:/Users/Jay/Python/venv/Scripts/chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "lathassjay"
PASSWORD = "Soppinahally@27"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.essential_cookies = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        self.essential_cookies.click()

        time.sleep(5)
        self.username = self.driver.find_element(By.NAME, "username")
        self.password = self.driver.find_element(By.NAME, "password")
        self.username.send_keys(USERNAME)
        self.password.send_keys(PASSWORD)

        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        self.login_button.click()
        time.sleep(3)

        self.save_info = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        self.save_info.click()
        time.sleep(3)

        self.turn_on_notification = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        self.turn_on_notification.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
            '//*[@id="mount_0_0_ru"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()