import pytest
import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected_arr


def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == expected_arr


def test_bubble_sort_invalid():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, 3)
    assert result == []

def test_bubble_sort_too_many_numbers():
    # REQ-03: Test with >= 10 numbers
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1

def test_bubble_sort_zero_numbers():
    # REQ-04: Test with 0 numbers
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0

def test_bubble_sort_non_integer():
    # REQ-05: Test with non-integer values
    input_arr = [1, "a", 3.5]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2