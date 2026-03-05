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
time.sleep(1)

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
time.sleep(1)



