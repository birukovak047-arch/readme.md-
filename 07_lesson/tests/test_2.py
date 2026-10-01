import pytest
from selenium import webdriver
from pages.page_shop1 import LoginPage
from pages.page_shop2 import InventoryPage
from pages.page_shop3 import CartPage
from pages.page_shop4 import CheckoutPage

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCTS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"]


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total(driver):
    """Проверка итоговой суммы при оформлении заказа."""
    # 1. Авторизация
    login_page = LoginPage(driver)
    login_page.open(URL)
    login_page.login(USERNAME, PASSWORD)

    # 2. Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    for product in PRODUCTS_TO_ADD:
        inventory_page.add_to_cart(product)

    # 3. Переход в корзину и Checkout
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 4. Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Иванов", "123456")
    checkout_page.click_continue()

    # 5. Проверка итоговой суммы
    total = checkout_page.get_total()
    assert total == "58.29", f"Ожидалось $58.29, получено ${total}"
