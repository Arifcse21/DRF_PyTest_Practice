import pytest


class Circuit:
    def __init__(self, name: str, ctype: str):
        self.name = name
        self.ctype = ctype

    def __str__(self):
        return f"{self.name}: {self.ctype}"


@pytest.fixture
def circuit() -> Circuit:
    return Circuit(name="led", ctype="diode")


def test_with_fixture(circuit: Circuit) -> None:
    print(f">Printing {circuit} from fixture")


@pytest.mark.parametrize(
    "circuit_type",
    ["Diode", "Zener Diode", "Forward biased"],
    # ids=[1, 2, 3]
)
def test_parametrize(circuit_type: str) -> None:
    print(f"\nTest with {circuit_type}")


def raise_not_circuit_exception() -> None:
    raise ValueError("Not Circuit Exception")


def test_raise_not_circuit_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_not_circuit_exception()
    assert "Not Circuit Exception" == str(e.value)

