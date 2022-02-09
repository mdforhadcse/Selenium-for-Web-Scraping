# This file will purse specific data that we need
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            'div[data-testid="property-card"]')

    def pull_deal_boxes_attributes(self):
        collection = []
        for deal_boxes in self.deal_boxes:
            hotel_name = deal_boxes.find_element_by_css_selector('div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotel_price = deal_boxes.find_element_by_class_name('_e885fdc12').get_attribute('innerHTML').replace('&nbsp;', ' ')
            hotel_score = deal_boxes.find_element_by_class_name('bd528f9ea6').get_attribute('innerHTML')

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection
