

from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test():
    def phonenumber(self,i):
        self.areaCode = i[0:2]
        self.exchange=i[2:6]
        self.line=i[6:10]
        return "(%s) %s-%s" % ( self.areaCode, self.exchange, self.line )
    def script(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\user\Documents\testing-python-app\Rippling\Driver\chromedriver.exe")
        baseURL = "https://vanilla-masker.github.io/vanilla-masker/demo.html"
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        phone_no_in_text='1234567890'
        phone_no = driver.find_element(By.ID, 'phone')
        phone_no.send_keys(phone_no_in_text)
        time.sleep(3)
        phone_number_text=phone_no.get_attribute('value')
        rendering_phone_number= self.phonenumber(phone_no_in_text)
        only_number=driver.find_element(By.ID,'numbers')
        only_number.send_keys(phone_no_in_text)
        time.sleep(3)
        text=only_number.get_attribute('value')

        assert text==phone_no_in_text
        assert phone_number_text==rendering_phone_number

        driver.quit()



test=test();
test.script()

