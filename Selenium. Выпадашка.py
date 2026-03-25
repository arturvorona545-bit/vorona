import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu")
wait = WebDriverWait(driver, 10,1)
action = ActionChains(driver)

STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")


SET_1 = driver.find_element(*STEP_1_LOCATOR)
SET_2 = driver.find_element(*STEP_2_LOCATOR)
SET_3 = driver.find_element(*STEP_3_LOCATOR)

action.move_to_element(SET_1).move_to_element(SET_2).move_to_element(SET_3).perform()


time.sleep(5)







