import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization_stepik(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(url=url)

    wait = WebDriverWait(browser, 5)

    button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Add to basket"]')))
    assert button is not None, "Element not found"

    time.sleep(5)
