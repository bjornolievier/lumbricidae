from lumbricidae.player import Player

def test_player_str() -> None:
    player = Player("P1")

    assert "Player P1" == str(player)