from dataclasses import dataclass


@dataclass(eq=True, slots=False, order=True)
class Tile:
    value: int
    worms: int
    is_open: bool

type TileStack = list[Tile]
type TileCollection = list[Tile]

def _generate_starting_tiles() -> TileCollection:
    collection = []
    for value in range(21, 37):
        worms = 0

        if value < 25:
            worms = 1
        elif value < 29:
            worms = 2
        elif value < 33:
            worms = 3
        elif value < 37:
            worms = 4
    
        collection.append(Tile(value, worms, True))
    
    return collection

starting_tiles: TileCollection = _generate_starting_tiles()