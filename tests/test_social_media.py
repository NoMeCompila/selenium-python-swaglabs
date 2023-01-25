import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.TestSwagLabsProducts import ProductsPage
from pages.TestSwaglabLogin import LoginPage
import pytest
from utilities import keys


@pytest.mark.social
@pytest.mark.tweeter
def test_twitter(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    products_page.click_tweeter()
    assert keys.twitter_url in products_page.get_current_url()


@pytest.mark.social
@pytest.mark.facebook
def test_facebook(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    products_page = ProductsPage(init_driver)
    products_page.click_facebook()
    assert keys.facebook_url in products_page.get_current_url()


@pytest.mark.social
@pytest.mark.linkedin
def test_linkedin(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    products_page = ProductsPage(init_driver)
    products_page.click_linkedin()
    assert keys.linkedin_url in products_page.get_current_url()