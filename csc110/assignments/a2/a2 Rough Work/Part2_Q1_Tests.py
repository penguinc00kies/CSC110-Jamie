"""Test Suite"""
from hypothesis import given
from hypothesis.strategies import integers, sets, lists

import Part2_Q1


@given(x=integers(), nums=sets(integers()))
def test_compare_arrangements_a(x: int, nums: set[int]) -> None:
    """Test that mystery_1a_nested and mystery_1a_nested_rearranged are identical in function"""
    assert Part2_Q1.mystery_1a_nested(x, nums) == Part2_Q1.mystery_1a_nested_rearranged2(x, nums)


@given(x=integers(), nums=lists(lists(integers())))
def test_compare_arrangements_b(x: int, nums: list[list[int]]) -> None:
    """Test that mystery_1b_nested and mystery_1b_nested_rearranged are identical in function"""
    assert Part2_Q1.mystery_1b_nested(x, nums) == Part2_Q1.mystery_1b_nested_rearranged2(x, nums)


if __name__ == '__main__':
    import pytest
    pytest.main(['Part2_Q1_Tests.py', '-v'])
