from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UI_Helper:
    @staticmethod
    def wait_for_element_to_be_visible(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def is_in_viewport(driver, element):
        return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    """, element)

    @staticmethod
    def get_visible_elements(driver, locator):
        all_elements = driver.find_elements(*locator)
        return [
            element for element in all_elements
            if UI_Helper.is_in_viewport(driver, element)
        ]

    @staticmethod
    def is_video_playing(driver):
        return driver.execute_script("""
        const video = document.querySelector('video');
        return video && 
               video.readyState === 4 && 
               !video.paused && 
               video.currentTime > 0;
    """)
