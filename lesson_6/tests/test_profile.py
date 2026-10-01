import faker
import config
from pages.profile_page import ProfilePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


fake = faker.Faker()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f"{first_name} {last_name}"


def test_change_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    profile.update_profile(first_name, last_name)
    profile.open_profile_page("airsworld")

    assert profile.get_user_name() == first_name,  "Имя профиля не было обновлено"

def test_check_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    name = profile.get_user_name()

    assert name != "", "Имя не должно быть пустым"
    assert len(name) > 0, "Имя содержит хотя бы один символ"
