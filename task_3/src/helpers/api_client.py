from urllib.parse import urljoin
import requests
from requests.auth import HTTPBasicAuth


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, headers=None, params=None, **kwargs):
        url = urljoin(self.base_url, path)
        response = requests.get(url, headers=headers, params=params, **kwargs)
        if response.ok:
            data = response.json()
            return data
        else:
            raise Exception(f"{response.status_code}, {response.content}")

    def post(self, path, headers=None, json=None, **kwargs):
        url = urljoin(self.base_url, path)
        response = requests.post(url, headers=headers, json=json, **kwargs)
        return response

    def put(self, path, headers=None, json=None):
        url = urljoin(self.base_url, path)
        response = requests.put(url, headers=headers, json=json)
        return response

    def delete(self, path, headers=None):
        url = urljoin(self.base_url, path)
        response = requests.delete(url, headers=headers)
        return response

    def auth(self, username, password):
        auth = HTTPBasicAuth(username, password)
        return auth
