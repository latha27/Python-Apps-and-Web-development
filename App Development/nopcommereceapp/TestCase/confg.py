from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_adoption(parser):
    parser.adopation("--browser--")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser--")



