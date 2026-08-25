from selenium import webdriver
from selenium.webdriver.common.by import By


def test_image_loading():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    image1 = driver.find_element(By.ID, "compass")
    image2 = driver.find_element(By.ID, "calendar")
    image3 = driver.find_element(By.ID, "award")
    image4 = driver.find_element(By.ID, "landscape")

    images = [image1, image2, image3, image4]

    expected_files = [
        "compass.png",
        "calendar.png",
        "award.png",
        "landscape.png"
    ]

    for i, img in enumerate(images):
        src = img.get_attribute("src")
        assert expected_files[i] in src
        assert img.is_displayed()

    driver.quit()