from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductsPage(BasePage):

    title = (By.CLASS_NAME, "title")
    products_order = (By.CLASS_NAME, "product_sort_container")
    products_locator = (By.XPATH, "//div[@class='inventory_item_name']")

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


    def get_first_product(self) -> None:
        print(self.get_first_element(self.products_locator))

    def get_last_prduct(self) -> None:
        print(self.get_last_item(self.products_locator))