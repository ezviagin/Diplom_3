import allure

from conftest import driver, user
from helpers.urls import *
from pages.order_list import OrderListPage
from pages.personal_space_page import PersonalSpacePage


@allure.title("Тестирование Ленты заказов")
class TestFeedOrders:
    @allure.description("Если кликнуть на заказ, появится всплывающее окно с деталями")
    def test_click_on_last_order(self, driver, user):
        page = OrderListPage(driver)
        page.navigate(BASE_URL)
        page.click_order_feed_button()
        page.wait_clickable_last_order()
        page.click_last_order()
        page.wait_for_visibility_order_number_in_info_window()
        assert page.get_info_order_window() is True

    @allure.description("Заказы пользователя из раздела «История заказов» отображаются на странице \"Лента заказов\"")
    def test_user_orders_history_displayed_on_feed_orders(self, driver, user):
        page = OrderListPage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.wait_for_create_order_button()
        page.drag_and_drop_flur_bun()
        page.click_create_order_button()
        page.wait_for_clickable_close_success_order_window_button()
        page.wait_for_close_popup_ingredient_window_button()
        page.click_close_popup_ingredient_window()
        page.click_on_personal_space_button()
        personal_page = PersonalSpacePage(driver)
        personal_page.wait_for_you_can_change_personal_data_text_hint()
        personal_page.click_on_order_history_button()
        personal_page.wait_for_order_list()
        expected_result = personal_page.get_last_order_number()
        page.click_order_feed_button()
        assert expected_result in page.get_orders_list()

    @allure.description("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increase_counter_completed_for_all_time(self, driver, user):
        page = OrderListPage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.click_order_feed_button()
        page.wait_for_visibility_completed_orders_today()
        current_quantity = page.get_completed_orders_all_days()
        page.click_constructor_button()
        page.wait_for_create_order_button()
        page.drag_and_drop_flur_bun()
        page.click_create_order_button()
        page.wait_for_clickable_close_success_order_window_button()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()
        page.wait_for_visibility_completed_orders_today()
        assert page.get_completed_orders_all_days() > current_quantity

    @allure.description("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increase_counter_completed_for_today(self, driver, user):
        page = OrderListPage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.wait_for_create_order_button()
        page.click_order_feed_button()
        page.wait_clickable_last_order()
        page.wait_for_visibility_completed_orders_today()
        current = page.get_completed_orders_today()
        page.click_constructor_button()
        page.wait_for_assemble_burger_title()
        page.drag_and_drop_flur_bun()
        page.click_create_order_button()
        page.wait_for_close_popup_ingredient_window_button()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()
        page.wait_for_visibility_completed_orders_today()
        assert page.get_completed_orders_today() > current

    @allure.description("После оформления заказа его номер появляется в разделе \"В работе\"")
    def test_completed_order_appears_in_progress_section(self, driver, user):
        page = OrderListPage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page.set_email(user.get_email())
        page.set_password(user.get_password())
        page.click_enter_button()
        page.wait_for_create_order_button()
        page.drag_and_drop_flur_bun()
        page.click_create_order_button()
        page.wait_for_clickable_close_success_order_window_button()
        page.wait_for_visibility_load_img()

        new_order_number = page.get_new_order_number()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()
        page.wait_for_order_feed_header()
        list_orders_in_work = page.get_order_list_in_work()
        assert new_order_number in list_orders_in_work
