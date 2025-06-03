import pytest

from lumbricidae.player import Player


@pytest.mark.unit
def test_player_str() -> None:
    player = Player("P1")

    assert str(player) == "Player P1"

@pytest.mark.unit
def test_player_initial_state() -> None:
    player = Player("P1")
    
    assert player.dice == {}
    assert player.tiles == []

@pytest.mark.unit
def test_player_must_have_name() -> None:
    with pytest.raises(ValueError):
        Player("")