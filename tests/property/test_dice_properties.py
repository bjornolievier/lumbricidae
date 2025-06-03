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