from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    all_links = driver.find_elements(By.TAG_NAME, "a")
    assert len(all_links) == 9

    for link in all_links():
        assert link.is_displayed()
        assert link[0] == "1"

    driver.quit()