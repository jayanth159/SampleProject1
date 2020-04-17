from selenium import webdriver
import unittest
import time
from Sampleproject2.Pages.Loginpage import loginpage

class logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/jayanth.kumar/PycharmProjects/SampleProject1/Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_login(self):
        driver=self.driver
        driver.get("https://sso.central.247-inc.net/auth/UI/Login?goto=https://platformcentral.247-inc.net/auth/after_auth")
        login=loginpage(driver)
        login.enter_username("jayanth.kumar")
        login.enter_password("Kjmar@t47")
        login.signin()
        time.sleep(2)

    def tearDown(self):
        print(self.driver.title)
        self.driver.close()
        self.driver.quit()
        print("test completed")