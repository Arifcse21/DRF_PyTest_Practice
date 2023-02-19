import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


class TestDiodeCreateCategory:
    def test_create_diode_cat(self, api_client):
        ep = reverse('create-diode-cat-list')
        payload = {
            "category": "LED",
            "description": "Light Emitting Diode"
        }
        resp = api_client().post(ep, payload)

        response = resp.json()
        successful = response["successful"]
        print("response = ", response)
        data = response["data"]

        assert resp.status_code == 201
        assert successful is True
        assert isinstance(data, dict)
        assert len(response) == 3
        assert len(data) == 5

    # @pytest.mark.xfail
    def test_create_diode_cat_invalid(self, api_client):
        ep = reverse('create-diode-cat-list')
        payload = {
            "category": "",
            "description": "Light Emitting Diode"
        }
        resp = api_client().post(ep, payload)

        response = resp.json()
        successful = response["successful"]
        print(response["message"])
        assert resp.status_code == 400
        assert successful is False



