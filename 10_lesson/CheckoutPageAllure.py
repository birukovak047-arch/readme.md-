"""
Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполняет форму данными покупателя.

        :param first_name: str — имя покупателя.
        :param last_name: str — фамилия покупателя.
        :param postal_code: str — почтовый индекс.
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(last_name)
        self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE_INPUT)
        ).send_keys(postal_code)

    @allure.step("Нажатие кнопки 'Continue'")
    def click_continue(self):
        """
        Нажимает кнопку Continue.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self):
        """
        Читает итоговую стоимость со страницы.

        :return: str — сумма заказа без символа '$'.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL))
        return total_element.text.split("$")[1].strip()
