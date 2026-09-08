from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    button_start = driver.find_element(
        By.XPATH, "//button[text()='Start']")
    button_start.click()
    # 3. Дождитесь появления текста "Hello World!"
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element(
        (By.ID, "finish"), "Hello World!"))
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshot/full_screen.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    hello_text = driver.find_element(By.ID, "finish").text
    assert hello_text == "Hello World!"

    driver.quit()
