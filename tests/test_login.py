from selenium.webdriver.chrome.webdriver import WebDriver
from pages.TestSwagLabsProducts import ProductsPage
from pages.TestSwaglabLogin import LoginPage
import pytest
from utilities import keys


@pytest.mark.valid_login
@pytest.mark.login
def test_login_swag_labs(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title


@pytest.mark.invalid_pwd
@pytest.mark.invalid_login
@pytest.mark.login
def test_invalid_pwd(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.invalid_user_pwd)

    assert keys.invalid_login_msg in login_page.get_err_mesg()


@pytest.mark.invalid_username
@pytest.mark.invalid_login
@pytest.mark.login
def test_invalid_username(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.invalid_username, keys.valid_user_pwd)

    assert keys.invalid_login_msg in login_page.get_err_mesg()


@pytest.mark.blank_data
@pytest.mark.invalid_login
@pytest.mark.login
def test_blank_data_login(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.click_login_btn()

    assert keys.invalid_login_msg in login_page.get_err_mesg()