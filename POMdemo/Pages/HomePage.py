from POMdemo.Locators.Locators import locators
class homepage():

    def __init__(self,driver):
        self.driver=driver
        self.driver.welcomeadmin_link_id=locators.welcomeadmin_link_id
        self.driver.logout_link_linktext=locators.logout_link_linktext

    def click_welcome(self):
        self.driver.find_element_by_id(self.driver.welcomeadmin_link_id).click()
    def click_logout(self):
        self.driver.find_element_by_link_text(self.driver.logout_link_linktext).click()