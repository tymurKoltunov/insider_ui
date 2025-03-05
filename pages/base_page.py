import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_TIMEOUT
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=BASE_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)
        self.EC = EC

    ACCEPT_COOKIES_BUTTON_XPATH = (By.XPATH, "//a[@id='wt-cli-accept-all-btn']")

    def accept_cookies(self):
        try:
            button = self.wait.until(self.EC.visibility_of_element_located(self.ACCEPT_COOKIES_BUTTON_XPATH))
            button.click()
        except Exception:
            return False

    def go_to(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def switch_tab(self, index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[index])

    def close_current_tab(self):
        self.driver.close()

    def does_url_contain(self, text):
        return text in self.driver.current_url

    def scroll_element_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    def hover_over_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
