from datetime import datetime
import os.path

import pytest

from config import BASE_URL
from framework.browser import Browser
from pages.base_page import BasePage


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = Browser()
    driver = browser.get_browser()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_test_fail(request, take_screenshot):
    yield
    if request.node.rep_call.failed or request.node.rep_setup.failed:
        try:
            take_screenshot()
        except Exception as e:
            print(f"Screenshot failed. Error - {e}")


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


@pytest.fixture(scope="function")
def accept_cookies(request):
    page = BasePage(request.cls.driver, timeout=3)
    page.accept_cookies()
