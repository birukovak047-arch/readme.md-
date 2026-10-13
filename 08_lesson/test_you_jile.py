from CompanyApi import CompanyApi

# Инициализация API-клиента
api = CompanyApi("https://ru.yougile.com/api-v2")

# --- Тесты для POST /api-v2/projects (Создание) ---


def test_create_project_positive():
    """Позитивный тест: создание проекта с корректным именем"""
    project_name = "Test Project"
    resp = api.create_project(project_name)

    assert resp.status_code == 201, (
        f"Ожидался статус 201, получен {resp.status_code}")
    response_body = resp.json()
    assert "id" in response_body, (
        "В ответе отсутствует ID созданного проекта")


def test_create_project_negative():
    """Негативный тест: создание проекта с пустым именем"""
    resp = api.create_project("")

    # Ожидаем ошибку 400 (Bad Request) или 422 (Unprocessable Entity)
    assert resp.status_code in [400, 422], (
        f"Ожидалась ошибка валидации, получен статус {resp.status_code}"
    )


# --- Тесты для PUT /api-v2/projects/{id} (Обновление) ---


def test_update_project_positive():
    """Позитивный тест: обновление имени существующего проекта"""
    # Создаем проект для обновления
    create_resp = api.create_project("Project to Update")
    project_id = create_resp.json().get("id")

    new_name = "Updated Project Name"
    resp = api.update_project(project_id, new_name)

    print("Status:", resp.status_code, "Body:", resp.text)  # ← отладка
    assert resp.status_code == 200, (
        f"Ожидался 200, получен {resp.status_code}. Ответ: {resp.text}"
    )


def test_update_project_negative():
    """Негативный тест: обновление несуществующего проекта"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    resp = api.update_project(non_existent_id, "New Name")

    # Ожидаем ошибку 404 (Not Found)
    assert resp.status_code == 404, \
        f"Ожидался статус 404, получен {resp.status_code}"


# --- Тесты для GET /api-v2/projects/{id} (Получение) ---


def test_get_project_positive():
    """Позитивный тест: получение информации о существующем проекте"""
    create_resp = api.create_project("Project to Get")
    project_id = create_resp.json().get("id")
    resp = api.get_project(project_id)
    assert resp.status_code == 200, (
        f"Ожидался статус 200, получен {resp.status_code}")
    project_data = resp.json()
    assert project_data.get("id") == project_id, "ID проекта не совпадает"


def test_get_project_negative():
    """Негативный тест: получение информации о несуществующем проекте"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project(non_existent_id)
    # Ожидаем ошибку 404 (Not Found)
    assert resp.status_code == 404, (
        f"Ожидался статус 404, получен {resp.status_code}")
