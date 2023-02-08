import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.AmazonPage import AmazonPage
import pytest
from pages.AmazonSearch import AmazonSearch
from utilities import keys
from tests.conftest import load_data

data = load_data("C:/Users/fernando.caballero/PycharmProjects/selenium-python/data/AmazonData.json")


@pytest.mark.amazon
@pytest.mark.parametrize("element", data["AmazonInput"])
def test_amazon_search(init_driver: WebDriver, element: str) -> None:
    amazon_home = AmazonPage(init_driver)
    amazon_home.go_to_page(keys.amazon_url)
    assert amazon_home.get_text(amazon_home.login_side) == keys.login_title
    amazon_home.do_send_key(amazon_home.search_bar, element)
    amazon_home.do_click(amazon_home.lupe)
    amazon_search = AmazonSearch(init_driver)
    assert amazon_search.get_text(amazon_search.results_title) == keys.res
    time.sleep(3)
