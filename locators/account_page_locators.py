from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, ".//input[contains(@name,'name')]")

    # Поле ввода password
    PASSWORD_FIELD = (By.XPATH, ".//input[contains(@name,'Пароль')]")

    # Кнопка "Войти"
    ENTER_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")

    # Кнопка "Войти"
    ENTER_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")

    # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[contains(text(),'Восстановить пароль')]")

    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, ".//button[contains(text(), 'Восстановить')]")

    # Кнопка "Сохранить"
    SAVE_BUTTON = (By.XPATH, ".//button[contains(text(),'Сохранить')]")

    # Кнопка показать/скрыть пароль
    SHOW_HIDE_PASS_BUTTON = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")

    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")

    # Поле ввода нового пароля
    SET_NEW_PASSWORD = (By.XPATH,
                        ".//input[@class='text input__textfield text_type_main-default' and @type= 'password']")

    # Подсвеченное поле пароля
    HIGHLIGHTED_PASSWORD_FIELD = (
        By.XPATH,
        ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")

    LOGIN_BUTTON = (By.XPATH, "(//button[contains(text(), 'Войти')])[1]")