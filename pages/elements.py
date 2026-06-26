from selenium.common import exceptions as EXCEPT
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import add_root
from frame.logger import logger as log


class WebElement:

    def __init__(self, driver, xpath, timeout=10, wait_after_click=False):
        self._driver = driver
        self._locator = (By.XPATH, xpath)
        self._timeout = timeout
        self._wait_after_click = wait_after_click

    def find(self, timeout=None):
        timeout = timeout or self._timeout

        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
        except (EXCEPT.TimeoutException, EXCEPT.WebDriverException):
            log.info('Element not found: %s', self._locator)
            return None

    def is_presented(self):
        return self.find(timeout=1) is not None

    def is_displayed(self):
        element = self.find(timeout=1)
        return element.is_displayed() if element else False

    def wait_to_be_clickable(self, timeout=None):
        timeout = timeout or self._timeout

        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except (EXCEPT.TimeoutException, EXCEPT.WebDriverException):
            log.info('Element not clickable: %s', self._locator)
            return None

    def click(self):
        element = self.wait_to_be_clickable()

        if not element:
            raise AttributeError(f'Element not found: {self._locator}')

        ActionChains(self._driver).move_to_element(element).click().perform()

    def clear(self):
        self.find().clear()

    def send_keys(self, value):
        element = self.find()

        if not element:
            raise AttributeError(f'Element not found: {self._locator}')

        element.clear()
        element.send_keys(value)

    def get_text(self):
        element = self.find()
        return element.text if element else ""

    @property
    def text(self):
        return self.get_text()

    def get_attribute(self, name):
        element = self.find()
        return element.get_attribute(name) if element else None

    def select(self, text):
        Select(self.find()).select_by_visible_text(text)

    def scroll_into_view(self):
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            self.find()
        )

    def screenshot(self, filename):
        self.scroll_into_view()

        self._driver.execute_script(
            "arguments[0].style.border='3px solid red'",
            self.find()
        )

        self._driver.save_screenshot(filename)


class ManyWebElements(WebElement):

    def find(self, timeout=None):
        timeout = timeout or self._timeout

        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except (EXCEPT.TimeoutException, EXCEPT.WebDriverException):
            log.info('Elements not found: %s', self._locator)
            return []

    def __getitem__(self, index):
        return self.find()[index]

    def __iter__(self):
        return iter(self.find())

    def __len__(self):
        return len(self.find())

    def count(self):
        return len(self)

    @property
    def text(self):
        return [element.text for element in self.find()]

    def get_text(self):
        return self.text

    def get_attribute(self, name):
        return [element.get_attribute(name) for element in self.find()]

    def click(self):
        raise NotImplementedError(
            "ManyWebElements does not support click(). "
            "Select an element first, e.g. buttons[0].click()."
        )

    def send_keys(self, value):
        raise NotImplementedError(
            "ManyWebElements does not support send_keys()."
        )

    def clear(self):
        raise NotImplementedError(
            "ManyWebElements does not support clear()."
        )
