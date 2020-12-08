from .day1 import get_two_entries_for_required_sum, read_puzzle_input, upd_get_n_entries_for_required_sum, get_n_entries_for_required_sum
import sys
import os
import pytest

TEST_INPUT_FILE_PATH = os.path.join(sys.path[1], "day1/test_sample.txt")


def test_get_two_entries_for_required_sum_2020():
    test_sample = read_puzzle_input(TEST_INPUT_FILE_PATH)

    first_number, second_number = get_two_entries_for_required_sum(test_sample, 2020)
    assert first_number + second_number == 2020

@pytest.mark.parametrize("n, required_sum", [(2, 2020), (3, 2020), (4, 2319)])
def test_upd_get_n_entries_for_required_sum(n, required_sum):
    test_sample = read_puzzle_input(TEST_INPUT_FILE_PATH)

    assert sum(upd_get_n_entries_for_required_sum(test_sample, required_sum, n)) == required_sum


@pytest.mark.parametrize("n, required_sum", [(2, 2020), (3, 2020), (4, 2319)])
def test_get_n_entries_for_required_sum(n, required_sum):
    test_sample = read_puzzle_input(TEST_INPUT_FILE_PATH)

    assert sum(get_n_entries_for_required_sum(test_sample, required_sum, n)) == required_sum
