from selenium.webdriver.common.by import By


class HomePageLocators:
    # Кнопка "Лента Заказов" в шапке
    ORDER_FEED_HEADER_BUTTON = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")

    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR_HEADER_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")

    # Кнопка "Личный кабинет" в шапке
    PERSONAL_SPACE_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")

    # Заголовок "Лента заказов" в /feed
    ORDER_FEED_TITLE = (By.XPATH, ".//h1[contains(text(), 'Лента заказов')]")

    # Заголовок "Соберите бургер" на домашней странице
    ASSEMBLE_BURGER_TITLE = (By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")

    # Кнопка "Флюорисцентная булка"
    FLUORESCENT_BUN_BUTTON = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")

    # Заголовок всплывающего окна "
    INGREDIENT_DETAILS_TITLE = (By.XPATH, ".//h2[contains(text(),'Детали ингредиента')]")

    # Кнопка закрытия всплывающего окна (крестик)
    CROSS_CLOSE_BUTTON = (By.XPATH, "(.//button[@type='button' and contains(@class, 'modal__close')])[1]")

    # Всплывающее окно со списком ингредиентов в заказе
    #INGREDIENT_DETAILS_POPUP_WINDOW = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")
    INGREDIENT_DETAILS_POPUP_WINDOW = (By.XPATH, "(.//div[@class='Modal_modal__container__Wo2l_'])[1]")

    # Поле для перетаскивания ингредиентов
    ADD_TO_ORDER_FIELD = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    # Флюорисцентная булка
    FLUORESCENT_BUN = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")

    # Счетчик добавления флюорисцентной булочки
    COUNTER_FLUORESCENT_BUN = (By.CSS_SELECTOR, "[class='counter_counter__num__3nue1']")

    # Кнопка "Создать заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")

    # Текст "Ваш заказ начали готовить" на всплывающем окне после офомрления заказа
    YOUR_ORDER_IS_BEING_PREPARED = (By.XPATH, ".//p[contains(text(),'Ваш заказ начали готовить')]")

    # Элемент, перекрывающий всю страницу и иногда не дающий нажать на кнопку
    MODAL_OVERLAY_ELEMENT = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")

    # Новый номер заказа
    NEW_ORDER_NUMBER = (
        By.XPATH,
        ".//h2[contains(@class,'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
        "text_type_digits-large mb-8')]",
    )
