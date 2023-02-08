from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AmazonSearch(BasePage):

    results_title: tuple = (By.XPATH, "(//span[@class='a-size-medium-plus a-color-base a-text-normal'])[1]")

    def __init__(self, driver):
        super(AmazonSearch, self).__init__(driver)
