"""
Page Object для страницы корзины.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """Page Object для страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self):
        """
        Возвращает количество товаров в корзине.

        :return: int — количество товаров в корзине.
        """
        items = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS))
        return len(items)

    @allure.step("Нажатие кнопки 'Checkout'")
    def click_checkout(self):
        """
        Нажимает кнопку Checkout.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
