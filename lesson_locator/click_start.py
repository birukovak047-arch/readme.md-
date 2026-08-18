from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://gitflic.ru")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "cookiesBtn").click()
sleep(1)

click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(1)

input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")
input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")
sleep(1)

# input_login.clear()
# input_password.clear()
# sleep(1)

# Нажимаем кнопку входа
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

# Получаем имя пользователя
user_name = driver.find_element(By.CLASS_NAME, "profile-page__profile-name")
print(user_name.text)

# Находим поле поиска
search_input = driver.find_element(By.CSS_SELECTOR, "input.gf-custom-search__input")

# Получаем существующий атрибут placeholder
print(search_input.get_attribute("placeholder"))  # Что будем искать?

# Пробуем получить несуществующий атрибут
print(search_input.get_attribute("plac"))  # Вернет None

sleep(2)

driver.quit()