import requests
from CompanyApi import CompanyApi

base_url = "http://139.100.217.192:8000"

api = CompanyApi(base_url)


def test_simple_req():
    resp = requests.get(base_url + '/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0


# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list) > len(filtered_list)


# Проверка добавления новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr

def test_auth():
    token = get_token()
    assert token is not None


def test_get_companies():
    body = get_company_list()
    assert len(body) > 0


def test_get_active_companies():
    full_list = get_company_list()
    filtered_list = get_company_list(params_to_add={'active': 'true'})
    assert len(full_list) > len(filtered_list)


def test_add_new():
    # Получить количество компаний до
    body = get_company_list()
    len_before = len(body)

    # Создать новую компанию
    name = "Autotest"
    descr = "Descr"
    create_company(name, descr)

    # Получить количество компаний после
    body = get_company_list()
    len_after = len(body)

    # Проверить, что количество компаний увеличилось на 1
    assert len_after - len_before == 1
    # Проверить название и описание
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == "new_id"

def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "UPDATED"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr

def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус компании
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    # Получаем список компаний и сохраняем его длину
    body = api.get_company_list()
    len_before = len(body)

    # Удаляем компанию
    api.delete_company(new_id)

    # Проверяем, что список компаний стал меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before - len_after == 1

    # Проверяем, что удалённая компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'


def test_deactivate():
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    body = api.set_active_state(new_id, False)

    assert body["is_active"] is False


def test_deactivate_and_activate_back():
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    body_d = api.set_active_state(new_id, False)
    assert body_d["is_active"] is False

    body_a = api.set_active_state(new_id, True)
    assert body_a["is_active"] is True