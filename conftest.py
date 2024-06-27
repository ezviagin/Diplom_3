import pytest

from selenium import webdriver
from user_api.stellar_burger_api import User


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def clean_cookies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def user():
    user = User()
    user.create_user()
    yield user
    user.delete_user()

'''
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.get(BASE_URL)
    yield driver

    driver.quit()
'''
