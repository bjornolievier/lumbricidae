import random

from aenum import NamedConstant


class DieFace(NamedConstant):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    WORM = 5

type DiceCollection = dict[DieFace, int]

def roll_dice(n: int) -> list[DieFace]:
    return random.choices(list(DieFace), k=n)