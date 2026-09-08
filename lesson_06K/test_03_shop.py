from selenium import webdriver
from selenium.webdriver.common.by import By


def test_buy():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(
        By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Kate")
    driver.find_element(By.ID, "last-name").send_keys("Birukova")
    driver.find_element(By.ID, "postal-code").send_keys("566543")

    driver.find_element(By.ID, "continue").click()

    sum = driver.find_element(
        By.CSS_SELECTOR, "[data-test='total-label']").text

    driver.quit()

    assert sum == 'Total: $58.29'
