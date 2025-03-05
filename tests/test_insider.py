import pytest

from enums.departments import Departments
from enums.locations import Locations
from pages.careers_page import CareersPage
from pages.home_page import HomePage
from utils.urls.career_urls import QA_URL, QA_POSITIONS_URL, LEVER_URL


@pytest.mark.usefixtures("driver_setup")
class TestInsiderCareers:
    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.careers_page = CareersPage(self.driver, timeout=30)

    def test_careers_page(self, accept_cookies):
        assert self.home_page.is_home_page_opened(), "Home page did not load"
        self.home_page.accept_cookies()
        self.home_page.select_careers()
        assert self.careers_page.is_teams_opened(), "Teams section is not opened"
        assert self.careers_page.is_locations_opened(), "Locations section is not opened"
        assert self.careers_page.is_life_opened(), "Life at Insider section is not opened"

    def test_qa_careers(self, accept_cookies):
        self.careers_page.go_to(QA_URL)
        self.careers_page.click_see_qa_jobs_button()
        self.careers_page.filter_by_location(Locations.Istanbul.value)
        self.careers_page.filter_by_department(Departments.QA.value)
        assert self.careers_page.is_positions_list_present(), "Positions list is absent"
        assert self.careers_page.does_positions_have_str_in_locations(Locations.Istanbul.value), \
            "Location is absent or incorrect"
        assert self.careers_page.does_positions_have_str_in_department(Departments.QA.value), \
            "Department is absent or incorrect"
        assert self.careers_page.does_positions_have_str_in_title(Departments.QA.value),\
            "Title is absent or incorrect"

    def test_application_redirect(self, accept_cookies):
        self.careers_page.go_to(QA_POSITIONS_URL)
        self.careers_page.scroll_filter_into_view()
        self.careers_page.hover_first_position()
        self.careers_page.click_view_role_button()
        self.careers_page.switch_tab(1)
        try:
            assert self.careers_page.does_url_contain(LEVER_URL), "Lever is not present in url"
        finally:
            self.careers_page.close_current_tab()
            self.careers_page.switch_tab(0)

