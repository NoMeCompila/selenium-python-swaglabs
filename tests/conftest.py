import pytest
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def config(scope="session"):
    """Fixture to load and return the configuration data.
    The fixture loads the data from a JSON file located at given path and returns it as a dictionary.
    Before returning the configuration data, the fixture asserts that the "browser" value is either
    "Firefox", "Chrome", or "Headless Chrome".
    Args:
        scope: The scope of the fixture, default is "session".
    Returns:
        A dictionary containing the configuration data.
    Raises:
        AssertionError: If the "browser" value in the configuration file is not Firefox, Chrome, or Headless Chrome.
    """
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
