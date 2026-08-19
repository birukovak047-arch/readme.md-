from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    name_p = driver.find_element(By.NAME, "custname")
    name_p.send_keys("Katya")
    driver.find_element(By.XPATH,
                        "//button[text() = 'Submit order']").click()

    # Сохраняем текущий URL после клика
    current_url = driver.current_url
    print(f"Текущий URL после отправки: {current_url}")
    assert (driver.current_url !=
            "https://httpbin.qa-territory.online/forms/post")

    driver.quit()
