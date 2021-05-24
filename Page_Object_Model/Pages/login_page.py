class LoginPage():
    # Define all the locators of the element
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    logout_link_text = "Logout"

    def __init__(self, driver):  # constructor initialized to create the driver
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.password_textbox_id).submit()

    def click_logout(self):
        self.driver.find_elemet_by_link_text(self.logout_link_text).click()
