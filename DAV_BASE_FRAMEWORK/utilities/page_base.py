from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PageBase:
    """
    write all customized methods here
    """
    LOCATOR_TYPES = {
        'id': By.ID,
        'name': By.NAME,
        'xpath': By.XPATH,
        'css': By.CSS_SELECTOR,
        'class': By.CLASS_NAME,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag_name': By.TAG_NAME
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.open()

    def get_locator(self, locator):
        try:
            selector, value = locator.split("-->")
            locator_type = selector.lower().strip()

            if locator_type in self.LOCATOR_TYPES:
                return self.LOCATOR_TYPES[locator_type], value.strip()
            else:
                raise ValueError(f"Invalid locator: {locator_type}")

        except (ValueError, AttributeError) as e:
            raise ValueError(f"Error parsing locator: {locator}. {e}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((self.get_locator(locator)))
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((self.get_locator(locator)))
        )

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def double_click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).context_click(element).perform()

    def send_keys_to_element(self, locator, keys, timeout=10):
        element = self.find_element(locator, timeout)
        element.send_keys(keys)

    def is_element_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.get_locator(locator))
        )

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def clear_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()

    def perform_drag_and_drop(self, source_locator, target_locator, timeout=10):
        source_element = self.find_element(source_locator, timeout)
        target_element = self.find_element(target_locator, timeout)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def switch_to_frame(self, locator, timeout=10):
        frame_element = self.find_element(locator, timeout)
        self.driver.switch_to.frame(frame_element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def is_element_displayed(self, locator, timeout=10):
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()

        except NoSuchElementException:
            return False

    def is_element_enabled(self, locator, timeout=10):
        try:
            element = self.find_element(locator, timeout)
            return element.is_enabled()

        except NoSuchElementException:
            return False

    def key_down_element(self, key):
        ActionChains(self.driver).key_down(key).perform()
