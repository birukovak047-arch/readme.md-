"""
Page Object для главной страницы магазина (список товаров).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    """Page Object для главной страницы магазина (список товаров)."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """
        Конструктор класса InventoryPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара '{product_name}' в корзину")
    def add_to_cart(self, product_name):
        """
        Добавляет товар в корзину по его названию.

        :param product_name: str — точное название товара на странице.
        :return: None
        """
        product_card = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f"//div[@class='inventory_item']"
                 f"[.//div[text()='{product_name}']]")
            )
        )
        add_button = product_card.find_element(
            By.XPATH, ".//button[contains(text(), 'Add to cart')]")
        add_button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
