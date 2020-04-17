from selenium import webdriver
import unittest
import HtmlTestRunner
class googlesearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/jayanth.kumar/PycharmProjects/SampleProject1/Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_search(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("what is Python")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def test_search_jayanth(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("what is Jayanth")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/jayanth.kumar/PycharmProjects/SampleProject1/reports"))