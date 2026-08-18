import time

from selenium import webdriver

# Современный способ. Selenium Manager автоматически настроит драйвер
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

print(driver.title)
print(driver.current_url)

driver.refresh()

# Ждем 5 секунд (чтобы увидеть результат)
time.sleep(2)

# Закрываем браузер
driver.quit()