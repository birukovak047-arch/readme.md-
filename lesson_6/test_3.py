from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    # Найдите радио-кнопку "Yes" и проверьте:
    but_r = driver.find_element(By.ID, "yesRadio")
    # 1. Что она отображается
    assert but_r.is_displayed() == True
    # 2. Что она доступна для клика
    assert but_r.is_enabled() == True

    driver.quit()
