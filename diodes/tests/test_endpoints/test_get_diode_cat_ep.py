import pytest
import requests
from django.urls import reverse


class TestUserViewSet:
    path = "get_diode_cat-list"

    def test_get_diode_cat_empty_list(self, client):
        resp = client.get(self.path)

        response_data = resp.json()
        successful = response_data["successful"]
        data = response_data["data"]

        assert resp.status_code == 200
        assert successful is True
        assert isinstance(data, list)
        assert len(data) == 0

