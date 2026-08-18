# 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_page_title():
#     driver = webdriver.Chrome()
#     driver.get("https://httpbin.qa-territory.online/")
#     main_button = driver.find_element(By.TAG_NAME, "h1")
#     assert "httpbin" in title.text.lower()
#     driver.quit()

# 2

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_form_interaction():
#     driver = webdriver.Chrome()
#     driver.get("https://httpbin.qa-territory.online/forms/post")
#     line_w = driver.find_element(By. //placeholder = [text()="Customer name"])
#     # Заполните поле "custname" значением "Иван Иванов"
#     name_field = driver.find_element(By.NAME, "custname")
#     name_field.send_keys("Иван Иванов")
#
#     # Найдите кнопку отправки и кликните на нее
#     submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
#     submit_btn.click()
#
#     driver.quit()
#
# 3

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    # Найдите радио-кнопку "Yes" и проверьте:
    # 1. Что она отображается
    button_visibility_hidden = driver.find_element(By.ID, "invisibleButton")

    if button_visibility_hidden.is_displayed():
        print("Кнопка видна")
    else:
        print("Кнопка скрыта")
    # 2. Что она доступна для клика

    driver.quit()