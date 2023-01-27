from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:

    title: tuple = (By.CLASS_NAME, "title")

    # constructor defines driver and implicit wait
    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(5) preguntar
        self.wait = WebDriverWait(self.driver, 10)

    # get an URL in str format and goes there
    def go_to_page(self, url: str) -> None:
        self.driver.get(url)

    # waits for an element then clicks it
    def do_click(self, by_locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    # write some text given as a parameter in a textbox
    def do_send_key(self, by_locator: tuple, txt: str) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(txt)

    # waits for an element and returns its text
    def get_text(self, by_locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    # clear the text from a textbox
    def clear_textbox(self, by_locator: tuple) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    # select an option in dropdown web element
    def select_dropdown_opt(self, by_locator: tuple, index: int) -> None:
        Select(self.wait.until(EC.element_to_be_clickable(by_locator))).select_by_index(index)

    # returns a list of all products with the vigen by locator
    def list_all_elements(self, by_locator: tuple) -> list:
        all_products = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        return [x.text for x in all_products]

    # returns the first item for the list of all elements with the given locator
    def get_first_element(self, by_locator: tuple) -> str:
        all_elements = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        return [x.text for x in all_elements][0]

    # returns the last item for the list of all elements with the given locator
    def get_last_item(self, by_locator: tuple) -> str:
        all_elements = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        return [x.text for x in all_elements][::-1][0]

    # indicates the driver to switch control of the execution flow to the window at the position of the given index
    def switch_windows(self, index: int) -> None:
        self.driver.switch_to.window(self.driver.window_handles[index])

    # gets the page title of the current page
    def get_page_title(self) -> str:
        return self.driver.title

    # gets the url of the current page
    def get_current_url(self) -> str:
        return self.driver.current_url
