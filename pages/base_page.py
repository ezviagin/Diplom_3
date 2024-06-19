import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import helpers.urls as url


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def navigate(self, page_url: str = url.BASE_URL):
        self.driver.get(page_url)

    @allure.step('Получить текущий URL страницы')
    def current_url(self):
        return self.driver.current_url.rstrip('/')

    def _find_element(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                             f"Can't find element by locator {locator}")
        except TimeoutError:
            return None

    def _find_elements(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                                             f"Can't find elements by locator {locator}")
        except TimeoutError:
            return None

    def _click_element(self, locator: tuple[str, str], timeout: int = 10):
        element = self._find_element(locator, timeout)
        if element:
            element.click()
        else:
            return

    def _enter_text(self, locator: tuple[str, str], text: str, timeout: int = 10):
        element = self._find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            return None

    def _element_is_visible(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutError:
            return False

    def _element_is_present(self, locator: tuple[str, str], timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            return True
        except TimeoutError:
            return False

    def _scroll_to_element(self, locator: tuple[str, str], timeout: int = 10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self._find_element(locator))
        self._element_is_visible(locator, timeout)

    @allure.step('Нажать Enter для завершения выбора')
    def _press_enter_button(self, locator: tuple[str, str], timeout: int = 10):
        self._find_element(locator, timeout).send_keys(Keys.ENTER)

    @allure.step('Переключить вкладку по номеру')
    def _switch_to(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Закрыть вкладку')
    def _close_page(self):
        self.driver.close()

    @allure.step('Дождаться отображения URL страницы')
    def _wait_for_url(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until_not(ec.url_matches('about:blank'))

    @allure.step("Перетащить элемент")
    def _drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self.driver)
        return actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Проверка отображения элемента")
    def _is_element_displayed(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        try:
            element = self._find_element(locator, timeout)
            return element.is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False