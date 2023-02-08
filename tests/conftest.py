import pytest
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# gives a json file path as a parametter and load in a python data object
def load_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data


@pytest.fixture()
def config(scope="session"):
    with open("C:/Users/fernando.caballero/PycharmProjects/selenium-python/config.json") as config_file:
        config = json.load(config_file)
    assert config["browser"] in ["Firefox", "Chrome", "Edge", "Headless Chrome"], f"Invalid browser value in " \
                                                                                  f"configuration: {config['browser']}"
    return config


@pytest.fixture()
def init_driver(config):
    if config["browser"] == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif config["browser"] == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif config["browser"] == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    else:
        raise Exception("Browser " + config["browser"] + " is not supported")

    driver.maximize_window()
    yield driver
    driver.quit()
