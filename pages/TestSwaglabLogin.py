from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):

    # attributes
    user_name_textbox = (By.ID, "user-name")
    user_pass_textbox = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    # constructor
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    # methods

    # get an URL in str format and goes there
    def go_to_page(self, url: str) -> None:
        self.driver.get(url)

    # search for username and password text box, fills it with the given string parameters then clicks the login button
    def login_swag_labs(self, username: str, password: str) -> None:
        self.do_send_key(self.user_name_textbox, username)
        self.do_send_key(self.user_pass_textbox, password)
        self.do_click(self.login_btn)