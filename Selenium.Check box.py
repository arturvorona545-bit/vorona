import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
checkbox = driver.find_element("xpath", "//span[@class='rc-tree-checkbox' ]")

checkbox.click()
time.sleep(5)