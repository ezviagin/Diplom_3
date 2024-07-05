from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

import helpers.urls as url


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, page_url: str = url.BASE_URL):
        self.driver.get(page_url)

    def current_url(self):
        return self.driver.current_url.rstrip('/')

    def _find_element(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def _find_elements(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                                             f"Can't find elements by locator {locator}")
        except TimeoutException:
            return None

    def _click_element(self, locator: tuple[str, str], timeout: int = 10):
        element = self._find_element(locator, timeout)
        if element:
            element.click()
        else:
            return None

    def _click_element_js(self, locator: tuple[str, str], timeout: int = 10):
        element = self._find_element(locator, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            return None

    def _wait_for_element_to_be_clickable(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            return None

    def _enter_text(self, locator: tuple[str, str], text: str, timeout: int = 10):
        element = self._wait_for_element_to_be_clickable(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            return None

    def _element_is_visible(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def _element_is_present(self, locator: tuple[str, str], timeout: int = 10):
        try:
            self._find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def _scroll_to_element(self, locator: tuple[str, str], timeout: int = 10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self._find_element(locator))
        self._element_is_visible(locator, timeout)

    def _drag_and_drop(self, src, tgt):
        drag_and_drop(self.driver, src, tgt)

    def _is_element_displayed(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        try:
            element = self._find_element(locator, timeout)
            if element is not None:
                return element.is_displayed()
            else:
                return False
        except (NoSuchElementException, TimeoutException):
            return False

    def _wait_for_element_to_disappear(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until_not(ec.presence_of_element_located(locator))

    def _wait_for_element_is_clickable(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
