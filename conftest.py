import pytest
from selenium import webdriver

MAIN_PAGE_URL = "https://www.padsplit.com/"


@pytest.fixture(scope="session")
def chrome_drv(request):
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(MAIN_PAGE_URL)
    yield driver
    print("\nquit browser..")
    driver.quit()
    return driver




