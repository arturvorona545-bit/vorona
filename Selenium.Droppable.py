import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

# Убеждаемся, что вкладка "Simple" активна
try:
    # Проверяем, есть ли вкладка "Simple" и кликаем по ней если нужно
    simple_tab = wait.until(EC.element_to_be_clickable((By.ID, "droppableExample-tab-simple")))
    simple_tab.click()
    time.sleep(1)
except:
    pass  # Если вкладка уже активна, игнорируем ошибку

# source - это то, что мы перетягиваем
# target - это то, куда мы перетягиваем
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

# Ожидаем появления элементов
SOURCE = wait.until(EC.presence_of_element_located(SOURCE_LOCATOR))
TARGET = wait.until(EC.presence_of_element_located(TARGET_LOCATOR))

# Выполняем drag and drop
action.drag_and_drop(SOURCE, TARGET).perform()

# Проверяем результат
time.sleep(2)

