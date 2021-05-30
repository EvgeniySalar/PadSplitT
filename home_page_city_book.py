from base_page import BasePage
from locators_city_book import MainPageLocatorsSc2


class HomePageScr(BasePage):

    def city_field_element_click(self):
        city_field = self.get_element_present(*MainPageLocatorsSc2.GET_STARTED)
        city_field.click()

    def city_popup_element(self):
        city_popup = self.get_element_present(*MainPageLocatorsSc2.POP_UP_WINDOW)
        return city_popup

    def city_join_button(self):
        city_list = self.get_element_present(*MainPageLocatorsSc2.JOIN_AS_A_MEMBER)
        city_list.click()
        return city_list

    def city_popup_join(self):
        city_popup = self.get_element_present(*MainPageLocatorsSc2.POP_UP_WINDOW_N)
        return city_popup

    def city_close_element_click(self):
        city_field = self.get_element_present(*MainPageLocatorsSc2.CLOSE_POP_UP)
        city_field.click()

    def city_popup_close(self):
        city_popup = self.get_element_present(*MainPageLocatorsSc2.CLOSE_POP_UP_INDICATOR)
        return city_popup



