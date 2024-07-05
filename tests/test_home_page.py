import allure

from conftest import driver, user
from helpers.urls import *
from pages.home_page import HomePage
from pages.personal_space_page import PersonalSpacePage


@allure.feature("Домашняя страница")
class TestHomePage:
    @allure.title("Лента Заказов")
    @allure.description("Переход по кнопке \"Лента Заказов\" в шапке")
    def test_click_on_order_feed_button(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_order_feed_button()
        page.wait_for_order_feed_header()
        assert page.current_url() == f"{BASE_URL}{FEED}"

    @allure.title("Конструктор")
    @allure.description("Переход по кнопке \"Конструктор\" в шапке")
    def test_click_on_constructor_button(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.wait_for_assemble_burger_title()
        assert page.current_url() == BASE_URL

    @allure.title("Появление всплывающего окна с деталями ингредиента")
    @allure.description("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_popup_windows_shown(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_ingredient()
        assert page.wait_for_ingredient_details_title().text == "Детали ингредиента"

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    @allure.description("Всплывающее окно закрывается кликом по крестику")
    def test_popup_windows_is_closed_by_click_on_cross(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_ingredient()
        page.wait_for_ingredient_details_title()
        page.click_close_popup_ingredient_window()
        is_closed = page.wait_for_popup_ingredient_window()
        assert is_closed is True

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.description("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_drag_and_drop_fluorescent_bun(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.drag_and_drop_fluorescent_bun()
        assert page.get_ingredient_num_in_order() > 0

    @allure.title("Оформление заказа")
    @allure.description("Оформить заказ авторизированным пользователем")
    def test_create_order_with_logged_in_user(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        ps_page = PersonalSpacePage(driver)
        ps_page.set_email(user.get_email())
        ps_page.set_password(user.get_password())
        ps_page.wait_for_visibility_enter_button()
        ps_page.click_enter_button()
        page.wait_for_create_order_button()
        page.drag_and_drop_fluorescent_bun()
        page.click_create_order_button()
        page.wait_for_close_popup_ingredient_window_button()
        assert page.get_your_order_is_being_prepared_field().text == "Ваш заказ начали готовить"
