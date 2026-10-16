from company_api import CompanyApi
from company_table import CompanyTable


api = CompanyApi("http://139.100.217.192:8000")
db = CompanyTable("postgresql://qa:skyqa@139.100.217.192:5432/x_clients")


def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()

    api_ids = {c["id"] for c in api_result}
    db_ids = {row["id"] for row in db_result}

    assert api_ids == db_ids, (
        f"Только в API: {api_ids - db_ids}\n"
        f"Только в БД: {db_ids - api_ids}"
    )


def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()

    api_ids = {c["id"] for c in filtered_list}
    db_ids = {row["id"] for row in db_list}

    assert api_ids == db_ids, (
        f"Только в API: {api_ids - db_ids}\n"
        f"Только в БД: {db_ids - api_ids}"
    )
