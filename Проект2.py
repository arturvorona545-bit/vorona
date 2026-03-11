import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/key_presses")

# Поле, которое должно быть в фокусе для нажатия клавиш
input_field = driver.find_element("xpath", "//input[@id='target']")
# Элемент, в котором отображается результат нажатия
result_field = driver.find_element("xpath", "//p[@id='result']")

# Кликаем по полю, чтобы оно стало активным
input_field.click()
time.sleep(1)

# Отправляем команду BACKSPACE
input_field.send_keys(Keys.BACKSPACE)
time.sleep(1)

# Получаем текст из элемента с результатом
result_text = result_field.text
print(f"Получен результат: '{result_text}'") # Для отладки

# Проверяем, что результат совпадает с ожидаемым для этого сайта
assert result_text == "You entered: BACK_SPACE", f"Ошибка! Ожидалось 'You entered: BACK_SPACE', получено '{result_text}'"