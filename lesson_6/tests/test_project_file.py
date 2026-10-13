from pages.profile_page import ProfilePage
from pages.project_page import ProjectPage


def test_project_page(driver):
    profile_page = ProfilePage(driver, "https://gitflic.ru/user/airsworld")
    project_page.open_project_page()

    assert profile_page.get_project_title.page() == "Проекты"