import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Нет плашки, которая говорит что мы бот.
# Настройка параметров ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])-доп.
#options.add_experimental_option('useAutomationExtension', False) - доп.
driver = webdriver.Chrome( options=options )
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

time.sleep(1)

                          #ALERT
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
driver.find_element("xpath", "//button[@id='promtButton']").click()

# Ожидание появления alert и запись элемента Alert в переменную
alert = driver.switch_to.alert
alert.send_keys("Arar")
time.sleep(4)

alert.dismiss()
print(alert)
time.sleep(4)


# # Ожидание появления alert и запись элемента Alert в переменную
# alert = wait.until(EC.alert_is_present())


