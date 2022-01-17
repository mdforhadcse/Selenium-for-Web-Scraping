# using Chrome Driver Manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# from selenium.webdriver.common.keys import Keys  # for enter keys from keyboard
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium.webdriver.chrome.service import Service
ser = Service("/Users/forhad/ChromeDriver/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.implicitly_wait(5)
try:
    no_button = driver.find_element_by_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. skipping......')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()