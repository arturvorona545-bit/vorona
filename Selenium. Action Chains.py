from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
wait = WebDriverWait(driver, 10,1)
action = ActionChains(driver)
action.click().perform()

DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
RIGHT_CLICK_BUTTON = ("xpath", "///button[@id='rightClickBtn']")
LEFT_CLICK_BUTTON = ("xpath", "///button[text()='Click Me']")

BUTTON = driver.find_element(*DOUBLE_CLICK_BUTTON)

action.double_click(BUTTON).perform()
time.sleep(5)