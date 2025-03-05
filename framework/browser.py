import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from config import DRIVER_NAME, PROJECT_PATH


class Browser:
    def __init__(self):
        self.driver_name = DRIVER_NAME
        self.drivers_path = os.path.join(PROJECT_PATH, "utils", "drivers")
        self.driver_path = os.path.join(self.drivers_path, self.driver_name)

    def get_browser(self):
        if self.driver_name == "chromedriver":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_service = ChromeService(str(self.driver_path))
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        elif self.driver_name == "geckodriver":
            firefox_options = webdriver.FirefoxOptions()
            firefox_service = FirefoxService(str(self.driver_path))
            driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
            driver.maximize_window()
        else:
            raise ValueError(f"Browser '{self.driver_name}' is not supported")
        return driver

