from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для главной страницы магазина (список товаров)."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name):
        """Добавить товар в корзину по его названию."""
        # Находим карточку товара по названию и кликаем кнопку внутри неё
        product_card = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                    f"//div[@class='inventory_item']"
                    f"[.//div[text()='{product_name}']]",)))
        add_button = product_card.find_element(
            By.XPATH, ".//button[contains(text(), 'Add to cart')]"
        )
        add_button.click()
        return self

    def go_to_cart(self):
        """Перейти в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
        return self
