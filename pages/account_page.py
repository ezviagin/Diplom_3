import allure

from conftest import driver
from locators.account_page_locators import AccountPageLocators
from locators.personal_space_locators import PersonalSpaceLocators
from pages.home_page import HomePage


class AccountPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Вводим email")
    def set_email(self, email):
        self._enter_text(AccountPageLocators.EMAIL_FIELD, email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        self._enter_text(AccountPageLocators.PASSWORD_FIELD, password)

    @allure.step("Клик по кнопке \"Восстановить пароль\"")
    def click_password_recovery_button(self):
        self._click_element(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Ожидание наличия кнопки Войти")
    def wait_for_visibility_enter_button(self):
        return self._element_is_visible(AccountPageLocators.ENTER_BUTTON)

    @allure.step("Кликаем по кнопке Войти")
    def click_enter_button(self):
        self._click_element(AccountPageLocators.ENTER_BUTTON)

    @allure.step("Ожидание наличия кнопки \"Войти в аккаунт\"")
    def wait_for_visibility_enter_into_account_button(self):
        return self._element_is_visible(AccountPageLocators.ENTER_INTO_ACCOUNT_BUTTON)

    @allure.step("Кликаем по кнопке \"Войти в аккаунт\"")
    def click_enter_into_account_button(self):
        self._click_element(AccountPageLocators.ENTER_INTO_ACCOUNT_BUTTON)

    @allure.step("Ввод нового пароля в форме \"Восстановление пароля\"")
    def set_new_password(self, password: str = 'Random123!'):
        self._enter_text(AccountPageLocators.SET_NEW_PASSWORD, password)

    @allure.step("Нажимаем кнопку Показать/спрятать пароль")
    def click_show_hide_password_button(self):
        self._click_element(AccountPageLocators.SHOW_HIDE_PASS_BUTTON)

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self._find_element(AccountPageLocators.PASSWORD_FIELD_PARENT)

    @allure.step("Присваиваем переменной родительский класс поля Пароль")
    def assign_parent_class_password_by_variable(self):
        return self._find_element(AccountPageLocators.HIGHLIGHTED_PASSWORD_FIELD)

    def wait_for_order_history_button(self):
        return self._element_is_visible(PersonalSpaceLocators.ORDERS_HISTORY_BUTTON)

