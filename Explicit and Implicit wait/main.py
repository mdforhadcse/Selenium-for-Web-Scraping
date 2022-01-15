# import os
# from selenium import webdriver
#
# # os.environ['PATH'] += r"/Users/forhad/ChromeDriver"
# # driver = webdriver.Chrome()
#
# file_path = '/Users/forhad/ChromeDriver/chromedriver'
# driver = webdriver.Chrome(file_path)


# using Chrome Driver Manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(5) #timeout to implicitly wait for an element to be found,or a command to complete.
my_element = driver.find_element_by_id('downloadButton')
my_element.click()


WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), # Element filtration
        'Complete!' #Expected text
    )
)