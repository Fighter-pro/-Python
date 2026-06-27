import requests


class YandexDiskClient:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"OAuth {self.token}"
        }

    def create_folder(self, folder_name):
        response = requests.put(
            self.BASE_URL,
            headers=self.headers,
            params={"path": folder_name}
        )
        return response

    def get_folder_info(self, folder_name):
        response = requests.get(
            self.BASE_URL,
            headers=self.headers,
            params={"path": folder_name}
        )
        return response

    def delete_folder(self, folder_name):
        response = requests.delete(
            self.BASE_URL,
            headers=self.headers,
            params={"path": folder_name, "permanently": "true"}
        )
        return response