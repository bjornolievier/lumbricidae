from lumbricidae.dice import DiceCollection
from lumbricidae.tile import TileStack


class Player:
    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("Player must have a name")
        self._name:str = name
        
        self._dice:DiceCollection = {}
        self._tiles:TileStack = []

    def __str__(self) -> str:
        return f"Player {self.name}"
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def dice(self) -> DiceCollection:
        return self._dice
    
    @property
    def tiles(self) -> TileStack:
        return self._tiles
