"""
Test the functions in L05.py
"""
# import L05 as lecture5
# from L05 import check_lengths
import L05


def test_check_lengths_one_string_equal() -> None:
    """Test whether check_lengths is correct a list with one item whose length is equal to max_length
    """
    expected = False
    actual = L05.check_lengths(['aaa'], 3)

    assert actual == expected

def test_check_lengths_one_string_less_than() -> None:
    """TTest whether check_lengths is correct a list with one item whose length is less than to max_length
    """
    expected = False
    actual = L05.check_lengths(['aaa'], 2)

    assert actual == expected


def test_check_lengths_one_string_greater_than() -> None:
    """TTest whether check_lengths is correct a list with one item whose length is greater than to max_length
    """
    expected = True
    actual = L05.check_lengths(['aaa'], 4)

    assert actual == expected

#if name
    #import pytest
    #pytest
