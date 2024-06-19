import allure
import pytest

from conftest import driver, user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from helpers.urls import *


class TestHomePage:
    @allure.description("Переход по кнопке \"Лента Заказов\" в шапке")
    def test_click_on_order_feed_button(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_order_feed_button()
        page.wait_for_order_feed_header()
        assert page.current_url() == f"{BASE_URL}{FEED}"

    @allure.description("Переход по кнопке \"Конструктор\" в шапке")
    def test_click_on_constructor_button(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.wait_for_assemble_burger_title()
        assert page.current_url() == BASE_URL

    @allure.description("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_popup_windows_shown(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_ingredient()
        assert page.wait_for_ingredient_details_title().text == "Детали ингредиента"

    @allure.description("Всплывающее окно закрывается кликом по крестику")
    def test_popup_windows_is_closed_by_click_on_cross(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_ingredient()
        page.wait_for_ingredient_details_title()
        page.click_close_popup_ingredient_window()
        assert page.wait_for_close_popup_ingredient_window_button() is False

    # TODO: fix locator, the test is failing
    @allure.description("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_drag_and_drop_fluor_bun(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.drag_and_drop_flur_bun()
        assert page.get_ingredient_num_in_order() > 0

    # В тесте создаётся и удаляется тестовый пользователь с помощью API согласно заданию
    # TODO: fix the locator for drag_and_drop above
    @allure.description("Оформить заказ авторизированным пользователем")
    def test_create_order_with_logged_in_user(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()

        login_page = LoginPage(driver)
        login_page.set_email(user.get_email())
        login_page.set_password(user.get_password())
        login_page.click_enter_button()
        login_page.wait_for_visibility_enter_button()

        page.drag_and_drop_flur_bun()
        page.click_create_order_button()

        assert page.get_your_order_is_being_prepared_field().text == "Ваш заказ начали готовить"
