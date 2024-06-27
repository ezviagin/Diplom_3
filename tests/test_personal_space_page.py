import allure

from conftest import driver, user
from pages.personal_space_page import PersonalSpacePage
from pages.account_page import AccountPage
from helpers.urls import *


@allure.title("Тестирование Личного кабинета")
class TestPersonalSpacePage:
    @allure.description("Переход по клику \"Личный кабинет\"")
    def test_click_on_personal_space_button(self, driver):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        login_page = AccountPage(driver)
        login_page.wait_for_visibility_enter_button()
        assert login_page.current_url() == f"{BASE_URL}{USER_LOGIN}"

    @allure.description("Переход в раздел \"История заказов\" в Личном кабинете")
    def test_click_on_order_history(self, driver, user):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.wait_for_create_order_button()
        page.click_on_personal_space_button()
        page.wait_for_you_can_change_personal_data_text_hint()
        page.click_on_order_history_button()
        page.wait_for_you_can_change_personal_data_text_hint()
        assert page.current_url() == f"{BASE_URL}{ORDER_HISTORY}"

    @allure.title("Проверка выхода из аккаунта при нажатии кнопки \"Выйти\" в Личном кабинете")
    def test_click_logout_page(self, driver, user):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.wait_for_create_order_button()
        page.click_on_personal_space_button()
        page.wait_for_logout_button_is_clickable()
        page.click_on_logout_button()
        page.wait_for_visibility_login_button()
        assert page.current_url() == f"{BASE_URL}{USER_LOGIN}"


@allure.title("Тестирование восстановления пароля пользователя")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке \"Восстановить пароль\"")
    def test_click_on_password_recovery_button(self, driver, user):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.wait_for_visibility_enter_into_account_button()
        page.click_enter_into_account_button()
        page.wait_for_password_recovery_button()
        page.click_on_password_recovery_button()
        assert page.current_url() == f"{BASE_URL}{USER_FORGOT_PASSWORD}"

    @allure.title("Ввод почты и клик по кнопке \"Восстановить\"")
    def test_recover_user_password(self, driver, user):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.wait_for_visibility_enter_into_account_button()
        page.click_enter_into_account_button()
        page.wait_for_password_recovery_button()
        page.click_on_password_recovery_button()
        page.set_email(user.get_email())
        page.click_on_recover_password_button()
        page.wait_for_email_and_recovery_code_button()
        assert page.current_url() == f"{BASE_URL}{USER_PASSWORD_RESET}"

    @allure.description("Проверка кнопки показать/скрыть пароль в форме восстановления пароля")
    def test_show_hide_password_button(self, driver, user):
        page = PersonalSpacePage(driver)
        page.navigate(BASE_URL)
        page.wait_for_visibility_enter_into_account_button()
        page.click_enter_into_account_button()
        page.click_password_recovery_button()
        page.set_email(user.get_email())
        page.click_on_recover_password_button()
        page.wait_for_email_and_recovery_code_button()
        page.set_new_password()
        page.click_show_hide_password_button()
        assert page.get_parent_class_password_field() == page.assign_parent_class_password_by_variable()
