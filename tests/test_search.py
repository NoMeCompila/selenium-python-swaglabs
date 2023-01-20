import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(init_driver):
    init_driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(init_driver, 10)
    user_textbox = init_driver.find_element(By.ID, "user-name")
    user_textbox.clear()
    user_textbox.send_keys("standard_user")

    pass_textbox = init_driver.find_element(By.ID, "password")
    pass_textbox.clear()
    pass_textbox.send_keys("secret_sauce")

    login_btn = init_driver.find_element(By.NAME, "login-button")
    login_btn.click()

     #= init_driver.find_element(By.XPATH, )
    prod_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    title = prod_title.text
    print()
    print(title)

    assert title == "PRODUCTS"

#def test_swag_home(init_driver):
#    wait = WebDriverWait(init_driver,10)
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_btn.click()
    count_products = init_driver.find_element(By.XPATH, "//span[@class = 'shopping_cart_badge']").text
    print(f"cantidad de productos en el carrito: {count_products}")
    assert int(count_products) == 1