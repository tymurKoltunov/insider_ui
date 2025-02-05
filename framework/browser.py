import os

from pytest_selenium.drivers.chrome import chrome_service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config import DRIVER_NAME, PROJECT_PATH, MOBILE_DEVICE_NAME


class Browser:
    def __init__(self):
        self.driver_name = DRIVER_NAME
        self.drivers_path = os.path.join(PROJECT_PATH, "utils", "drivers")
        self.chrome_driver_path = os.path.join(self.drivers_path, self.driver_name)

    def get_chrome_options(self):
        chrome_options = Options()
        mobile_emulation = {"deviceName": MOBILE_DEVICE_NAME}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        return chrome_options

    def get_browser(self):
        chrome_options = self.get_chrome_options()
        chrome_service = Service(str(self.chrome_driver_path))
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        return driver

