from home_page_city_book import HomePageScr


class MainPagescr(HomePageScr):

    def citys_field_is_clicked(self):
        assert self.city_popup_element().is_enabled(), "Field is not clicked"
        print("Field is clicked")

    def city_field_join_is_clicked(self):
        assert self.city_popup_join().is_displayed(), "JOin field is not clicked"
        print("JOin Field is clicked")

    def city_pop_close(self):
        assert self.city_popup_close().is_displayed(), "Pop up is not closed"
        print("Pop up is closed")


