import os
import pytest

from ya_disk import YandexDiskClient


TOKEN = os.getenv("YANDEX_TOKEN")


@pytest.mark.skipif(TOKEN is None, reason="Не указан YANDEX_TOKEN")
def test_create_folder_success():
    client = YandexDiskClient(TOKEN)
    folder_name = "netology_test_folder"

    client.delete_folder(folder_name)

    create_response = client.create_folder(folder_name)
    assert create_response.status_code == 201

    info_response = client.get_folder_info(folder_name)
    assert info_response.status_code == 200

    folder_info = info_response.json()
    assert folder_info["name"] == folder_name

    client.delete_folder(folder_name)


@pytest.mark.parametrize(
    "token, expected_status_code",
    [
        ("wrong_token", 401),
        ("", 401),
    ]
)
def test_create_folder_with_wrong_token(token, expected_status_code):
    client = YandexDiskClient(token)

    response = client.create_folder("wrong_token_folder")

    assert response.status_code == expected_status_code


@pytest.mark.skipif(TOKEN is None, reason="Не указан YANDEX_TOKEN")
def test_create_existing_folder():
    client = YandexDiskClient(TOKEN)
    folder_name = "netology_existing_folder"

    client.delete_folder(folder_name)

    first_response = client.create_folder(folder_name)
    assert first_response.status_code == 201

    second_response = client.create_folder(folder_name)
    assert second_response.status_code == 409

    client.delete_folder(folder_name)