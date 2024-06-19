from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, "//input[contains(@name,'name')]")

    # Поле ввода password
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@name,'Пароль')]")

    # Кнопка "Войти"
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
