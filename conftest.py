from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': 'en-ES'})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("--language")
    if browser_language == "fr":
        print("\nstart chrome browser with french.")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        webdriver_service = Service('/path/to/chromedriver')
        browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    elif browser_language == "ru":
        print("\nstart chrome browser with russian.")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        webdriver_service = Service('/path/to/chromedriver')
        browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    elif browser_language == "es":
        print("\nstart chrome browser with spanish.")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        webdriver_service = Service('/path/to/chromedriver')
        browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    else:
        raise pytest.UsageError("--browser_name should have a language")
    yield browser
    print("\nquit browser..")
    browser.quit()
