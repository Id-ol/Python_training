# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_first_olx(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_first_olx(self):
        success = True
        wd = self.wd
        wd.get("https://www.olx.ua/account/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index")
        wd.find_element_by_id("userPass").click()
        wd.find_element_by_id("userPass").send_keys("\\undefined")
        wd.find_element_by_id("userEmailPhoneRegister").click()
        wd.find_element_by_id("userEmailPhoneRegister").send_keys("\\undefined")
        wd.find_element_by_id("userPassRegister").click()
        wd.find_element_by_id("userPassRegister").send_keys("\\undefined")
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[1]/div/form/fieldset/div[1]/div/input").click()
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[1]/div/form/fieldset/div[1]/div/input").send_keys("\\undefined")
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[1]/div/form/fieldset/div[2]/div/input").click()
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[1]/div/form/fieldset/div[2]/div/input").send_keys("\\undefined")
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[2]/form/div[1]/div/input").click()
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[2]/form/div[1]/div/input").send_keys("\\undefined")
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[2]/form/div[2]/div/input").click()
        wd.find_element_by_xpath("//div[@class='mandatory-login__login']/div/div/ul/li[2]/form/div[2]/div/input").send_keys("\\undefined")
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").clear()
        wd.find_element_by_id("userEmail").send_keys("d-o@ukr.net")
        wd.find_element_by_id("userPass").click()
        wd.find_element_by_id("userPass").clear()
        wd.find_element_by_id("userPass").send_keys("0905do")
        wd.find_element_by_id("se_userLogin").click()
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").send_keys("\\undefined")
        wd.find_element_by_id("userPass").click()
        wd.find_element_by_id("userPass").send_keys("\\undefined")
        wd.find_element_by_id("userEmailPhoneRegister").click()
        wd.find_element_by_id("userEmailPhoneRegister").send_keys("\\undefined")
        wd.find_element_by_id("userPassRegister").click()
        wd.find_element_by_id("userPassRegister").send_keys("\\undefined")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
