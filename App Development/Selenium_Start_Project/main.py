from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path ="C:/Users/Jay/Python/venv/Lib/site-packages/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

my_dict = {}

upcoming_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
upcoming_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

for n in range(len(upcoming_time)):
    my_dict[n] = {
               "time": upcoming_time[n].text,
               "name": upcoming_events[n].text
    }


print(my_dict)







driver.close()