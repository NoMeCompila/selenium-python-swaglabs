from pages.TestSwagLabsProducts import ProductsPage
from pages.TestSwaglabLogin import LoginPage
import pytest
from utilities import keys


@pytest.mark.login
def test_login_swag_labs(init_driver):
    login_page = LoginPage(init_driver)
    login_page.go_to_page(keys.sauce_url)
    login_page.login_swag_labs(keys.valid_username, keys.valid_user_pwd)

    products_page = ProductsPage(init_driver)
    assert products_page.get_title() == keys.swag_labs_title

    products_page.select_products_order(keys.products_order_z_a)
    print()
    products_page.get_first_product()
    products_page.get_last_prduct()