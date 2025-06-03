import pytest

from lumbricidae.tile import Tile, starting_tiles


@pytest.mark.unit
def test_starting_tiles() -> None:
    assert starting_tiles == [Tile(value=21, worms=1, is_open=True), 
                            Tile(value=22, worms=1, is_open=True), 
                            Tile(value=23, worms=1, is_open=True), 
                            Tile(value=24, worms=1, is_open=True), 
                            Tile(value=25, worms=2, is_open=True), 
                            Tile(value=26, worms=2, is_open=True), 
                            Tile(value=27, worms=2, is_open=True), 
                            Tile(value=28, worms=2, is_open=True), 
                            Tile(value=29, worms=3, is_open=True), 
                            Tile(value=30, worms=3, is_open=True), 
                            Tile(value=31, worms=3, is_open=True), 
                            Tile(value=32, worms=3, is_open=True), 
                            Tile(value=33, worms=4, is_open=True), 
                            Tile(value=34, worms=4, is_open=True), 
                            Tile(value=35, worms=4, is_open=True), 
                            Tile(value=36, worms=4, is_open=True)]
