from player import Player

MIN_PLAYERS = 2
MAX_PLAYERS = 7

class Game:
    def __init__(self) -> None:
        self._players: list[Player] = []

    def add_player_by_name(self, player_name: str) -> None:
        if self.number_of_players == MAX_PLAYERS:
            raise ValueError("Cannot add more players")
        
        self._players.append(Player(player_name))
    
    @property
    def number_of_players(self) -> int:
        return len(self._players)
    
    @property
    def players(self) -> list[str]:
        return [str(player) for player in self._players]
    
    def can_start(self) -> bool:
        return MIN_PLAYERS <= self.number_of_players <= MAX_PLAYERS