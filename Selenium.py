import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(1)
# --- 1. Full Name (First Name) ---
first_name_field = driver.find_element("xpath", "//input[@id='firstName']")
first_name_field.clear()
first_name_field.send_keys("Alex")
assert first_name_field.get_attribute("value") == "Alex"
time.sleep(1)
# --- 2. Last Name ---
last_name_field = driver.find_element("xpath", "//input[@id='lastName']")
last_name_field.clear()
last_name_field.send_keys("Vorona")
assert last_name_field.get_attribute("value") == "Vorona"
time.sleep(1)
# --- 3. Email ---
email_field = driver.find_element("xpath", "//input[@id='userEmail']")
email_field.clear()
email_field.send_keys("test@example.com")
assert email_field.get_attribute("value") == "test@example.com"
time.sleep(1)
# --- 4. Mobile Number ---
number_field = driver.find_element("xpath", "//input[@id='userNumber']")
number_field.clear()
number_field.send_keys("9876543210")
assert number_field.get_attribute("value") == "9876543210"
time.sleep(1)
# --- 5. Subjects ---
subject_field = driver.find_element("xpath", "//input[@id='subjectsInput']")
subject_field.click()
subject_field.clear()
subject_field.send_keys("RUSSIA")
assert subject_field.get_attribute("value") == "RUSSIA"

time.sleep(1)
# --- 6. Current Address ---
current_address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address_field.clear()
current_address_field.send_keys("123 Main Street, Springfield")
assert current_address_field.get_attribute("value") == "123 Main Street, Springfield"
time.sleep(1)
# 6. Демонстрация клавиш на Last Name
last_name_field.send_keys(Keys.BACKSPACE)  # Удаляем последнюю букву 'a'
assert last_name_field.get_attribute("value") == "Voron"


time.sleep(5)