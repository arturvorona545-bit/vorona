from selenium import webdriver


class TestExample:

    # Locators

    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    OUTPUT_BLOCK = ("xpath", "//div[@id='output']")
    CLOSE_BANNER = ("xpath", "//*[@id='close-fixedban']/img")

    # Тестовый метод (Тест)

    def test_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Artur")
        assert username.get_attribute("value") == "Artur"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("aqa112@gmail.com")
        assert email.get_attribute("value") == "aqa112@gmail.com"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Komandorskaya 6")
        assert address.get_attribute("value") == "Komandorskaya 6"

        submit_button = driver.find_element(*self.SUBMIT_BUTTON)
        driver.execute_script("arguments[0].click();", submit_button)

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        output_text = output.text
        assert "Artur" in output_text
        assert "aqa112@gmail.com" in output_text
        assert "Komandorskaya 6" in output_text