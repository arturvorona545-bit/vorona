from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Настройка опций
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--start-maximized')  # Добавляем максимизацию окна
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.page_load_strategy = 'normal'

# Создаем драйвер
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Максимизируем окно для лучшей видимости
driver.maximize_window()

try:
    driver.get("https://demoqa.com")
    time.sleep(2)

    # Скроллим вниз, чтобы элемент стал видимым
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

    # Функция для безопасного клика
    def safe_click(element_locator):
        try:
            element = wait.until(EC.element_to_be_clickable(element_locator))
            # Пробуем кликнуть через ActionChains
            action.move_to_element(element).click().perform()
            return True
        except ElementClickInterceptedException:
            # Если перехвачено, скроллим к элементу и кликаем через JS
            element = driver.find_element(*element_locator)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", element)
            return True
        except Exception as e:
            return False

    # Переходим в раздел "Elements"
    ELEMENTS = ("xpath", "//div[@class='card-body']")
    if safe_click(ELEMENTS):
        pass  # Добавляем pass, если ничего не нужно делать
    time.sleep(2)

    # Переходим в подраздел "Text Box"
    TEXT_BOX = ("xpath", "//span[@class='text']")
    if safe_click(TEXT_BOX):
        pass
    time.sleep(2)

    # Переходим к разделу заполнения полей
    # Используем wait для полей
    full_name_field = wait.until(EC.presence_of_element_located(("xpath", "//input[@id='userName']")))
    full_name_field.clear()
    full_name_field.send_keys("Артур Ворона")
    assert "Артур Ворона" in full_name_field.get_attribute("value")

    email_field = wait.until(EC.presence_of_element_located(("xpath", "//input[@type='email']")))
    email_field.clear()
    email_field.send_keys("Artur.vorona@list.ru")
    assert "Artur.vorona@list.ru" in email_field.get_attribute("value")  # Исправлено: проверяем правильный email

    current_address = wait.until(EC.presence_of_element_located(("xpath", "//textarea[@id='currentAddress']")))
    current_address.clear()
    current_address.send_keys("Краснодар, улица Командорская 6.")
    assert "Краснодар, улица Командорская 6." in current_address.get_attribute("value")

    permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
    permanent_address.clear()
    permanent_address.send_keys("Краснодарский Край, Калининский район, Гривенская.")
    assert "Краснодарский Край, Калининский район, Гривенская." in permanent_address.get_attribute("value")
    time.sleep(2)

    # Переход к разделу по загрузке файлов
    UPLOAD = ("xpath", "//span[text()='Upload and Download']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", driver.find_element(*UPLOAD))
    time.sleep(1)
    if safe_click(UPLOAD):
        pass
    time.sleep(2)

    # Загрузка файла
    FILE_CRED = ("xpath", "//input[@id='uploadFile']")
    upload_element = wait.until(EC.presence_of_element_located(FILE_CRED))
    # Используем абсолютный путь (убедитесь, что файл существует)
    upload_element.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")
    time.sleep(2)

    # Переход к динамическим элементам
    DYNAMIC_P = ("xpath", "//span[text()='Dynamic Properties']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", driver.find_element(*DYNAMIC_P))
    time.sleep(1)
    if safe_click(DYNAMIC_P):
        pass

    # Работа с динамическими элементами
    wait = WebDriverWait(driver, 30, poll_frequency=1)
    ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='enableAfter']")
    DELETE_BUTTON = ("xpath", "//button[@id='visibleAfter']")

    wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))
    driver.find_element(*ADD_ELEMENT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

    time.sleep(2)

    # Работа с Alert
    ALERTS_DIV = ("xpath", "//div[contains(@class, 'header-text') and contains(text(), 'Alerts, Frame & Windows')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", driver.find_element(*ALERTS_DIV))
    time.sleep(1)
    if safe_click(ALERTS_DIV):
        pass
    time.sleep(2)

    ALERTS_TAB = ("xpath", "//span[text()='Alerts']")
    if safe_click(ALERTS_TAB):
        pass
    time.sleep(2)

    # Alert с подтверждением
    alert_button = wait.until(EC.element_to_be_clickable(("xpath", "//button[@id='alertButton']")))
    alert_button.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    time.sleep(1)

    # Alert с таймером
    timer_button = driver.find_element("xpath", "//button[@id='timerAlertButton']")
    timer_button.click()
    alert = wait.until(EC.alert_is_present())
    time.sleep(1)
    alert.accept()
    time.sleep(1)

    # Alert с подтверждением/отменой
    confirm_button = driver.find_element("xpath", "//button[@id='confirmButton']")
    confirm_button.click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.dismiss()
    time.sleep(1)

    # Alert с вводом текста
    prompt_button = driver.find_element("xpath", "//button[@id='promtButton']")
    prompt_button.click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.send_keys("Iva.AQA")
    time.sleep(1)
    alert.accept()
    time.sleep(2)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(3)
    driver.quit()