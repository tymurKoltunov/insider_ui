from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from helpers.ui_helper import UI_Helper
from pages.base_page import BasePage


class TwitchBrowsePage(BasePage):
    SEARCH_INPUT_XPATH = (By.XPATH, "//input[@type='search']")
    CHANNELS_TAB_XPATH = (By.XPATH, "//a[@role='tab']//div[contains(text(), 'Channels')]")
    STREAM_XPATH = (By.XPATH, "//div[@role='list']//div//button")

    def search_for(self, text):
        search_input_el = UI_Helper.wait_for_element_to_be_visible(self.driver, self.SEARCH_INPUT_XPATH)
        search_input_el.send_keys(text)
        search_input_el.send_keys(Keys.ENTER)

    def select_channels_tab(self):
        tab = UI_Helper.wait_for_element_to_be_visible(self.driver, self.CHANNELS_TAB_XPATH)
        tab.click()
        UI_Helper.wait_for_element_to_be_visible(self.driver, self.STREAM_XPATH)

    def select_first_visible_streamer(self):
        visible_streamers = UI_Helper.get_visible_elements(self.driver, self.STREAM_XPATH)
        visible_streamers[0].click()
