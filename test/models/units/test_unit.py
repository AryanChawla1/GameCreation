import pytest

from ....models.units.unit import Unit

@pytest.fixture
def mock_unit():
    return Unit(
        "test",
        1,
        0.5,
        30,
        5,
        0.0,
        500,
        30,
        1
    )

def test_mock_unit_attack(mock_unit: Unit):
    assert mock_unit.attack() == mock_unit.attack_damage

def test_mock_unit_take_damage(mock_unit: Unit):
    mock_unit.lose_hp(20)
    assert mock_unit.hp == 481