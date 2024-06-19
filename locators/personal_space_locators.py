from selenium.webdriver.common.by import By


class PersonalSpaceLocators:
    # Кнопка "История заказов"
    ORDERS_HISTORY_BUTTON = (By.XPATH, ".//a[contains(text(),'История заказов')]")

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(),'Выход')]")

    # Номер последнего заказа в Истории заказов
    LAST_ORDER_NUMBER = (By.XPATH, ".//p[@class= 'text text_type_digits-default']")

    # Подсказка при переходе в Личном кабинете
    HERE_YOU_CAN_CHANGE_PERSONAL_DATA_HINT = (By.XPATH, ".//p[contains(text(), 'В этом разделе вы можете изменить')]")
