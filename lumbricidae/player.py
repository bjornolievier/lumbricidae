class Player:
    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"Player {self.name}"
    
    @property
    def name(self) -> str:
        return self._name