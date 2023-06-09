import pytest

from  ...models.castle import Castle

@pytest.fixture
def mock_castle():
    return Castle()

def test_default_castle_health(mock_castle: Castle):
    assert mock_castle.hp == 500

def test_default_castle_level_up(mock_castle: Castle):
    mock_castle.level_up()
    assert mock_castle.level == 2
    assert mock_castle.hp == 1000

def test_default_castle_lose_hp(mock_castle: Castle):
    mock_castle.lose_hp(50)
    assert mock_castle.hp == 450

def test_default_castle_dead(mock_castle: Castle):
    mock_castle.lose_hp(600)
    assert mock_castle.hp == 0

def test_castle_level_two_creation():
    mock_castle = Castle(2)
    assert mock_castle.hp == 1000
    assert mock_castle.level == 2