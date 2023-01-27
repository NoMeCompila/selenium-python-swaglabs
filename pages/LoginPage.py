from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):

    # attributes
    user_name_textbox = (By.ID, "user-name")
    user_pass_textbox = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    login_msg_error = (By.TAG_NAME, "h3")

    # constructor
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    # methods

    # search for username and password text box, fills it with the given string parameters then clicks the login button
    def login_swag_labs(self, username: str, password: str) -> None:
        self.do_send_key(self.user_name_textbox, username)
        self.do_send_key(self.user_pass_textbox, password)
        self.do_click(self.login_btn)

    # clicks on the logind big red button
    def click_login_btn(self) -> None:
        self.do_click(self.login_btn)

    # returns the error message from an invalid login
    def get_err_mesg(self) -> str:
        return self.get_text(self.login_msg_error)