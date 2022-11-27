import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_folder", default=os.path.expanduser("~/Documents/"))
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")
    driver = None

    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(executable_path=f"{driver_folder}{os.sep}geckodriver", options=options)
    elif _browser == "chrome":
        options = CromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}chromedriver", options=options)
    elif _browser == "edge":
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(executable_path=f"{driver_folder}{os.sep}msedgedriver", options=options)

    driver.maximize_window()
    yield driver
    driver.close()
    
