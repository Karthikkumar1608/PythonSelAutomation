import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = None

def pytest_addoption(parser):
    parser.addini('url', 'url of the application')
    parser.addini('username', 'login username')
    parser.addini('password', 'login password')
    parser.addoption('--browser_name', action="store",default = "chrome")

@pytest.fixture(scope="session")
def config(request):
    return {
        'url':request.config.getini('url'),
        'username':request.config.getini('username'),
        'password':request.config.getini('password'),
        'browser_name':request.config.getoption("browser_name")
    }

@pytest.fixture(scope="class")
def setup(request, config):
    global driver
    if config['browser_name'] == 'chrome':
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)
    elif config['browser_name'] == 'firefox':
        service_obj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj)
    elif config['browser_name'] == 'edge':
        service_obj = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get(config['url'])
    request.cls.driver = driver
    request.cls.config = config

    yield driver
    driver.quit()
