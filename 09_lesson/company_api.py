import requests


class CompanyApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_company_list(self, params_to_add=None):
        params = params_to_add or {}
        resp = requests.get(f"{self.base_url}/company", params=params)
        resp.raise_for_status()
        return resp.json()
