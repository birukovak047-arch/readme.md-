"""
Тесты для оформления заказа в SauceDemo с отчётом Allure.
"""
import allure
import pytest
from selenium import webdriver
from LoginPageAllure import LoginPage
from InventoryPageAllure import InventoryPage
from CartPageAllure import CartPage
from CheckoutPageAllure import CheckoutPage

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCTS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"]


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    :return: WebDriver — объект драйвера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы при оформлении заказа")
@allure.description(
    "Тест авторизуется на saucedemo.com, добавляет 3 товара в корзину, "
    "переходит к оформлению заказа и проверяет, что итоговая сумма "
    "равна $58.29.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_checkout_total(driver):
    """
    Проверка итоговой суммы при оформлении заказа.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    login_page = LoginPage(driver)

    with allure.step(f"Открытие страницы {URL}"):
        login_page.open(URL)

    with allure.step("Авторизация под standard_user"):
        login_page.login(USERNAME, PASSWORD)

    inventory_page = InventoryPage(driver)

    with allure.step("Добавление товаров в корзину"):
        for product in PRODUCTS_TO_ADD:
            allure.attach(product, name="Добавленный товар",
                          attachment_type=allure.attachment_type.TEXT)
            inventory_page.add_to_cart(product)

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    cart_page = CartPage(driver)

    with allure.step("Нажатие кнопки Checkout"):
        cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнение формы покупателя"):
        checkout_page.fill_form("Иван", "Иванов", "123456")

    with allure.step("Нажатие кнопки Continue"):
        checkout_page.click_continue()

    with allure.step("Проверка итоговой суммы: ожидается $58.29"):
        total = checkout_page.get_total()
        assert total == "58.29", f"Ожидалось $58.29, получено ${total}"
