import json
import pytest
import requests
from django.urls import reverse
from pathlib import Path


pytestmark = pytest.mark.django_db


class TestDiodeCategory:

    def test_get_diode_cat_empty_list(self, api_client):
        ep = "/api/v1/diodes/get-diode-cat/"
        resp = api_client().get(ep)

        response_data = resp.json()
        successful = response_data["successful"]
        data = response_data["data"]

        assert resp.status_code == 200
        assert successful is True
        assert isinstance(data, list)
        assert len(data) == 0

