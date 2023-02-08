from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AmazonPage(BasePage):

    login_side: tuple = (By.XPATH, "//span[@class='a-truncate-cut']")
    search_bar: tuple = (By.ID, "twotabsearchtextbox")
    lupe: tuple = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super(AmazonPage, self).__init__(driver)
