from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CheckPage(BasePage):

    title: tuple = (By.CLASS_NAME, "title")
    f_name: tuple = (By.ID, "first-name")
    l_name: tuple = (By.ID, "last-name")
    zip_c: tuple = (By.ID, "postal-code")
    continue_btn: tuple = (By.ID, "continue")

    def __init__(self, driver):
        super(CheckPage, self).__init__(driver)

    def fill_personal_data(self, fname_locator: tuple,
                           lname_locator: tuple, zip_locator: tuple, first_name: str, last_name: str, zip_code: str):

        self.do_send_key(fname_locator, first_name)
        self.do_send_key(lname_locator, last_name)
        self.do_send_key(zip_locator, zip_code)