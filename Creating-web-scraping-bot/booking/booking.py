# from selenium.webdriver.chrome.service import Service
# ser = Service("/Users/forhad/ChromeDriver/chromedriver")
# op = webdriver.ChromeOptions()
# s = webdriver.Chrome(service=ser, options=op)


import booking.constants as const
from selenium import webdriver
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/Users/forhad/ChromeDriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)
