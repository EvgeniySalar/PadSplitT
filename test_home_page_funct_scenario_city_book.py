import pytest

from home_page_city_book import HomePageScr

from mainpage_scenario_city_book import MainPagescr




class TestSiteFuncScr:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        self.home_page = HomePageScr(chrome_drv)
        self.main_page = MainPagescr(chrome_drv)
        yield chrome_drv

    def test_click_on_city_field(self):
        self.home_page.city_field_element_click()
        self.main_page.citys_field_is_clicked()

    def test_join_button_click(self):
        self.home_page.city_join_button()
        self.main_page.city_field_join_is_clicked()

    def test_popup_close(self):
        self.home_page.city_close_element_click()
        self.main_page.city_pop_close()

 

