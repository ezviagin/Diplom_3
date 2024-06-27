import allure

from conftest import driver
from locators.account_page_locators import AccountPageLocators
from locators.personal_space_locators import PersonalSpaceLocators
from pages.account_page import AccountPage


class PersonalSpacePage(AccountPage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание появления подсказки \"В этом разделе вы можете изменить свои персональные данные\" "
                 "в Личном Кабинете ")
    def wait_for_you_can_change_personal_data_text_hint(self):
        return self._element_is_visible(PersonalSpaceLocators.HERE_YOU_CAN_CHANGE_PERSONAL_DATA_HINT)

    @allure.step("Проверка видимости подсказки \"В этом разделе вы можете изменить свои персональные данные\" "
                 "в Личном Кабинете ")
    def is_you_can_change_personal_data_text_visible(self):
        return self._is_element_displayed(PersonalSpaceLocators.HERE_YOU_CAN_CHANGE_PERSONAL_DATA_HINT, timeout=3)

    @allure.step("Нажать кнопку \"История заказов\"")
    def click_on_order_history_button(self):
        self._click_element(PersonalSpaceLocators.ORDERS_HISTORY_BUTTON)

    @allure.step("Нажать кнопку \"Выйти\"")
    def click_on_logout_button(self):
        self._click_element_js(PersonalSpaceLocators.LOGOUT_BUTTON)

    @allure.step("Дождаться появления на странице номера последнего заказа")
    def wait_for_order_list(self):
        return self._element_is_visible(PersonalSpaceLocators.LAST_ORDER_NUMBER)

    @allure.step("Получить номер последнего заказа")
    def get_last_order_number(self):
        return self._find_element(PersonalSpaceLocators.LAST_ORDER_NUMBER).text

    @allure.step("Дождаться появления кнопки \"Восстановить пароль\"")
    def wait_for_password_recovery_button(self):
        return self._element_is_visible(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Нажать на кнопку \"Восстановить пароль\"")
    def click_on_password_recovery_button(self):
        self._click_element(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Нажать на кнопку \"Востановить\"")
    def click_on_recover_password_button(self):
        self._click_element(AccountPageLocators.RECOVERY_BUTTON)

    @allure.step("Дождаться появления кнопки \"Сохранить\"")
    def wait_for_email_and_recovery_code_button(self):
        return self._element_is_visible(AccountPageLocators.SAVE_BUTTON)

    def wait_for_logout_button_is_clickable(self):
        self._wait_for_element_is_clickable(PersonalSpaceLocators.LOGOUT_BUTTON)

    @allure.step("Дождаться появления кнопки \"Войти\"")
    def wait_for_visibility_login_button(self):
        return self._element_is_visible(AccountPageLocators.LOGIN_BUTTON)

    @allure.step("Войти в аккаунт, выйти и войти, если пользователь авторизован")
    def click_login(self, email: str = '', password: str = ''):
        if self.is_you_can_change_personal_data_text_visible() is True:
            self.click_on_logout_button()
            self.wait_for_visibility_enter_button()

        self.set_email(email)
        self.set_password(password)
        self.click_enter_button()

