from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
class Reportresults:
    # hotel_name=''
    def __init__(self,  hotelList: WebElement):
        self.hotelList=hotelList
        self.elements = self.pull_element()
        

    def pull_element(self):
        return self.hotelList.find_elements_by_class_name('sr_property_block')


    def get_hotel_attr(self):
        for element in self.elements:
            hotel_name = element.find_element_by_class_name(
                'sr-hotel__name').get_attribute('innerHTML').strip()
            print(hotel_name)     