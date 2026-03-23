import json
import os
from selenium.webdriver.chrome.webdriver import WebDriver

class CookieManager:
    def __init__(self, driver: WebDriver, file_path: str = "cookies.json"):
        self.driver = driver
        self.file_path = file_path

    def save(self) -> bool:
        cookies = self.driver.get_cookies()
        if cookies is None or len(cookies) == 0:
            return False

        with open(self.file_path, "w") as file:
            json.dump(cookies, file, indent=4)
        return True

    def load(self) -> bool:
        if not os.path.exists(self.file_path):
            return False

        with open(self.file_path, "r") as file:
            data = json.load(file)

        if data is None or not isinstance(data, list):
            return False

        self.driver.delete_all_cookies()

        for cookie in data:
            cookie_copy = cookie.copy()
            cookie_copy.pop('sameSite', None)

            try:
                self.driver.add_cookie(cookie_copy)
            except Exception:
                pass

        self.driver.refresh()
        return True