import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        pass


@pytest.fixture
def client():
    return APIClient


