from selenium.webdriver.common.by import By


class OrderListLocators:
    # Выбор последнего заказа из ленты (первый элемент массива заказов на странице)
    LAST_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]")

    # Ингредиенты последнего заказа в сплывающем окне просмотра последнего заказа
    ORDER_NUMBER_IN_INFO_WINDOW = (By.XPATH, ".//ul[@class='Modal_list__2sHWc']")

    # Кнопка-крестик закрытия информации о последнем заказе
    CLOSE_ORDER_INFO_BUTTON = (
        By.XPATH,
        ".//button [@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type= 'button']"
    )

    CLOSE_SUCCESS_ORDER_WINDOW_BUTTON = (
        By.CSS_SELECTOR,
        "[class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']",
    )

    # Список заказов
    ORDERS_LIST = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']")

    # Счетчик заказов за сегодня
    COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    # Счетчик заказов за всё время
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, ".//p [@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    # Последний заказ в работе
    IN_WORK_CHAPTER = (By.XPATH, ".//ul[@class= 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")

    # Последний заказ в списке "В работе"
    ORDER_IN_WORK = (By.XPATH, ".//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")

