import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

first_name_filed = driver.find_element("xpath", "//input[@id='firstName']")
first_name_filed.clear()

first_name_filed.send_keys("Alex")


time.sleep(1)

#Задача 2 ввести значение в LastName
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

last_name_filed = driver.find_element("xpath", "//input[@id='lastName']")
last_name_filed.clear()
last_name_filed.send_keys("Vorona")

# Получаем значение из поля и сохраняем в переменную
field_value = last_name_filed.get_attribute("value")
# Проверяем, что оно пустое (равно пустой строке)
assert field_value == "Vorona"


#Задача 3 ввести значение Email
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
email_field =driver.find_element("xpath", "//input[@id='userEmail']")
email_field.clear()
email_field.send_keys("test@example.com")
field_value_email = email_field.get_attribute("value")
assert field_value_email == "test@example.com"

#Задача 4 ввести значение MOBILE NUMBER(10)
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
number_field = driver.find_element("xpath", "//input[@id='userNumber']")
number_field.clear()
number_field.send_keys("9876543210")
field_value_number = number_field.get_attribute("value")
assert field_value_number == "9876543210"


#Задача 5 ввести значение Current Address
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
current_address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address_field.send_keys("123 Main Street, Springfield")
field_value = current_address_field.get_attribute("value")
assert field_value == "123 Main Street, Springfield"
time.sleep(1)
