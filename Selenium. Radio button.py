import time
from selenium import webdriver


YES_RADIO_BUTTON =("xpath", "//input[@id='yesRadio']")
IMPRESSIVE_RADIO_BUTTON =("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON =("xpath", "//input[@id='noRadio']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

driver.find_element(*IMPRESSIVE_RADIO_BUTTON).click()
time.sleep(5)