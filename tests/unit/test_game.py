import pytest

from lumbricidae.game import MAX_PLAYERS, Game
from lumbricidae.tile import starting_tiles


@pytest.fixture
def game():
    return Game()

@pytest.mark.unit
def test_game_initial_state(game) -> None:
    assert game.number_of_players == 0
    assert game.open_tiles == starting_tiles

@pytest.mark.unit
def test_can_add_players(game) -> None:
    game.add_player_by_name("P1")
    game.add_player_by_name("P2")

    assert game.number_of_players == 2
    assert game.players == ["Player P1", "Player P2"]

@pytest.mark.unit
def test_cannot_add_more_than_max_players(game) -> None:
    with pytest.raises(ValueError):
        for i in range(1, MAX_PLAYERS + 2):
            game.add_player_by_name(f"P{i}")

@pytest.mark.unit
def test_game_cannot_start_with_less_than_2_players(game) -> None:
    assert not game.can_start()

    game.add_player_by_name("P1")
    assert not game.can_start()

    game.add_player_by_name("P2")
    assert game.can_start()

@pytest.mark.unit
def test_cannot_add_player_with_empty_name(game) -> None:
    with pytest.raises(ValueError):
        game.add_player_by_name("")

@pytest.mark.unit
def test_cannot_add_player_after_game_starts(game) -> None:
    game.add_player_by_name("P1")
    game.add_player_by_name("P2")
    game.start()

    with pytest.raises(RuntimeError):
        game.add_player_by_name("P3")
