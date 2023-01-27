from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CompletePage(BasePage):


    complete_cart: tuple = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super(CompletePage, self).__init__(driver)

