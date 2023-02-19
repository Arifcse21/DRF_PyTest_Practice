import json
import pytest
import requests
from django.urls import reverse
from pathlib import Path


pytestmark = pytest.mark.django_db


class TestDiodeGetCategory:

    def test_get_diode_cat_empty_list(self, api_client):
        ep = reverse("get-diode-cat-list")
        resp = api_client().get(ep)

        response_data = resp.json()
        successful = response_data["successful"]
        data = response_data["data"]

        assert resp.status_code == 200
        assert successful is True
        assert isinstance(data, list)
        assert len(data) == 0

