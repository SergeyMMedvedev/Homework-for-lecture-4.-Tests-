from ya_disk_api_service import Ya
from requests.exceptions import HTTPError


def test_create_folder(token, folder):
    ya = Ya(token, folder)
    response = ya.create_resource()
    assert response.status_code == 201

    try:
        ya.create_resource()
        assert False
    except HTTPError as e:
        assert e.response.status_code == 409
