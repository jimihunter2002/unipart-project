from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from ..utilities import custom_logger as cl
import logging


class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("locator type " + locator_type + " not correct/ supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locator_type)
        return element

    def elememt_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            element.send_keys(Keys.ENTER)
            self.log.info("Send data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def waitForElement(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=poll_frequency,
                                ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False
