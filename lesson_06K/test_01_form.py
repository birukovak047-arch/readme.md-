from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    driver.implicitly_wait(10)

    form = ["first-name", "last-name", "address",
            "zip-code", "city", "country", "e-mail",
            "phone", "job-position", "company"]
    values = ["Иван","Петров", "Ленина, 55-3", "", "Москва", "Россия",
              "test@skypro.com", "+7985899998787", "QA", "SkyPro"]
    for x in range(0, len(form)):
        driver.find_element(By.NAME, form[x]).send_keys(values[x])

    # field_1 = driver.find_element(By.NAME, "first-name")
    # field_1.send_keys("Иван")
    # field_2 = driver.find_element(By.NAME, "last-name")
    # field_2.send_keys("Петров")
    # field_3 = driver.find_element(By.NAME, "address")
    # field_3.send_keys("Ленина, 55-3")
    # field_4 = driver.find_element(By.NAME, "zip-code")
    # field_4.send_keys("")
    # field_5 = driver.find_element(By.NAME, "city")
    # field_5.send_keys("Москва")
    # field_6 = driver.find_element(By.NAME, "country")
    # field_6.send_keys("Россия")
    # field_7 = driver.find_element(By.NAME, "e-mail")
    # field_7.send_keys("test@skypro.com")
    # field_8 = driver.find_element(By.NAME, "phone")
    # field_8.send_keys("+7985899998787")
    # field_9 = driver.find_element(By.NAME, "job-position")
    # field_9.send_keys("QA")
    # field_10 = driver.find_element(By.NAME, "company")
    # field_10.send_keys("SkyPro")

    driver.find_element(By.XPATH,
                        "//button[text() = 'Submit']").click()

    field_zip = driver.find_element(
        By.CSS_SELECTOR, ".alert-danger#zip-code")
    assert field_zip.is_displayed()

    field_all = driver.find_elements(
        By.CSS_SELECTOR, ".alert-success")
    assert len(field_all) == 9

    driver.quit()
