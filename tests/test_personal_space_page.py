import allure

from conftest import driver, user
from pages.home_page import HomePage
from pages.personal_space_page import PersonalSpacePage
from helpers.urls import *


@allure.feature("Личный кабинет")
class TestPersonalSpacePage:
    @allure.title("Переход в \"Личный кабинет\"")
    @allure.description("Переход по клику \"Личный кабинет\"")
    def test_click_on_personal_space_button(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        ps_page = PersonalSpacePage(driver)
        ps_page.wait_for_visibility_enter_button()
        assert ps_page.current_url() == f"{BASE_URL}{USER_LOGIN}"

    @allure.title("История заказов")
    @allure.description("Переход в раздел \"История заказов\" в Личном кабинете")
    def test_click_on_order_history(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        ps_page = PersonalSpacePage(driver)
        page.click_on_personal_space_button()
        ps_page.set_email(user.get_email())
        ps_page.set_password(user.get_password())
        ps_page.click_enter_button()
        page.wait_for_create_order_button()
        page.click_on_personal_space_button()
        ps_page.wait_for_you_can_change_personal_data_text_hint()
        ps_page.click_on_order_history_button()
        ps_page.wait_for_you_can_change_personal_data_text_hint()
        assert page.current_url() == f"{BASE_URL}{ORDER_HISTORY}"

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта при нажатии кнопки \"Выйти\" в Личном кабинете")
    def test_click_logout_page(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        ps_page = PersonalSpacePage(driver)
        ps_page.set_email(user.get_email())
        ps_page.set_password(user.get_password())
        ps_page.click_enter_button()
        page.wait_for_create_order_button()
        page.click_on_personal_space_button()
        ps_page.wait_for_logout_button_is_clickable()
        ps_page.click_on_logout_button()
        ps_page.wait_for_visibility_login_button()
        assert page.current_url() == f"{BASE_URL}{USER_LOGIN}"


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Страница восстановления пароля")
    @allure.description("Переход на страницу восстановления пароля по кнопке \"Восстановить пароль\"")
    def test_click_on_password_recovery_button(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        ps_page = PersonalSpacePage(driver)
        ps_page.wait_for_visibility_enter_into_account_button()
        ps_page.click_enter_into_account_button()
        ps_page.wait_for_password_recovery_button()
        ps_page.click_on_password_recovery_button()
        assert ps_page.current_url() == f"{BASE_URL}{USER_FORGOT_PASSWORD}"

    @allure.title("Восстановить пароль через email")
    @allure.description("Ввод почты и клик по кнопке \"Восстановить\"")
    def test_recover_user_password(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        ps_page = PersonalSpacePage(driver)
        ps_page.wait_for_visibility_enter_into_account_button()
        ps_page.click_enter_into_account_button()
        ps_page.wait_for_password_recovery_button()
        ps_page.click_on_password_recovery_button()
        ps_page.set_email(user.get_email())
        ps_page.click_on_recover_password_button()
        ps_page.wait_for_email_and_recovery_code_button()
        assert ps_page.current_url() == f"{BASE_URL}{USER_PASSWORD_RESET}"

    @allure.title("Показать/скрыть введенный пароль")
    @allure.description("Проверка кнопки показать/скрыть пароль в форме восстановления пароля")
    def test_show_hide_password_button(self, driver, user):
        ps_page = PersonalSpacePage(driver)
        ps_page.navigate(BASE_URL)
        ps_page.wait_for_visibility_enter_into_account_button()
        ps_page.click_enter_into_account_button()
        ps_page.click_password_recovery_button()
        ps_page.set_email(user.get_email())
        ps_page.click_on_recover_password_button()
        ps_page.wait_for_email_and_recovery_code_button()
        ps_page.set_new_password()
        ps_page.click_show_hide_password_button()
        assert ps_page.get_parent_class_password_field() == ps_page.assign_parent_class_password_by_variable()
