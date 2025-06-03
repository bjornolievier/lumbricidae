from enum import Enum

from lumbricidae.player import Player
from lumbricidae.tile import TileCollection, starting_tiles
import lumbricidae.config as config

class GameState(Enum):
    SETUP = "setup"
    STARTED = "started"
    FINISHED = "finished"

class Game:
    def __init__(self) -> None:
        self._players: list[Player] = []
        self._tiles: TileCollection = starting_tiles
        self._state: GameState = GameState.SETUP

    def add_player_by_name(self, player_name: str) -> None:
        if not self._state == GameState.SETUP:
            raise RuntimeError("Cannot add players after the game has started")
        
        if self.number_of_players == config.MAX_PLAYERS:
            raise ValueError("Cannot add more than {MAX_PLAYERS} players")
        
        self._players.append(Player(player_name))

    @property
    def number_of_players(self) -> int:
        return len(self._players)
    
    @property
    def players(self) -> list[str]:
        return [str(player) for player in self._players]
    
    @property
    def open_tiles(self) -> TileCollection:
        return [tile for tile in self._tiles if tile.is_open]
    
    def start(self) -> None:
        if not self.can_start():
            raise RuntimeError("Game cannot start with less than {MIN_PLAYERS} players")
        
        self._state = GameState.STARTED

        # TODO Game logic would go here
        pass
    
    def can_start(self) -> bool:
        return config.MIN_PLAYERS <= self.number_of_players <= config.MAX_PLAYERS
    