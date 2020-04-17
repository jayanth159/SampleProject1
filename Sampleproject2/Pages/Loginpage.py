from Sampleproject2.Locators.locators import locators
class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.driver.username_textbox_id=locators.username_textbox_id
        self.driver.password_textbox_id=locators.password_textbox_id
        self.driver.signin_button_xpath=locators.signin_btn_xpath

    def enter_username(self,username):
        self.driver.find_element_by_id(self.driver.username_textbox_id).clear()
        self.driver.find_element_by_id(self.driver.username_textbox_id).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.driver.password_textbox_id).clear()
        self.driver.find_element_by_id(self.driver.password_textbox_id).send_keys(password)
    def signin(self):
        self.driver.find_element_by_xpath(self.driver.signin_button_xpath).click()