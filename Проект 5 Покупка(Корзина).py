import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

username = driver.find_element("xpath", "//input[@id='user-name']")
username.send_keys("standard_user")
password = driver.find_element("xpath", "//input[@id='password']")
password.send_keys("secret_sauce")

login_button = driver.find_element ("xpath", "//input[@id='login-button']")
login_button.click()
time.sleep(5)