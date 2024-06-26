import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать кнопку \"Лента Заказов\"")
    def click_order_feed_button(self):
        return self._click_element(HomePageLocators.ORDER_FEED_HEADER_BUTTON, timeout=600)

    @allure.step("Дрождаться появления заголовка \"Лента заказов\"")
    def wait_for_order_feed_header(self):
        return self._element_is_visible(HomePageLocators.ORDER_FEED_TITLE)

    @allure.step("Нажать кнопку \"Конструктор\"")
    def click_constructor_button(self):
        return self._click_element(HomePageLocators.CONSTRUCTOR_HEADER_BUTTON)

    @allure.step("Дождаться появления заголовка \"Соберите бургер\"")
    def wait_for_assemble_burger_title(self):
        return self._element_is_visible(HomePageLocators.ASSEMBLE_BURGER_TITLE)

    @allure.step("Нажать на ингредиент \"Флюорисцентная булка\"")
    def click_ingredient(self):
        self._click_element(HomePageLocators.FLUR_BUN_BUTTON)

    @allure.step("Дождаться появления заголовка всплывающего окна \"Детали ингредиента\"")
    def wait_for_ingredient_details_title(self):
        return self._element_is_visible(HomePageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Нажать на закрытие всплывающего окна с ингредиентом (крестик)")
    def click_close_popup_ingredient_window(self):
        self._click_element(HomePageLocators.CROSS_CLOSE_BUTTON)

    @allure.step("Дождаться появление кнопки закрытия всплывающего окна с ингредиентом (крестик)")
    def wait_for_close_popup_ingredient_window_button(self):
        return self._is_element_displayed(HomePageLocators.CROSS_CLOSE_BUTTON, timeout=30)

    @allure.step("Перетащить Флюорисцентную булочку в поле заказа")
    def drag_and_drop_flur_bun(self):
        src = self._find_element(HomePageLocators.FLUORESCENT_BUN)
        tgt = self._find_element(HomePageLocators.ADD_TO_ORDER_FIELD)
        return self._drag_and_drop(src, tgt)

    @allure.step("Получить счетчик ингредиентов")
    def get_ingredient_num_in_order(self):
        return int(self._find_element(HomePageLocators.COUNTER_FLUORESCENT_BUN).text)

    @allure.step("Нажать кнопку \"Личный кабинет\"")
    def click_on_personal_space_button(self):
        self._click_element(HomePageLocators.PERSONAL_SPACE_BUTTON)

    @allure.step("Нажать кнопку \"Создать заказ\"")
    def click_create_order_button(self):
        self._click_element_js(HomePageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Прочитать поле, куда приходит уведомление, что заказ начал готовиться")
    def get_your_order_is_being_prepared_field(self):
        return self._is_element_displayed(HomePageLocators.YOUR_ORDER_IS_BEING_PREPARED)

    @allure.step("Дождаться появления кнопки \"Создать заказ\"")
    def wait_for_create_order_button(self):
        return self._is_element_displayed(HomePageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Дождаться, когда исчезнет перекрывающий страницу элемент Modal Overlay")
    def wait_for_modal_overlay_to_disappear(self):
        self.wait_for_element_to_disappear(HomePageLocators.MODAL_OVERLAY_ELEMENT)

    @allure.step("Дождаться прогрузки картинки при оформлении заказа")
    def wait_for_visibility_load_img(self):
        return self._element_is_visible(HomePageLocators.LOADING_IMG_ORDER_FORMATION)

    @allure.step("Получить номер созданного заказа")
    def get_new_order_number(self):
        return self._find_element(HomePageLocators.NEW_ORDER_NUMBER).text
