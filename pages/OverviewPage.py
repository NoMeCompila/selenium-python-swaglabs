from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class OverPage(BasePage):

    items_price: tuple = (By.XPATH, "//div[@class='inventory_item_price']")
    tax_price: tuple = (By.CLASS_NAME, "summary_tax_label")
    sumary_total: tuple = (By.CLASS_NAME, "summary_total_label")
    finish_btn: tuple = (By.ID, "finish")

    def __init__(self, driver):
        super(OverPage, self).__init__(driver)

    def get_items_cost(self, by_locator) -> float:
        return sum(list(map(lambda x: float(x.replace("$", "")), self.list_all_elements(by_locator))))

    def dollar_to_float(self, by_locator: tuple) -> float:
        if "Tax" in self.get_text(by_locator):
            price = float(self.get_text(by_locator).replace("Tax: $", ""))
        elif "Total" in self.get_text(by_locator):
            price = float(self.get_text(by_locator).replace("Total: $", ""))
        else:
            price = float(self.get_text(by_locator).replace("$", ""))
        return price

    def get_total_cost(self, items_locator: tuple, tax_locator: tuple) -> float:
        return self.get_items_cost(items_locator) + self.dollar_to_float(tax_locator)


'''
    def dollar_to_float(self, by_locator: tuple) -> float:
        return float(self.get_text(by_locator).replace("$", ""))

    def clear_total(self, by_locator: tuple) -> float:
        return float(self.get_text(by_locator).replace("Total: $", ""))
        
    def clear_tax(self, by_locator: tuple) -> float:
        return float(self.get_text(by_locator).replace("Tax: $", ""))
'''

