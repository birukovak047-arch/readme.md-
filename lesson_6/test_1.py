from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_1():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    # Нажимаем кнопку Remove и ждем сообщения
    but_rem = driver.find_element(By.XPATH, "//button[text()='Remove']")
    but_rem.click()
    # Ждем появления текста "It's gone!" и проверяем
    text = wait.until(
        EC.presence_of_element_located(By.XPATH, "//button[text()='Remove']"))
    text.click()