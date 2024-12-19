from selenium.webdriver.common.by import By


class Products:
    def __init__(self, driver):
        self.driver = driver

    title = (By.CSS_SELECTOR, ".title")

    def get_title(self):
        return self.driver.find_element(*Products.title)