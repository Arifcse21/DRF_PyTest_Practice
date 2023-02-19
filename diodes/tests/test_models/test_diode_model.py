import pytest
from diodes.models import Diode


@pytest.mark.django_db
def test_diode_model_empty():
    count = Diode.objects.count()

    assert count == 0
