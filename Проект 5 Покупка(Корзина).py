import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--start-maximized")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
# Открываем сайт
driver.get("https://www.saucedemo.com")
time.sleep(2)


# Логин пароль
username = driver.find_element("xpath", "//input[@id='user-name']")
username.send_keys("standard_user")
password = driver.find_element("xpath", "//input[@id='password']")
password.send_keys("secret_sauce")

login_button = driver.find_element ("xpath", "//input[@id='login-button']")
login_button.click()
time.sleep(5)

# Заассертим, что мы на главной странице магазина
assert "inventory.html" in driver.current_url, "Не удалось войти в магазин"
assert len(driver.find_elements(By.CLASS_NAME, "inventory_item")) > 0, "Товары не загрузились"

# Добавляем товары в корзину
Cart1 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
Cart1.click()
time.sleep(2)
Cart2 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
Cart2.click()
time.sleep(2)

# Проверим товары в корзине
cart_badge = driver.find_element("xpath", "//span[@class='shopping_cart_badge']")
assert cart_badge.text == "2"

# Перейдем в корзину
cart_button = driver.find_element("xpath", "//a[@class='shopping_cart_link']")
cart_button.click()
time.sleep(2)

# Кликаем кнопку Checkout
checkout = driver.find_element("xpath", "//button[@id='checkout']")
checkout.click()
time.sleep(2)

#Заполняем поля для отправки
first_name = driver.find_element("xpath", "//input[@id='first-name']")
first_name.send_keys("Артур")

last_name = driver.find_element("xpath", "//input[@id='last-name']")
last_name.send_keys("Ворона")
postal_code = driver.find_element("xpath", "//input[@id='postal-code']")
postal_code.send_keys("353739")
time.sleep(2)

# Жмем продолжить
continue_button = driver.find_element("xpath", "//input[@id='continue']")
continue_button.click()
time.sleep(1)

# Жмем  кнопку Finish
finish_button = driver.find_element("xpath", "//button[@id='finish']")
finish_button.click()
time.sleep(2)

# Жмем кнопку вернуться домой
back_home = driver.find_element("xpath", "//button[@id='back-to-products']")
back_home.click()
time.sleep(2)