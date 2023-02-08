from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):

    cart_items: tuple = (By.XPATH, "//div[@class='inventory_item_name']")
    item_price: tuple = (By.XPATH, "//div[@class='inventory_item_price']")
    checkout_btn: tuple = (By.ID, "checkout")

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)


