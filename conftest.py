from datetime import datetime
import os.path

import pytest

from config import BASE_URL
from framework.browser import Browser


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = Browser()
    driver = browser.get_browser()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def take_screenshot(request):
    def _take_screenshot():
        test_name = request.node.name
        screenshots_folder = f"screenshots/{test_name}"
        os.makedirs(screenshots_folder, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{time_stamp}.png"
        request.cls.driver.save_screenshot(os.path.join(screenshots_folder, file_name))
    return _take_screenshot
