import pytest

from lumbricidae.tile import starting_tiles

@pytest.mark.property
def test_starting_tiles_invariants():
    """Property: Starting tiles should always have consistent properties"""
    tiles = starting_tiles
    
    assert len(tiles) == 16  # Known game constant
    assert all(tile.is_open for tile in tiles)
    assert all(21 <= tile.value <= 36 for tile in tiles)
    assert all(1 <= tile.worms <= 4 for tile in tiles)
    
    # Worm distribution should match game rules
    values_to_worms = {tile.value: tile.worms for tile in tiles}
    assert all(values_to_worms[v] == 1 for v in range(21, 25))
    assert all(values_to_worms[v] == 2 for v in range(25, 29))
    assert all(values_to_worms[v] == 3 for v in range(29, 33))
    assert all(values_to_worms[v] == 4 for v in range(33, 37))