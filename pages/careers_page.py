import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersPage(BasePage):
    TEAMS_XPATH = (By.XPATH, "//div[contains(@class, 'job-item')]")
    LOCATIONS_XPATH = (By.XPATH, "//div[@id='location-slider']")
    LIFE_AT_INSIDER_CAROUSEL_XPATH = (By.XPATH, "//div[@class='elementor-swiper']")
    SEE_QA_JOBS_BUTTON_XPATH = (By.XPATH, "//a[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance']")
    FILTER_BY_LOCATION_DROPDOWN_XPATH = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    FILTER_BY_DEPARTMENT_DROPDOWN_XPATH = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    LOCATION_OPTION_XPATH = "//li[contains(@id, '{}')]"
    DEPARTMENT_OPTION_XPATH = "//li[contains(@id, '{}')]"
    CAREER_POSITIONS_LIST_XPATH = (By.XPATH, "//div[@id='jobs-list']")
    POSITIONS_TITLES_XPATH = (By.XPATH, "//p[contains(@class, 'position-title')]")
    POSITIONS_DEPARTMENTS_XPATH = (By.XPATH, "//span[contains(@class, 'position-department')]")
    POSITIONS_LOCATIONS_XPATH = (By.XPATH, "//div[contains(@class, 'position-location')]")
    FIRST_POSITION_IN_LIST_XPATH = (By.XPATH, "(//div[contains(@class, 'position-list-item-wrapper')])[1]")
    FIRST_POSITION_VIEW_ROLE_BUTTON_XPATH = (By.XPATH, "(//div[contains(@class, 'position-list-item-wrapper')])[1]//a")
    BROWSE_HEADER_XPATH = (By.XPATH, "//h3[contains(normalize-space(),'Browse Open Positions')]")
    FILTER_DROPDOWN_OPTIONS_XPATH = (By.XPATH, "//li[contains(@class, 'select2-results__option')]")

    def is_teams_opened(self):
        try:
            team_items = self.wait.until(self.EC.visibility_of_all_elements_located(self.TEAMS_XPATH))
            return len(team_items) > 0
        except TimeoutError:
            return False

    def is_locations_opened(self):
        try:
            self.wait.until(self.EC.visibility_of_element_located(self.LOCATIONS_XPATH))
            return True
        except TimeoutError:
            return False

    def is_life_opened(self):
        try:
            self.wait.until(self.EC.visibility_of_element_located(self.LIFE_AT_INSIDER_CAROUSEL_XPATH))
            return True
        except TimeoutError:
            return False

    def click_see_qa_jobs_button(self):
        button = self.wait.until(self.EC.visibility_of_element_located(self.SEE_QA_JOBS_BUTTON_XPATH))
        button.click()

    def filter_by_location(self, location):
        retries = 20
        current_try = 0
        dropdown = self.wait.until(self.EC.visibility_of_element_located(self.FILTER_BY_LOCATION_DROPDOWN_XPATH))
        self.scroll_element_into_view(dropdown)
        if dropdown.get_attribute("title") != location:
            while retries > current_try:
                dropdown.click()
                options = self.wait.until(self.EC.visibility_of_all_elements_located(self.FILTER_DROPDOWN_OPTIONS_XPATH))
                if len(options) > 1:
                    break
                dropdown.click()
                current_try += 1
                time.sleep(1)
            option = self.wait.until(self.EC.visibility_of_element_located(
                (By.XPATH, self.LOCATION_OPTION_XPATH.format(location))))
            option.click()

    def filter_by_department(self, department):
        dropdown = self.wait.until(self.EC.visibility_of_element_located(self.FILTER_BY_DEPARTMENT_DROPDOWN_XPATH))
        if dropdown.get_attribute("title") != department:
            dropdown.click()
            option = self.wait.until(self.EC.visibility_of_element_located(
                (By.XPATH, self.DEPARTMENT_OPTION_XPATH.format(department))))
            option.click()

    def is_positions_list_present(self):
        try:
            self.wait.until(self.EC.visibility_of_element_located(self.CAREER_POSITIONS_LIST_XPATH))
            return True
        except TimeoutError:
            return False

    def does_positions_have_str_in_title(self, title_to_check):
        titles = self.wait.until(self.EC.visibility_of_all_elements_located(self.POSITIONS_TITLES_XPATH))
        return all(title_to_check in title.text for title in titles)

    def does_positions_have_str_in_department(self, department_to_check):
        deps = self.wait.until(self.EC.visibility_of_all_elements_located(self.POSITIONS_DEPARTMENTS_XPATH))
        return all(department_to_check in dep.text for dep in deps)

    def does_positions_have_str_in_locations(self, location_to_check):
        locs = self.wait.until(self.EC.visibility_of_all_elements_located(self.POSITIONS_LOCATIONS_XPATH))
        return all(location_to_check in loc.text for loc in locs)

    def hover_first_position(self):
        position = self.wait.until(self.EC.visibility_of_element_located(self.FIRST_POSITION_IN_LIST_XPATH))
        self.hover_over_element(position)

    def click_view_role_button(self):
        button = self.wait.until(self.EC.visibility_of_element_located(self.FIRST_POSITION_VIEW_ROLE_BUTTON_XPATH))
        button.click()

    def scroll_filter_into_view(self):
        header = self.wait.until(self.EC.visibility_of_element_located(self.FILTER_BY_LOCATION_DROPDOWN_XPATH))
        self.scroll_element_into_view(header)


