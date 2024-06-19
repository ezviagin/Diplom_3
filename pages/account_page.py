import allure

from conftest import driver
from locators.account_page_locators import AccountPageLocators
from pages.home_page import HomePage


class AccountPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Вводим email")
    def set_email(self, email):
        email_input = self._find_element(AccountPageLocators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        password_input = self._find_element(AccountPageLocators.PASSWORD_FIELD)
        password_input.send_keys(password)

    @allure.step("Клик по кнопке \"Восстановить пароль\"")
    def click_password_recovery_button(self):
        button = self._find_element(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)
        button.click()

    @allure.step("Ожидание наличия кнопки Войти")
    def wait_for_visibility_enter_button(self):
        return self._element_is_visible(AccountPageLocators.ENTER_BUTTON)

    @allure.step("Кликаем по кнопке Войти")
    def click_enter_button(self):
        button = self._find_element(AccountPageLocators.ENTER_BUTTON)
        button.click()

