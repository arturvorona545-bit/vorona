import time
from selenium import webdriver
# Настройка браузера

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Инициализация браузера
driver = webdriver.Chrome(options=options)
driver.get ("https://ya.ru")
print(driver.title)
#time.sleep(1)


# Запуск в режиме инкогнито

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get ("https://ya.ru")
print(driver.title)
#time.sleep(1)

# Игнорирование SSL-ошибок (--ignore-certificate-errors)

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=options)
driver.get ("https://ya.ru")
print(driver.title)
#time.sleep(1)


#Установка размера окна (--window-size=X,Y)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get ("https://krasnodar.velo-shop.ru/")
print(driver.title)
#time.sleep(1)



# Отключение кэширования (--disable-cache)

options = webdriver.ChromeOptions()
options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=options)
driver.get ("https://ya.ru")
print(driver.title)


#Пример комплексной настройки:
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-cache")
# options.add_argument("--no-sandbox")
#
# driver = webdriver.Chrome(options=options)


from selenium import webdriver
river = webdriver.Chrome(options=options)
driver.get ("https://krasnodar.velo-shop.ru/")
print(driver.title)

from selenium import webdriver
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get ("https://krasnodar.velo-shop.ru/")

from selenium import webdriver
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.get ("https://krasnodar.velo-shop.ru/")