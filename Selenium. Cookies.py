
import json
import time
from selenium import webdriver

from Функции import add

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Вводим данные

 driver.find_element(*LOGIN_FIELD).send_keys("artur.vorona.99@list.ru")
 driver.find_element(*PASSWORD_FIELD).send_keys("45312569")
 driver.find_element(*SUBMIT_BUTTON).click()

time.sleep(5)
cookies = driver.get_cookies()

with open("cookies.json", "w") as file:
    json.dump(cookies, file, indent=4)

with open("cookies.txt", "r") as file:
    cookies = json.load(file)
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(8)