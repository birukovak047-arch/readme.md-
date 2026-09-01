import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get("https://gitflic.ru/")
   driver.add_cookie({
      "name": "SESSION",
      "value": "NzYyZmJiZjctZjRmZi00OTA4LThkNDYtMWY4ZmUyZTY0OGU0",
      "domain": "gitflic.ru"
   })
   driver.add_cookie({
       "name": "cookiesAccepted",
       "value": "true",
       "domain": "gitflic.ru"
   })
   driver.refresh()
   yield driver
   driver.quit()