from selenium.webdriver.support.wait import WebDriverWait

from helpers.ui_helper import UI_Helper
from pages.base_page import BasePage


class TwitchStreamPage(BasePage):

    def wait_for_steam_to_load(self):
        WebDriverWait(self.driver, 10).until(lambda d: UI_Helper.is_video_playing(d))
