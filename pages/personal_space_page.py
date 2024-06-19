import allure

from conftest import driver
from locators.account_page_locators import AccountPageLocators
from locators.personal_space_locators import PersonalSpaceLocators
from pages.home_page import HomePage


class PersonalSpacePage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_you_can_change_personal_data_text_hint(self):
        super()._element_is_visible(PersonalSpaceLocators.HERE_YOU_CAN_CHANGE_PERSONAL_DATA_HINT)

    def click_on_order_history_button(self):
        super()._click_element(PersonalSpaceLocators.ORDERS_HISTORY_BUTTON)

    def click_on_logout_button(self):
        super()._click_element(PersonalSpaceLocators.LOGOUT_BUTTON)

    def wait_for_password_recovery_button(self):
        return super()._element_is_visible(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)

    def click_on_password_recovery_button(self):
        super()._click_element(AccountPageLocators.PASSWORD_RECOVERY_BUTTON)

    def click_on_recover_password_button(self):
        super()._click_element(AccountPageLocators.RECOVER_BUTTON)

    def wait_for_email_and_recovery_code_button(self):
        return super()._element_is_visible(AccountPageLocators.SAVE_BUTTON)
