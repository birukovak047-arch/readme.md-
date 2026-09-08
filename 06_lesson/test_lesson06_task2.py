from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    # Добавляем cookie первого пользователя
    driver.add_cookie({
        "name": "SESSION",
        "value": "YmY4YTM2NDgtMGQ4My00OTJhLTk4NTAtOWFlYjliODBjOTMz",
        "domain": "gitflic.ru"
    })
    # Добавляем cookie для окна подтверждения работы с cookie
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # Обновляем страницу, чтобы cookie применилась
    driver.refresh()
    driver.get(
        "https://gitflic.ru/project?sort=updated_at&direction=ASC")
    person_one = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "MWQzN2Y4MDAtNmNiZi00NzJhLTkyOGYtOGQwODExNDk2MTdk",
        "domain": "gitflic.ru"})
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"})
    driver.refresh()
    driver.get(
        "https://gitflic.ru/project?sort=updated_at&direction=ASC")
    person_two = driver.current_url
    assert person_one != person_two

    driver.quit()
