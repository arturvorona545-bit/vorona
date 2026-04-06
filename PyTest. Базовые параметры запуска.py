from selenium import webdriver

class TestExample:

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")  # исправлено: https и demoqa
        assert driver.current_url == "https://demoqa.com/login", "открыта некорректная страница"
        driver.quit()

    def test_login2(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")  # исправлено: https и demoqa
        assert driver.current_url == "https://demoqa.com/login", "открыта некорректная страница"
        driver.quit()
