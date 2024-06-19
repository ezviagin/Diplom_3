import pytest

from selenium import webdriver
from pages.base_page import BasePage
from user_api.stellar_burger_api import User
from helpers.urls import BASE_URL


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = User()
    user.create_user()
    yield user
    user.delete_user()
