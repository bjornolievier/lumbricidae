import random

from aenum import NamedConstant


class DieFace(NamedConstant):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    WORM = 5

    def __int__(self) -> int:
        return self.value

    @property
    def is_worm(self) -> bool:
        return self == DieFace.WORM 

type DiceCollection = dict[DieFace, int]

def roll_dice(n: int) -> list[DieFace]:
    return random.choices(list(DieFace), k=n)