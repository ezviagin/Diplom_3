import pytest

from selenium import webdriver
from user_api.stellar_burger_api import User


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = User()
    user.create_user()
    yield user
    user.delete_user()
