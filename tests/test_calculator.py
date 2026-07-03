from src.calculator import add, percent_change


def test_add():
    assert add(2, 3) == 5


def test_percent_change():
    assert percent_change(100, 150) == 50
