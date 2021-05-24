from selenium import webdriver
import unittest
import HtmlTestRunner
import sys  # this is imported to et the PATH environment variable value
# Set PATH environment variable value to current folder location
# To run the program in terminal we need to set the value of PATH variable to the current project location
# HTML report will only generate if we run the program in terminal
sys.path.append("/Users/animeshmukherjee/PycharmProjects/pythonProject/Unit_Test_Page_Object_Model")
from Page_Object_Model.Pages.login_page import LoginPage
import time


class TestLogin(unittest.TestCase):
    base_url = "https://admin-demo.nopcommerce.com/"
    email = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod  # defined the setUpClass to execute as first method
    def setUpClass(cls):
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        time.sleep(3)
        login_page.click_login()
        time.sleep(6)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Website title does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/animeshmukherjee/Desktop/Animesh/Log_file'))

# To run this test case in terminal type "python3 Page_Object_Model/TestCases/login_test.py"
