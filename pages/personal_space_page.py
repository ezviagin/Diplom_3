import allure

from conftest import driver
from locators.personal_space_locators import PersonalSpaceLocators
from pages.base_page import BasePage


class PersonalSpacePage(BasePage):
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
        return self._element_is_visible(PersonalSpaceLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Нажать на кнопку \"Восстановить пароль\"")
    def click_on_password_recovery_button(self):
        self._click_element(PersonalSpaceLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Нажать на кнопку \"Востановить\"")
    def click_on_recover_password_button(self):
        self._click_element(PersonalSpaceLocators.RECOVERY_BUTTON)

    @allure.step("Дождаться появления кнопки \"Сохранить\"")
    def wait_for_email_and_recovery_code_button(self):
        return self._element_is_visible(PersonalSpaceLocators.SAVE_BUTTON)

    @allure.step("Дождаться, когда кнопка \"Выход\" станет кликабельной")
    def wait_for_logout_button_is_clickable(self):
        self._wait_for_element_is_clickable(PersonalSpaceLocators.LOGOUT_BUTTON)

    @allure.step("Дождаться появления кнопки \"Войти\"")
    def wait_for_visibility_login_button(self):
        return self._element_is_visible(PersonalSpaceLocators.LOGIN_BUTTON)

    @allure.step("Вводим email")
    def set_email(self, email):
        self._enter_text(PersonalSpaceLocators.EMAIL_FIELD, email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        self._enter_text(PersonalSpaceLocators.PASSWORD_FIELD, password)

    @allure.step("Клик по кнопке \"Восстановить пароль\"")
    def click_password_recovery_button(self):
        self._click_element(PersonalSpaceLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Ожидание наличия кнопки Войти")
    def wait_for_visibility_enter_button(self):
        return self._element_is_visible(PersonalSpaceLocators.ENTER_BUTTON)

    @allure.step("Кликаем по кнопке Войти")
    def click_enter_button(self):
        self._click_element_js(PersonalSpaceLocators.ENTER_BUTTON)

    @allure.step("Ожидание наличия кнопки \"Войти в аккаунт\"")
    def wait_for_visibility_enter_into_account_button(self):
        return self._element_is_visible(PersonalSpaceLocators.ENTER_INTO_ACCOUNT_BUTTON)

    @allure.step("Кликаем по кнопке \"Войти в аккаунт\"")
    def click_enter_into_account_button(self):
        self._click_element(PersonalSpaceLocators.ENTER_INTO_ACCOUNT_BUTTON)

    @allure.step("Ввод нового пароля в форме \"Восстановление пароля\"")
    def set_new_password(self, password: str = 'Random123!'):
        self._enter_text(PersonalSpaceLocators.SET_NEW_PASSWORD, password)

    @allure.step("Нажимаем кнопку Показать/спрятать пароль")
    def click_show_hide_password_button(self):
        self._click_element(PersonalSpaceLocators.SHOW_HIDE_PASS_BUTTON)

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self._find_element(PersonalSpaceLocators.PASSWORD_FIELD_PARENT)

    @allure.step("Присваиваем переменной родительский класс поля Пароль")
    def assign_parent_class_password_by_variable(self):
        return self._find_element(PersonalSpaceLocators.HIGHLIGHTED_PASSWORD_FIELD)

    @allure.step("Дождаться кнопки \"История заказов\"")
    def wait_for_order_history_button(self):
        return self._element_is_visible(PersonalSpaceLocators.ORDERS_HISTORY_BUTTON)

    @allure.step("Войти в аккаунт, выйти и войти, если пользователь авторизован")
    def click_login(self, email: str = '', password: str = ''):
        if self.is_you_can_change_personal_data_text_visible() is True:
            self.click_on_logout_button()
            self.wait_for_visibility_enter_button()

        self.set_email(email)
        self.set_password(password)
        self.click_enter_button()
