from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_window():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(driver, 10)
    # Ваш код здесь
    modal_w = wait.until(EC.presense_of_element_located(
        (By.CSS_SELECTOR, "div[class="modal"]))
    # assert modal_w.text == "This is a modal window"

    close = EC.driver.find_element(By.X.Path, "//p[text() = 'Close']")
    close.click()
    assert close = driver.invisibility_of_element_located()


    driver.quit()