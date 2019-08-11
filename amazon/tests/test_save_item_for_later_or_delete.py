from amazon.pages.home.amazon_home import AmazonHome
from amazon.pages.home.view_page import ViewPage
import unittest
import pytest
from amazon.utilities.read_data import read_file
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("one_time_setup", "set_up")
@ddt
class TestSaveForLater(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.amazon_home_page = AmazonHome(self.driver)
        self.amazon_view_page = ViewPage(self.driver)

    @pytest.mark.run(order=1)
    @pytest.fixture()
    @data(read_file())
    @unpack
    def test_save_for_later(self, first_book, second_book, third_book):
        #search and add item to cart
        self.amazon_home_page.enter_search_text(first_book)
        self.amazon_home_page.select_searched_item(first_book)
        self.amazon_home_page.add_to_cart()

        # search and add item to cart
        self.amazon_home_page.enter_search_text(second_book)
        self.amazon_home_page.select_searched_item(second_book)
        self.amazon_home_page.add_to_cart()

        # search and add item to cart
        self.amazon_home_page.enter_search_text(third_book)
        self.amazon_home_page.select_searched_item(third_book)
        self.amazon_home_page.add_to_cart()

        # confirm number of items in cart
        cart_count = self.amazon_home_page.get_number_of_cart_items()
        assert cart_count == 3

        item = "Experiences of Test Automation"
        action = "save"

        #view items in cart view page and save item for later
        self.amazon_home_page.view_cart_items()
        self.amazon_view_page.save_item_for_later(item, action)

        #verify item is saved for later
        item_count = self.amazon_view_page.verify_item_is_saved_for_later_or_deleted()
        assert item_count == 2, "This number of items in carts has been reduced by 1"


    def test_delete_item_from_cart(self):
        #deletes item from cart

        item = "Agile Testing"
        action = "delete"
        self.amazon_view_page.delete_item_from_cart(item, action)
        item_count = self.amazon_view_page.verify_item_is_saved_for_later_or_deleted()
        assert item_count == 1, "The item deleted has not been removed from cart"

    def test_increase_item_quantity(self):
        #add specified quantity to cart

        item = "Selenium WebDriver 3 Practical Guide"
        qty = 2
        self.amazon_view_page.increase_item_quantity(item, qty)
        item_count = self.amazon_view_page.verify_item_is_saved_for_later_or_deleted()
        assert item_count == 3, "More or less than 3 items in cart"

    def test_mark_item_as_gift(self):
        #mark item as gift and verify

        item = "Selenium WebDriver 3 Practical Guide"
        gift_checkbox_checked = self.amazon_view_page.mark_item_as_gift(item)
        assert gift_checkbox_checked == True, "Gift checkbox is not checked"