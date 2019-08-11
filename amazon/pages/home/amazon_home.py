from amazon.base.selenium_driver import SeleniumDriver
from amazon.utilities import custom_logger as cl
import logging
import time

class AmazonHome(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _search_box = "twotabsearchtextbox"
    _item_link = '//*[text()= "%s"]'
    _add_to_cart = "add-to-cart-button"
    _cart = "nav-cart-count"
    _new_item_accordion = "//div[@id='newOfferAccordionRow']//div[@class='a-accordion-row-a11y']"
    _paper_back_section = "mediaTab_heading_1"
    _swatch = "//*[@id='tmmSwatches']//li[2]"

    def enter_search_text(self, search_text):
        """
        for searching for item in search box
        :param search_text: search item string
        :return: null
        """
        self.send_keys(search_text, self._search_box)

    def select_an_item(self, search_text):
        self.select_searched_item(search_text)

    def select_searched_item(self, search_text):
        """
        select a specific item in cart view
        :param search_text: string for locating item
        :return:
        """
        search_text = search_text.strip()
        item_elem = self._item_link % search_text
        try:
            element = self.get_element(item_elem, "xpath")
            element.click()
            self.log.info("Send data on element with locator: " + item_elem )
        except:
            self.log.info("Cannot send data on element with locator: " + item_elem )
            self.print_stack()

    def add_to_cart(self):
        """
        Add item to cart based on media type
        :return: null
        """
        swatch_elem = self.check_swatch_elem_displayed()
        if swatch_elem:
            _swatch = self.get_element(self._swatch, "xpath")
            _swatch_attr = _swatch.get_attribute("class")
            if "selected" in _swatch_attr:
                element = self.get_element(self._add_to_cart)
                element.click()
        else:
            self.select_media_type(self._paper_back_section)
            new_item_accordion = self.get_element(self._new_item_accordion, "xpath")
            accordion_aria_attr = new_item_accordion.get_attribute("aria-checked")
            # cart_count = int(cart_elem.text)
            print(accordion_aria_attr)
            try:
                if accordion_aria_attr == 'true':
                    element = self.get_element(self._add_to_cart)
                    element.click()
                    time.sleep(5)
                    self.log.info("Send data on element with locator: " + self._add_to_cart)
                else:
                    new_item_accordion = self.get_element(self._new_item_accordion, "xpath")
                    new_item_accordion.click()
                    time.sleep(5)
                    element = self.get_element(self._add_to_cart)
                    element.click()
                    time.sleep(3)

            except:
                self.log.info("Cannot send data on element with locator: " + self._add_to_cart)
                self.print_stack()


    def select_media_type(self, locator):
        """
        selects type of media e.g paperback
        :param locator: id for locating element
        :return: null
        """
        class_name = "a-active"
        media_section = self.get_element(locator)
        target_attr= media_section.get_attribute("class")
        if class_name in target_attr:
            #self.log.info("media section: " + media_section + " is active")
            pass
        else:
            media_section.click()

    def check_swatch_elem_displayed(self):
        _swatch_parent = "tmmSwatches"
        _swatch_parent = self.get_element(_swatch_parent)
        if _swatch_parent == None:
            pass
        else:
            return _swatch_parent.is_displayed()

    def get_number_of_cart_items(self):
        """

        :return: item count in cart
        """
        count_elem = self.get_element(self._cart)
        cart_items_count = int(count_elem.text)
        return cart_items_count

    def view_cart_items(self):
        """
        for viewing cart items
        :return: null
        """
        cart = self.get_element(self._cart)
        cart.click()
