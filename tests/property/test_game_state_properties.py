import pytest
from hypothesis import given
from hypothesis import strategies as st
import lumbricidae.config as config
from lumbricidae.game import Game
from lumbricidae.player import Player   

@pytest.mark.property
@given(st.integers(min_value=0, max_value=10))
def test_game_player_invariants(num_players):
    """Property: Game state should be consistent regardless of player count"""
    game = Game()
    
    # Try to add players
    added_players = 0
    for i in range(num_players):
        try:
            game.add_player_by_name(f"Player{i}")
            added_players += 1
        except ValueError:
            break  # Hit max players
    
    assert game.number_of_players == added_players
    assert game.number_of_players <= config.MAX_PLAYERS
    assert (game.can_start()) == (config.MIN_PLAYERS <= added_players <= config.MAX_PLAYERS)

@pytest.mark.property
@given(st.text(min_size=1, max_size=50))
def test_player_name_handling(name):
    """Property: Any non-empty string should be a valid player name"""
    try:
        player = Player(name.strip())
        assert player.name == name.strip()
        assert str(player) == f"Player {name.strip()}"
    except ValueError:
        # Should only fail for empty names after stripping
        assert not name.strip()