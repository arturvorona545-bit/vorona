import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")


dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))
dropdown.select_by_visible_text("Option 2")
time.sleep(2)