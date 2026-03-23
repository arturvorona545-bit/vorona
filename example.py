import time
import os.path
from selenium import webdriver
from cookies_manager import CookieManager

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")
time.sleep(2)

cookie_manager = CookieManager(driver)

if os.path.exists("cookies.json"):
    cookie_manager.load()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("artur.vorona.99@list.ru")
    driver.find_element(*PASSWORD_FIELD).send_keys("45312569")
    driver.find_element(*SUBMIT_BUTTON).click()
    time.sleep(5)
    cookie_manager.save()

time.sleep(5)
driver.quit()