# import requests
#
# base_url = "http://139.100.217.192:8000"
#
#
# def test_simple_req():
#     resp = requests.get(base_url + '/company/list')
#
#     response_body = resp.json()
#     first_company = response_body[0]
#
#     assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
#     assert resp.status_code == 200
#     assert resp.headers["content-type"] == "application/json"
#
#
# def test_auth():
#     creds = {"username": "harrypotter", "password": "expelliarmus"}
#     resp = requests.post(base_url + "/auth/login", json=creds)
#
#     assert resp.json()["user_token"] is not None
#     assert resp.status_code == 200
#
#
# def test_create_company():
#     company = {"name": "python", "description": "requests"}
#     resp = requests.post(base_url + '/company/create', json=company)
#
#     assert resp.status_code == 201
#     company = {"name": "python", "description": "requests"}
#     resp = requests.post(base_url + "/company/create", json=company)
#     assert resp.status_code == 201
