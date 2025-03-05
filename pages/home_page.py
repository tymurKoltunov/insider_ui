from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO_XPATH = (By.XPATH, "//h1")
    COMPANY_NAVBAR_XPATH = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    CAREERS_DROPDOWN_XPATH = (By.XPATH, "//a[@class='dropdown-sub' and contains(text(), 'Careers')]")

    def is_home_page_opened(self):
        try:
            self.wait.until(self.EC.visibility_of_element_located(self.LOGO_XPATH))
            return True
        except TimeoutError:
            return False

    def select_careers(self):
        company_nav = self.wait.until(self.EC.visibility_of_element_located(self.COMPANY_NAVBAR_XPATH))
        company_nav.click()
        careers_option = self.wait.until(self.EC.visibility_of_element_located(self.CAREERS_DROPDOWN_XPATH))
        careers_option.click()
