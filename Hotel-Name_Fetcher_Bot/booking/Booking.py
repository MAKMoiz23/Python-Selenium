from booking.ReportResults import Reportresults
from booking.booking_filterations import bookingFilteration
from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.keys import Keys


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r';C:\driver_selenium', teardown= False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
            return super().__exit__(*args)

    def land_first_page(self):
        self.get(const.BASE_URL)

    def choose_currency(self, currency = None):
        def_curr = self.find_element_by_xpath('//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[1]/button')
        def_curr.click()

        sel_curr = self.find_elements_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency.upper()}"]'
            )
        sel_curr[0].click()

    def search_place_to_go(self, place_to_go):
        inp =  self.find_element_by_id("ss")
        inp.clear()
        inp.send_keys(place_to_go.capitalize())
        search = self.find_elements_by_xpath('//*[@id="frm"]/div[1]/div[4]/div[2]/button')
        search[0].click()
    
    def select_dates(self, chk_in_date, chk_out_date):
        if chk_in_date[4] != '-' and chk_in_date[7] != '-':
            print('Invalid date, should be yyyy-mm-dd')
            return
        elif chk_out_date[4] != '-' and chk_out_date[7] != '-':
            print('Invalid date, should be yyyy-mm-dd')
            return
        
        date_1 = self.find_elements_by_css_selector(f'td[data-date="{chk_in_date}"]')
        date_1[0].click()

        try:
            date_2 = self.find_elements_by_css_selector(f'td[data-date="{chk_out_date}"]')
            date_2[0].click()
        except:
            pass
    

    def select_adults_children_rooms(self, adults, childrens, ages, rooms):
        sel_adult = self.find_element_by_id("group_adults")
        sel_children = self.find_element_by_id("group_children")
        sel_rooms = self.find_element_by_id("no_rooms")

        sel_adult.click()
        for adult in range(1, adults-1):
            sel_adult.send_keys(Keys.ARROW_DOWN)

        sel_children.click()
        for child in range(childrens):
            sel_children.send_keys(Keys.ARROW_DOWN)
        
        sel_children.click()
        
        for c_no in range(1, len(ages)+1):
            sel_age = self.find_elements_by_css_selector(f'select[aria-label="Child {c_no} age"]')
            sel_age = sel_age[0]
            sel_age.click()
            age = ages[c_no-1]

            if age > 17 or age<0:
                print("Not a child :'(")
                continue

            elif age == 12:
                continue

            elif age >12:
                age -= 12
                for i in range(age):
                    sel_age.send_keys(Keys.ARROW_DOWN)

            elif age <12:
                age =12 - age
                for i in range(age):
                    sel_age.send_keys(Keys.ARROW_UP)

            elif age == 'age at check out':
                for i in range(12):
                    sel_age.send_keys(Keys.ARROW_UP)

            else:
                print(f'{age} is not a valid age')
        
        for i in range(1, rooms):
            sel_rooms.send_keys(Keys.ARROW_DOWN)

    def apply_filterations(self):
        filt = bookingFilteration(driver=self)
        filt.with_additional_health_safety()
        filt.with_star_rating(4, 5, 1)

    def report_results(self):
        hotel_list = self.find_element_by_id("hotellist_inner")
        r = Reportresults(hotelList=hotel_list)
        r.get_hotel_attr()








