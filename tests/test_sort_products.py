from selenium.webdriver.chrome.webdriver import WebDriver
from pages.TestSwagLabsProducts import ProductsPage
from pages.TestSwaglabLogin import LoginPage
import pytest
from utilities import keys


@pytest.mark.sort_products
@pytest.mark.sort_a_z
def test_order_a_z(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    produtcs_page = ProductsPage(init_driver)
    assert produtcs_page.get_title() == keys.swag_labs_title

    produtcs_page.select_products_order(keys.products_order_a_z)
    assert produtcs_page.get_first_product() == keys.first_a_z
    assert keys.last_a_z in produtcs_page.get_last_prduct()


@pytest.mark.sort_products
@pytest.mark.sort_z_a
def test_order_z_a(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    produtcs_page = ProductsPage(init_driver)
    assert produtcs_page.get_title() == keys.swag_labs_title

    produtcs_page.select_products_order(keys.products_order_z_a)
    assert keys.last_a_z in produtcs_page.get_first_product()
    assert keys.first_a_z in produtcs_page.get_last_prduct()


@pytest.mark.sort_products
@pytest.mark.sort_high
def test_order_high_price(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    produtcs_page = ProductsPage(init_driver)
    assert produtcs_page.get_title() == keys.swag_labs_title

    produtcs_page.select_products_order(keys.products_order_price_high)
    assert keys.first_high in produtcs_page.get_first_product()
    assert keys.last_high in produtcs_page.get_last_prduct()


@pytest.mark.sort_products
@pytest.mark.sort_low
def test_order_low_price(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    produtcs_page = ProductsPage(init_driver)
    assert produtcs_page.get_title() == keys.swag_labs_title

    produtcs_page.select_products_order(keys.products_order_price_low)
    assert keys.last_high in produtcs_page.get_first_product()
    assert keys.first_high in produtcs_page.get_last_prduct()