from selenium.webdriver.remote.webdriver import WebDriver


class bookingFilteration:
    def __init__(self, driver:WebDriver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    def with_additional_health_safety(self):
        try:
            chk_box=self.driver.find_element_by_xpath(f'//*[@id="filter_health_and_hygiene"]/div[2]/a/label/input')
            self.driver.execute_script("arguments[0].click();", chk_box)
        except:
            chk_box=self.driver.find_element_by_id(f'__bui-1')
            self.driver.execute_script("arguments[0].click();", chk_box)
    
    def with_star_rating(self, *stars):
        for star in stars:
            filter_elemant = self.driver.find_element_by_css_selector(f'a[data-id="class-{star}"]')
            filter_elemant.click()