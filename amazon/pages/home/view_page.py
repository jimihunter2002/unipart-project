from selenium import webdriver
from selenium.webdriver.support.select import Select
from amazon.utilities import custom_logger as cl
from amazon.pages.home.amazon_home import AmazonHome
from amazon.base.selenium_driver import SeleniumDriver
import logging
import time

class ViewPage(AmazonHome):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators for view page
    _delete_or_save = ('//input[contains(@aria-label,"%s") and contains(@value,"%s")]')
    _save_for_later = "Save for later"
    _delete_item = "Delete"
    _select_option = '//span[@class="a-size-medium sc-product-title a-text-bold" and ' \
                     'contains(text(),"%s")]//ancestor::div[@class="a-fixed-left-grid-col a-col-right"]' \
                     '//descendant::select[@name="quantity"]'
    _checkbox_option = '//span[@class="a-size-medium sc-product-title a-text-bold" and contains(text(),"%s")]' \
                       '//ancestor::div[@class="a-fixed-left-grid-col a-col-right"]' \
                       '//descendant::input[@type="checkbox"]'

    def save_item_for_later(self, item, action):
        """

        :param item: string for locating item
        :param action: Save for later
        :return: no return value
        """
        action_elem = self.get_element_action(item, action)
        action_elem.click()
        time.sleep(5)


    def delete_item_from_cart(self, item, action):
        """

        :param item: string for locating item
        :param action: Delete
        :return: no return value
        """
        action_elem = self.get_element_action(item, action)
        action_elem.click()
        time.sleep(5)

    def get_element_action(self, item, action):
        """

        :param item: string for locating element
        :param action: save or delete
        :return:
        """
        if action.lower() == "save":
            _save = self._delete_or_save % (item, self._save_for_later)
            _save =  self.get_element(_save, "xpath")
            return _save
        elif action.lower() == "delete":
            _delete = self._delete_or_save % (item, self._delete_item)
            _delete = self.get_element(_delete, "xpath")
            return _delete
        else:
            return

    def verify_option_not_displayed(self, item, action):
        option = self.get_element_action(item, action)
        return option.self.is_displayed()

    def verify_item_is_saved_for_later_or_deleted(self):
        """

        :return: number of items in cart
        """
        count_after_save = self.get_number_of_cart_items()
        return count_after_save

    def increase_item_quantity(self, item, qty):
        """
        :param item: text to match for finding element
        :param qty: quantity of items to add to cart
        1 less than intended quantity e.g if 2 is needed 1 is passed as
        quantity value
        :return: no return value
        """

        select_option = self._select_option % (item)
        _select_elem = self.get_element(select_option, "xpath")
        sel = Select(_select_elem)
        sel.select_by_index(qty)
        time.sleep(3)

    def mark_item_as_gift(self, item):
        """

        :param item: string for locating element
        :return: bool for checked or not
        """
        checkbox_option = self._checkbox_option % (item)
        gift_checkbox_elem = self.get_element(checkbox_option, "xpath")
        gift_checkbox_elem.click()
        time.sleep(2)
        gift_checkbox_elem =  self.is_checked(checkbox_option)
        return gift_checkbox_elem

    def is_checked(self, item):
        """

        :param item: string for locating element
        :return: bool for checked box
        """
        gift_checkbox_elem = self.get_element(item, "xpath")
        gift_checked = gift_checkbox_elem.get_attribute("checked")
        gift_checked = bool(gift_checked)
        return gift_checked

