from selenium import webdriver
import HtmlTestRunner
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMdemo.Pages.HomePage import homepage
from POMdemo.Pages.LoginPage import Loginpage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/jayanth.kumar/PycharmProjects/SampleProject1/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login=Loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.press_login()
        hompage=homepage(driver)
        hompage.click_welcome()
        hompage.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # print(self.driver.title)
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output ="C:/Users/jayanth.kumar/PycharmProjects/SampleProject1/reports"))

