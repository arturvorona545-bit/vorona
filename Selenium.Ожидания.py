from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver, 10,poll_frequency=1)

VISIBLE_AFTER_BUTTON = ("xpath","//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))