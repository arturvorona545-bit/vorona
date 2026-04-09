import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:

    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=chrome_options)

    @pytest.mark.smoke
    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        print("\n=== ТЕСТ 1 ===")
        print(f"URL: {self.driver.current_url}")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"
        print("✓ Тест пройден!")

    @pytest.mark.regression
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        print("\n=== ТЕСТ 2 ===")
        print(f"URL: {self.driver.current_url}")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка"
        print("✓ Тест пройден!")

    def teardown_method(self):
        self.driver.quit()
        print("Браузер закрыт")