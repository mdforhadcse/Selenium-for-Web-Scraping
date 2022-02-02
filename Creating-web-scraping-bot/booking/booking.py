import booking.constants as const
import os
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
import pandas as pd


class Booking(webdriver.Chrome):
    def __init__(self, driver_path="", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            # f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency=
            # {currency};top_currency=1"]' -FULL STRING
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'  # SUB-STRING define
        )
        selected_currency_element.click()

    def search_place_to_visit(self, place_to_visit):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_visit)

        select_first_result = self.find_element_by_css_selector('li[data-i="0"]')
        select_first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        select_check_in_date = self.find_element_by_css_selector(f'td[data-date="{check_in_date}"]')
        select_check_in_date.click()

        select_check_out_date = self.find_element_by_css_selector(f'td[data-date="{check_out_date}"]')
        select_check_out_date.click()

    def select_adults(self, count=1):
        select_element = self.find_element_by_id('xp__guests__toggle')
        select_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            # if value of adult is 1 then get out of while loop
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute('value')  # getting value from attribute

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector('button[aria-label="Increase number of Adults"]')
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector('button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.sort_price_lowest_first()
        filtration.apply_star_rating(3, 4, 5)

    def report_results(self):
        hotel_boxes = self.find_element_by_class_name('_814193827')

        report = BookingReport(hotel_boxes)
        info_list = report.pull_deal_boxes_attributes()
        df = pd.DataFrame(info_list)
        print(df)
        print(info_list)
