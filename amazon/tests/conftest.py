import os
import pytest
from amazon.base.webdriver_factory import WebDriverFactory
#from ..base.webdriver_factory import WebDriverFactory
#from ..base.webdriver_factory import  WebDriverFactory

@pytest.yield_fixture()
def set_up():
    print("running method level setup")
    yield
    print("running method level tear down")

@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("running one time tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
