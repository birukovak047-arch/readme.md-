from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items_count(self):
        """Вернуть количество товаров в корзине."""
        items = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
        return len(items)

    def click_checkout(self):
        """Нажать кнопку Checkout."""
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self
