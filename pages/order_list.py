import allure

from conftest import driver
from locators.order_list_locators import OrderListLocators
from pages.account_page import AccountPage


class OrderListPage(AccountPage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждем кликабельности по номеру последнего заказа")
    def wait_clickable_last_order(self):
        return self._wait_for_element_is_clickable(OrderListLocators.LAST_ORDER)

    @allure.step("Кликаем по последнему заказу")
    def click_last_order(self):
        button = self._click_element(OrderListLocators.LAST_ORDER)

    @allure.step("Получение списка заказов в работе и последних готовых")
    def get_orders_list(self):
        return self._find_element(OrderListLocators.ORDERS_LIST).text

    @allure.step("Получение количества выполненных сегодня заказов")
    def get_completed_orders_today(self):
        return self._find_elements(OrderListLocators.COUNTER_COMPLETED_FOR_TODAY)[1].text

    @allure.step("Получение количества выполненных за все время заказов")
    def get_completed_orders_all_days(self):
        return self._find_elements(OrderListLocators.COUNTER_COMPLETED_FOR_ALL_TIME)[0].text

    @allure.step("Ожидание видимости счетчика выполненных за сегодня заказов")
    def wait_for_visibility_completed_orders_today(self):
        return self._element_is_visible(OrderListLocators.COUNTER_COMPLETED_FOR_TODAY)

    @allure.step("Проверка наличия открытого окна с информацией о заказе")
    def get_info_order_window(self):
        element = self._find_elements(OrderListLocators.CLOSE_ORDER_INFO_BUTTON)[1]
        if element.is_displayed():
            return True
        return False

    @allure.step("Ожидаем видимости номера заказа в окне информации о заказе")
    def wait_for_visibility_order_number_in_info_window(self):
        return self._element_is_visible(OrderListLocators.ORDER_NUMBER_IN_INFO_WINDOW)

    @allure.step("Получаем номер последнего заказа в Работе")
    def get_order_list_in_work(self):
        return self._find_element(OrderListLocators.ALL_ORDER_NUMBERS_IN_ORDER_LIST).text

    @allure.step("Ожидаем кликабельности кнопки-крестика вплывающего окна \"Ваш заказ начали готовить\"")
    def wait_for_clickable_close_success_order_window_button(self):
        return self._wait_for_element_is_clickable(OrderListLocators.CLOSE_SUCCESS_ORDER_WINDOW_BUTTON)

    @allure.step("Закрыть окно \"Заказ успешно создан\"")
    def close_success_order_window(self):
        self._click_element(OrderListLocators.CLOSE_SUCCESS_ORDER_WINDOW_BUTTON)

    @allure.step("Ожидаем появления номера заказа в Работе")
    def wait_for_visibility_order_number_in_work(self):
        return self._element_is_visible(OrderListLocators.ORDER_IN_WORK)
