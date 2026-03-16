import time
from selenium import webdriver
# Настройка браузера

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Инициализация браузера
driver = webdriver.Chrome(options=options)
driver.get ("https://ya.ru")
print(driver.title)
time.sleep(2)