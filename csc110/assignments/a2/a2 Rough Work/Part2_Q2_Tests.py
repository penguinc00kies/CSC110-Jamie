"""Test Suite"""
from hypothesis import given
from hypothesis.strategies import integers, sets

import Part2_Q2


@given(x=integers(), y=integers(), z=sets(integers()))
def test_compare_arrangements_a(x: int, y: int, z: set[int]) -> None:
    """Test that mystery_2a_if and mystery_2a_no_if are identical in function"""
    assert Part2_Q2.mystery_2a_if(x, y, z) == Part2_Q2.mystery_2a_no_if(x, y, z)


@given(x=integers())
def test_compare_arrangements_b(x: int) -> None:
    """Test that mystery_2a_if and mystery_2a_no_if are identical in function"""
    assert Part2_Q2.mystery_2b_if(x) == Part2_Q2.mystery_2b_no_if(x)


@given(x=integers(), y=integers(), z=integers())
def test_compare_arrangements_c(x: int, y: int, z: int) -> None:
    """Test that mystery_2a_if and mystery_2a_no_if are identical in function"""
    assert Part2_Q2.mystery_2c_if(x, y, z) == Part2_Q2.mystery_2c_no_if(x, y, z)


if __name__ == '__main__':
    import pytest

    pytest.main(['Part2_Q2_Tests.py', '-v'])
