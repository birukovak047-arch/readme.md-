import pytest
from selenium import webdriver
from pages.page_calc import Сalculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def calculator_url():
    return (
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_slow_calculator_addition(driver, calculator_url):
    page = Сalculator(driver)
    page.open(calculator_url)
    page.set_delay(45)
    page.click_seven()
    page.click_plus()
    page.click_eight()
    page.click_equal()
    page.wait_for_result("15", timeout=50)

    assert page.get_result() == "15", (
        f"Ожидался результат 15, получен {page.get_result()}"
    )
