from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, ".//input[contains(@name,'name')]")

    # Поле ввода password
    PASSWORD_FIELD = (By.XPATH, ".//input[contains(@name,'Пароль')]")

    # Кнопка "Войти"
    ENTER_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")

    # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[contains(text(),'Восстановить пароль')]")

    RECOVER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Восстановить')]")

    SAVE_BUTTON = (By.XPATH, ".//button[contains(text(),'Сохранить')]")

    SHOW_HIDE_PASS_BUTTON = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")

    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")

    INPUT_PASSWORD = (By.XPATH,".//input[@class='text input__textfield text_type_main-default' and @type= 'password']")

    HIGHLIGHTED_PASSWORD_FIELD = (
        By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")