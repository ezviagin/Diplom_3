from conftest import *
from helpers.urls import *
from pages.home_page import HomePage
from pages.order_list_page import OrderListPage
from pages.personal_space_page import PersonalSpacePage
from user_api.stellar_burger_api import *


@allure.feature("Лента заказов")
class TestOrderList:
    @allure.title("Детали заказа")
    @allure.description("Если кликнуть на заказ, появится всплывающее окно с деталями")
    def test_click_on_last_order(self, driver):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        ol_page = OrderListPage(driver)
        page.click_order_feed_button()
        ol_page.wait_clickable_last_order()
        ol_page.click_last_order()
        ol_page.wait_for_visibility_order_number_in_info_window()
        assert ol_page.get_info_order_window() is True

    @allure.title("История заказа пользователя")
    @allure.description("Заказы пользователя из раздела \"История заказов\" отображаются на странице \"Лента заказов\"")
    def test_user_orders_history_displayed_on_feed_orders(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page_ps = PersonalSpacePage(driver)
        page_ps.click_login(user.get_email(), user.get_password())
        page.wait_for_create_order_button()
        page.drag_and_drop_fluorescent_bun()
        page.click_create_order_button()
        ol_page = OrderListPage(driver)
        ol_page.wait_for_clickable_close_success_order_window_button()
        page.wait_for_close_popup_ingredient_window_button()
        page.click_close_popup_ingredient_window()
        page.click_on_personal_space_button()
        personal_page = PersonalSpacePage(driver)
        personal_page.wait_for_you_can_change_personal_data_text_hint()
        personal_page.click_on_order_history_button()
        personal_page.wait_for_order_list()
        expected_result = personal_page.get_last_order_number()
        page.click_order_feed_button()
        assert expected_result in ol_page.get_orders_list()

    @allure.title("Увеличение счётчика \"Выполнено за всё время\" при создании заказа")
    @allure.description("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increase_counter_completed_for_all_time(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()

        ps_page = PersonalSpacePage(driver)
        ps_page.click_login(user.get_email(), user.get_password())
        page.wait_for_create_order_button()
        page.click_order_feed_button()
        page.wait_for_order_feed_header()

        ol_page = OrderListPage(driver)
        current_num = ol_page.get_completed_orders_all_days()
        page.click_constructor_button()
        page.wait_for_create_order_button()
        page.drag_and_drop_fluorescent_bun()
        page.click_create_order_button()

        ol_page.wait_for_clickable_close_success_order_window_button()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()
        ol_page.wait_for_visibility_completed_orders_today()
        assert ol_page.get_completed_orders_all_days() > current_num

    @allure.title("Увеличение счётчика 'Выполнено за сегодня' при создании заказа")
    @allure.description("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increase_counter_completed_for_today(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page_ps = PersonalSpacePage(driver)
        page_ps.click_login(user.get_email(), user.get_password())
        page.wait_for_create_order_button()
        page.click_order_feed_button()

        ol_page = OrderListPage(driver)
        ol_page.wait_clickable_last_order()
        ol_page.wait_for_visibility_completed_orders_today()
        current = ol_page.get_completed_orders_today()

        page.click_constructor_button()
        page.wait_for_assemble_burger_title()
        page.drag_and_drop_fluorescent_bun()
        page.click_create_order_button()
        page.wait_for_close_popup_ingredient_window_button()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()

        ol_page.wait_for_visibility_completed_orders_today()
        today = ol_page.get_completed_orders_today()
        assert today > current

    @allure.title("Заказ в разделе 'В работе' после оформления")
    @allure.description("После оформления заказа его номер появляется в разделе \"В работе\"")
    def test_completed_order_appears_in_progress_section(self, driver, user):
        page = HomePage(driver)
        page.navigate(BASE_URL)
        page.click_on_personal_space_button()
        page_ps = PersonalSpacePage(driver)
        page_ps.click_login(user.get_email(), user.get_password())
        page.wait_for_create_order_button()
        page.drag_and_drop_fluorescent_bun()
        page.click_create_order_button()
        page.wait_for_popup_ingredient_window()
        ol_page = OrderListPage(driver)
        ol_page.wait_for_clickable_close_success_order_window_button()
        page.wait_for_popup_ingredient_window()
        new_order_num = page.get_new_order_number()
        page.click_close_popup_ingredient_window()
        page.click_order_feed_button()
        page.wait_for_order_feed_header()
        orders_in_work_list = ol_page.get_order_list_in_work()
        assert new_order_num in orders_in_work_list
