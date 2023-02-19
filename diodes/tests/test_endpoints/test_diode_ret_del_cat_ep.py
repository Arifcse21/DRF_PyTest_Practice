import pytest
import requests
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestDiodeRetDelCategory:
    endpoint = reverse("ret-del-diode-cat-detail", kwargs={"pk": 1})

    def test_diode_retrieve_cat(self, api_client):

        resp = api_client().get(self.endpoint)
        print(resp.json())
        assert resp.status_code == 200
        
