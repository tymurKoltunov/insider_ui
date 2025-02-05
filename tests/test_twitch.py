import pytest

from pages.twitch_browse_page import TwitchBrowsePage
from pages.twitch_stream_page import TwitchStreamPage


@pytest.mark.usefixtures("driver_setup")
class TestTwitch:
    def setup_method(self):
        self.browse_page = TwitchBrowsePage(self.driver)
        self.stream_page = TwitchStreamPage(self.driver)

    def test_starcraft_search(self, take_screenshot):
        self.browse_page.accept_cookies()
        self.browse_page.click_browse_button()
        self.browse_page.search_for("StarCraft II")
        self.browse_page.select_channels_tab()
        self.browse_page.scroll_screen()
        self.browse_page.scroll_screen()
        self.browse_page.select_first_visible_streamer()
        self.stream_page.wait_for_steam_to_load()
        take_screenshot()
