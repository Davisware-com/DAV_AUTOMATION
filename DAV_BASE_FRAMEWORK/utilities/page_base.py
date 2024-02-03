# import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    # @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    def click_element(self, locator, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            element.click()
            print("Element clicked successfully")
        except Exception as e:
            print(f"Failed to click element: {str(e)}")

    def send_keys_to_element(self, locator, keys, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            element.send_keys(keys)
        except Exception as e:
            print(f"Failed to send keys: {str(e)}")

    def get_text_from_element(self, locator, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            element_text = element.text
            return element_text
        except Exception as e:
            print(f"Failed to get element text: {str(e)}")
            return None

    def find_element(self, locator, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")
            return element
        except Exception as e:
            print(f"Failed to find element: {str(e)}")
            return None

    def find_elements(self, locator, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                elements = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((By.ID, value))
                )
            elif selector.lower() == "name":
                elements = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                elements = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                elements = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")
            return elements
        except Exception as e:
            print(f"Failed to find elements: {str(e)}")
            return None

    def scroll_to_element(self, locator):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = self.driver.find_element(By.ID, value)
            elif selector.lower() == "name":
                element = self.driver.find_element(By.NAME, value)
            elif selector.lower() == "xpath":
                element = self.driver.find_element(By.XPATH, value)
            elif selector.lower() == "css":
                element = self.driver.find_element(By.CSS_SELECTOR, value)
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except Exception as e:
            print(f"Failed to scroll to element: {str(e)}")

    def find_element_and_send_keys(self, locator, keys, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            element.send_keys(keys)
        except Exception as e:
            print(f"Failed to find element or send keys: {str(e)}")

    def find_element_and_get_text(self, locator, timeout=10):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, value))
                )
            elif selector.lower() == "name":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.NAME, value))
                )
            elif selector.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, value))
                )
            elif selector.lower() == "css":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, value))
                )
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            element_text = element.text
            print("Element text:", element_text)
            return element_text
        except Exception as e:
            print(f"Failed to find element or retrieve text: {str(e)}")
            return None

    def is_element_present(self, locator):
        try:
            selector = locator.split("-->")[0]
            value = locator.split("-->")[1]

            if selector.lower() == "id":
                self.driver.find_element(By.ID, value)
            elif selector.lower() == "name":
                self.driver.find_element(By.NAME, value)
            elif selector.lower() == "xpath":
                self.driver.find_element(By.XPATH, value)
            elif selector.lower() == "css":
                self.driver.find_element(By.CSS_SELECTOR, value)
            else:
                raise ValueError(f"Invalid locator strategy: {selector}")

            return True
        except NoSuchElementException:
            return False


