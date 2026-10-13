from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Сalculator:

    # Локаторы элементов страницы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SEVEN_INPUT = (By.XPATH, "//span[text()='7']")
    EIGHT_INPUT = (By.XPATH, "//span[text()='8']")
    PLUS_INPUT = (By.XPATH, "//span[text()='+']")
    EQUAL_INPUT = (By.XPATH, "//span[text()='=']")
    RESULT_INPUT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url):
        """Открыть страницу по переданному URL."""
        self.driver.get(url)
        return self

    def set_delay(self, seconds):
        """Ввести задержку в поле #delay."""
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_seven(self):
        """Нажать кнопку 7."""
        self.wait.until(EC.element_to_be_clickable(self.SEVEN_INPUT)).click()
        return self

    def click_plus(self):
        """Нажать кнопку +."""
        self.wait.until(EC.element_to_be_clickable(self.PLUS_INPUT)).click()
        return self

    def click_eight(self):
        """Нажать кнопку 8."""
        self.wait.until(EC.element_to_be_clickable(self.EIGHT_INPUT)).click()
        return self

    def click_equal(self):
        """Нажать кнопку =."""
        self.wait.until(EC.element_to_be_clickable(self.EQUAL_INPUT)).click()
        return self

    def wait_for_result(self, expected_value, timeout):
        """Дождаться появления ожидаемого значения на экране калькулятора."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element
            (self.RESULT_INPUT, expected_value))
        return self

    def get_result(self):
        """Вернуть текущий текст с экрана калькулятора."""
        return self.wait.until(
            EC.presence_of_element_located(self.RESULT_INPUT)).text
