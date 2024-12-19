from selenium.webdriver.common.by import By

from PageObjects.Products import Products


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "user-name")
    password = (By.NAME, "password")
    login_button = (By.NAME, "login-button")

    def get_name(self):
        return self.driver.find_element(*LoginPage.name)


    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        self.driver.find_element(*LoginPage.login_button).click()
        products = Products(self.driver)
        return products
