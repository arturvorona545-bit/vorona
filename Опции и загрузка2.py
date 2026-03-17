import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

FILE_UPLOAD_FILED =("xpath", "//input[@id='uploadFile']")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

#Загрузка файла-пример

file_field = driver.find_element(*FILE_UPLOAD_FILED)
file_field.send_keys(r"C:\user\PycharmProjects\PythonProject\vorona\example.jpeg")
time.sleep(2)