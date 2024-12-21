import time

from PageObjects.LoginPage import LoginPage
from Tests.conftest import username, password
from utils.BaseClass import BaseClass


class Test_Login(BaseClass):

    def test_valid_login_001(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(username)
         # (config['username']))
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(password)
            # config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()
        time.sleep(5)
        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")
