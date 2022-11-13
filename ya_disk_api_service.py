import requests
from requests import Response


class Ya:

    _BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str, folder_name: str) -> None:
        self.token = token
        self.folder = folder_name

    @property
    def folder(self) -> str:
        return self._folder

    @folder.setter
    def folder(self, folder_name: str) -> None:
        self._folder = folder_name + r'/'

    def _get_headers(self) -> dict:
        """Возвращает заголовки, наобходимые для отправки запросов к API Яндекс диска"""
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        return headers

    def create_resource(self) -> Response:
        """Создает папку на Яндекс диске."""
        url = self._BASE_URL
        params = {
            "path": self.folder,
        }
        response = requests.put(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response

    def _delete_resourse(self) -> Response:
        """Удаляет папку на Яндекс диске."""
        url = self._BASE_URL
        params = {
            "path": self.folder,
        }
        response = requests.delete(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response
