import pytest
from hypothesis import given
from hypothesis import strategies as st

from lumbricidae.dice import DieFace, roll_dice


@pytest.mark.property
@given(st.integers(min_value=1, max_value=8))
def test_roll_dice_returns_valid_faces(n):
    """Property: All rolled dice should be valid faces"""
    result = roll_dice(n)
    assert len(result) == n
    assert all(isinstance(face, DieFace) for face in result)
    assert all(1 <= face <= 5 for face in result)

@pytest.mark.property
@given(st.integers(min_value=1, max_value=8))
def test_dice_roll_sum_bounds(n):
    """Property: Sum of n dice should be between n and 5*n"""
    result = roll_dice(n)
    total = sum(int(face) for face in result)
    assert n <= total <= 5 * n

@pytest.mark.property
@given(st.lists(st.sampled_from(list(DieFace)), min_size=1, max_size=8))
def test_dice_collection_properties(dice_list):
    """Property: Any collection of dice should have valid totals"""
    total = sum(int(face) for face in dice_list)
    worm_count = sum(1 for face in dice_list if face.is_worm)
    
    assert total >= len(dice_list)  # Minimum: all 1s
    assert total <= 5 * len(dice_list)  # Maximum: all 5s/worms
    assert 0 <= worm_count <= len(dice_list)