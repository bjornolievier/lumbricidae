from lumbricidae.game import Game, MAX_PLAYERS
import pytest

@pytest.fixture
def game():
    return Game()

def test_game_initial_state(game) -> None:
    assert game.number_of_players == 0

def test_can_add_players(game) -> None:
    game.add_player_by_name("P1")
    game.add_player_by_name("P2")

    assert game.number_of_players == 2
    assert game.players == ["Player P1", "Player P2"]

def test_cannot_add_more_than_max_players(game) -> None:
    with pytest.raises(ValueError):
        for i in range(1, MAX_PLAYERS + 2):
            game.add_player_by_name(f"P{i}")

def test_game_cannot_start_with_less_than_2_players(game) -> None:
    assert not game.can_start()

    game.add_player_by_name("P1")
    assert not game.can_start()

    game.add_player_by_name("P2")
    assert game.can_start()
