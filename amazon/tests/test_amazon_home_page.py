from amazon.pages.home.amazon_home import AmazonHome
from amazon.pages.home.view_page import ViewPage
import unittest
import pytest
from amazon.utilities.read_data import read_file
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("one_time_setup", "set_up")
@ddt
class TestAddToAmazonCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.amazon_home_page = AmazonHome(self.driver)
        self.amazon_view_page = ViewPage(self.driver)

    #@pytest.mark.run(order=1)
    @pytest.fixture()
    @data(read_file())
    @unpack
    def test_add_items_to_cart(self, first_book, second_book, third_book):
        print("data: ", data)
        self.amazon_home_page.enter_search_text(first_book)
        self.amazon_home_page.select_searched_item(first_book)
        self.amazon_home_page.add_to_cart()

        self.amazon_home_page.enter_search_text(second_book)
        self.amazon_home_page.select_searched_item(second_book)
        self.amazon_home_page.add_to_cart()

        self.amazon_home_page.enter_search_text(third_book)
        self.amazon_home_page.select_searched_item(third_book)
        self.amazon_home_page.add_to_cart()
        cart_count = self.amazon_home_page.get_number_of_cart_items()
        assert cart_count == 3
