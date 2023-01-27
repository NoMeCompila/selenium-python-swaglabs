from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductsPage(BasePage):

    products_order: tuple = (By.CLASS_NAME, "product_sort_container")
    products_locator: tuple = (By.XPATH, "//div[@class='inventory_item_name']")
    twitter_locator: tuple = (By.XPATH, "//li[@class='social_twitter']/a")
    facebook_locator: tuple = (By.XPATH, "//li[@class='social_facebook']/a")
    linkedin_locator: tuple = (By.XPATH, "//li[@class='social_linkedin']/a")

    # add to cart buttons
    bolt_tshirt_btn: tuple = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    fleece_btn: tuple = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    add_btn: tuple = (By.XPATH, "//div[@class='pricebar']/button")
    total_cart_items: tuple = (By.XPATH, "//span[@class='shopping_cart_badge']")

    # constructor
    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver)

    # gets title for the homepage
    def get_title(self) -> str:
        return self.get_text(self.title)

    # change the order of products
    def select_products_order(self, index: int) -> None:
        self.select_dropdown_opt(self.products_order, index)

    # order the text of the dropdown
    def get_order_text(self) -> str:
        return self.get_text(self.products_order)

    # return the name of all products
    def get_all_products(self) -> None:
        print(self.list_all_elements(self.products_locator))

    # returns the first product of the swaglabs home page
    def get_first_product(self) -> str:
        return self.get_first_element(self.products_locator)

    # returns the last product of the swaglabs home page
    def get_last_product(self) -> str:
        return self.get_last_item(self.products_locator)

    def add_tshirt(self) -> None:
        self.do_click(self.products_locator)

    def add_jacket(self) -> None:
        self.do_click(self.fleece_btn)

    def add_product(self, by_locator: tuple) -> None:
        self.do_click(by_locator)

    def get_btn_texts(self) -> list:
        return self.list_all_elements(self.add_btn)

    # clicks in social media icons
    def verify_social_media(self, by_locator: tuple) -> None:
        self.do_click(by_locator)
        self.switch_windows(1)


'''
    def click_tweeter(self) -> None:
        self.do_click(self.twitter_locator)
        self.switch_windows(1)

    def click_facebook(self) -> None:
        self.do_click(self.facebook_locator)
        self.switch_windows(1)

    def click_linkedin(self) -> None:
        self.do_click(self.linkedin_locator)
        self.switch_windows(1)
'''