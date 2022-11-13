import pytest
from dotenv import load_dotenv
from ya_disk_api_service import Ya
from requests.exceptions import HTTPError
import os
import yaml


def get_token():
    load_dotenv()
    return os.getenv('YA_TOKEN')


def get_folder_name():
    with open('config.yml', 'r') as f:
        ycfg = yaml.safe_load(f)
    return ycfg.get('FOLDER_NAME')


def remove_testing_folder():
    ya_token = get_token()
    folder = get_folder_name()
    yandex = Ya(ya_token, folder)
    try:
        yandex._delete_resourse()
        print(
            f'Folder with name {folder} deleted after tests.')
    except HTTPError:
        print(
            f'Folder with name {folder} does not exist. Do not need to delete this.')


def pytest_unconfigure():
    remove_testing_folder()


@pytest.fixture()
def token():
    yield get_token()


@pytest.fixture()
def folder():
    yield get_folder_name()
