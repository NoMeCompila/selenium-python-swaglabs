from selenium.webdriver.chrome.webdriver import WebDriver
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckPage
from pages.OverviewPage import OverPage
from pages.ProductsPage import ProductsPage
from pages.LoginPage import LoginPage
import pytest
from utilities import keys


@pytest.mark.correct_data
@pytest.mark.fill_data
def test_complete_data(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.add_product(products_page.bolt_tshirt_btn)
    products_page.add_product(products_page.fleece_btn)
    assert products_page.get_btn_texts().count("REMOVE") == 2
    assert products_page.get_text(products_page.total_cart_items) == "2"

    products_page.do_click(products_page.total_cart_items)
    cart = CartPage(init_driver)
    assert cart.get_text(cart.title) == keys.cart_title
    assert len(cart.list_all_elements(cart.cart_items)) == 2

    cart.do_click(cart.checkout_btn)
    check_page = CheckPage(init_driver)
    assert check_page.get_text(check_page.title) == keys.check_title

    check_page.fill_personal_data(check_page.f_name, check_page.l_name, check_page.zip_c, keys.first_name,
                                  keys.last_name, keys.zip_code)

    check_page.do_click(check_page.continue_btn)
    overview_page = OverPage(init_driver)
    assert overview_page.get_text(overview_page.title) == keys.overview_title


@pytest.mark.blank_data
@pytest.mark.fill_data
def test_blank_data(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.add_product(products_page.bolt_tshirt_btn)
    products_page.add_product(products_page.fleece_btn)
    assert products_page.get_btn_texts().count("REMOVE") == 2
    assert products_page.get_text(products_page.total_cart_items) == "2"

    products_page.do_click(products_page.total_cart_items)
    cart = CartPage(init_driver)
    assert cart.get_text(cart.title) == keys.cart_title
    assert len(cart.list_all_elements(cart.cart_items)) == 2

    cart.do_click(cart.checkout_btn)
    check_page = CheckPage(init_driver)
    assert check_page.get_text(check_page.title) == keys.check_title

    check_page.fill_personal_data(check_page.f_name, check_page.l_name, check_page.zip_c)
    check_page.do_click(check_page.continue_btn)
    assert keys.blank_data_error in check_page.get_text(check_page.data_error_msg)


@pytest.mark.blank_name
@pytest.mark.fill_data
def test_blank_name(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.add_product(products_page.bolt_tshirt_btn)
    products_page.add_product(products_page.fleece_btn)
    assert products_page.get_btn_texts().count("REMOVE") == 2
    assert products_page.get_text(products_page.total_cart_items) == "2"

    products_page.do_click(products_page.total_cart_items)
    cart = CartPage(init_driver)
    assert cart.get_text(cart.title) == keys.cart_title
    assert len(cart.list_all_elements(cart.cart_items)) == 2

    cart.do_click(cart.checkout_btn)
    check_page = CheckPage(init_driver)
    assert check_page.get_text(check_page.title) == keys.check_title

    check_page.fill_personal_data(check_page.f_name, check_page.l_name, check_page.zip_c, "", keys.last_name,
                                  keys.zip_code)
    check_page.do_click(check_page.continue_btn)
    assert keys.blank_data_error in check_page.get_text(check_page.data_error_msg)


@pytest.mark.blank_last_name
@pytest.mark.fill_data
def test_blank_last_name(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.add_product(products_page.bolt_tshirt_btn)
    products_page.add_product(products_page.fleece_btn)
    assert products_page.get_btn_texts().count("REMOVE") == 2
    assert products_page.get_text(products_page.total_cart_items) == "2"

    products_page.do_click(products_page.total_cart_items)
    cart = CartPage(init_driver)
    assert cart.get_text(cart.title) == keys.cart_title
    assert len(cart.list_all_elements(cart.cart_items)) == 2

    cart.do_click(cart.checkout_btn)
    check_page = CheckPage(init_driver)
    assert check_page.get_text(check_page.title) == keys.check_title

    check_page.fill_personal_data(check_page.f_name, check_page.l_name, check_page.zip_c, keys.first_name, "",
                                  keys.zip_code)
    check_page.do_click(check_page.continue_btn)
    assert keys.blank_data_error in check_page.get_text(check_page.data_error_msg)


@pytest.mark.blank_zip_code
@pytest.mark.fill_data
def test_blank_last_name(init_driver: WebDriver) -> None:
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)
    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.add_product(products_page.bolt_tshirt_btn)
    products_page.add_product(products_page.fleece_btn)
    assert products_page.get_btn_texts().count("REMOVE") == 2
    assert products_page.get_text(products_page.total_cart_items) == "2"

    products_page.do_click(products_page.total_cart_items)
    cart = CartPage(init_driver)
    assert cart.get_text(cart.title) == keys.cart_title
    assert len(cart.list_all_elements(cart.cart_items)) == 2

    cart.do_click(cart.checkout_btn)
    check_page = CheckPage(init_driver)
    assert check_page.get_text(check_page.title) == keys.check_title

    check_page.fill_personal_data(check_page.f_name, check_page.l_name, check_page.zip_c, keys.first_name,
                                  keys.last_name)
    check_page.do_click(check_page.continue_btn)
    assert keys.blank_data_error in check_page.get_text(check_page.data_error_msg)
