from selenium.webdriver.common.by import By

from helpers.ui_helper import UI_Helper


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    ACCEPT_COOKIES_BUTTON_XPATH = (By.XPATH, "//button[@data-a-target='consent-banner-accept']")
    BROWSE_BUTTON_XPATH = (By.XPATH, "//a[@href='/directory']//div[contains(text(),'Browse')]")

    def accept_cookies(self):
        button = UI_Helper.wait_for_element_to_be_visible(self.driver, self.ACCEPT_COOKIES_BUTTON_XPATH)
        button.click()

    def click_browse_button(self):
        button = UI_Helper.wait_for_element_to_be_visible(self.driver, self.BROWSE_BUTTON_XPATH)
        button.click()

    def scroll_screen(self):
        screen_height = self.driver.get_window_size()['height']
        self.driver.execute_script(f"window.scrollBy(0,{screen_height})")

