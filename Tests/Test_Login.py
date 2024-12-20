from PageObjects.LoginPage import LoginPage
from utils.BaseClass import BaseClass


class Test_Login(BaseClass):

    def test_valid_login_001(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")


    def test_valid_login_002(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_003(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_004(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_005(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_006(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_007(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")

    def test_valid_login_008(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")
        log.info("Test Execution completed")

    def test_valid_login_009(self, config):
        # To verify whether the user is able to login to the Application with valid credentials
        # and also verify whether the user is taken to 'Products' page post successful login.
        loginpage = LoginPage(self.driver)
        log = self.getlogger()
        log.info("Testcase_001_validate the Login with valid credentials")
        loginpage.get_name().send_keys(config['username'])
        log.info("Username entered successfully")
        loginpage.get_password().send_keys(config['password'])
        log.info("Password entered successfully")
        products = loginpage.get_login_button()

        productpagetitle = products.get_title().text
        assert "Products" == productpagetitle
        log.info("Logged in successfully")
        log.info("Test Execution completed1")