import pytest


def test_first_test_func() -> None:
    assert 1 == 1


@pytest.mark.skip(reason="This test might fail")
def test_to_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="4 > 1 is true")
def test_to_be_skipped_if():
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_if_fails():
    assert 1 == 2


@pytest.mark.slow
def test_custom_marker():
    assert 1 == 1
