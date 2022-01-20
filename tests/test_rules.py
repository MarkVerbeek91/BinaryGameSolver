import pytest

import rules

N = None


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        ([0, 0, N, N, N, 1, 1, 0], [0, 0, 1, 1, 0, 1, 1, 0]),
    ],
)
def test_apply(in_data, out_data):
    assert rules.apply(in_data) == out_data


def test_apply_triple_rules_on_row():
    line = [0, 0, N, N, 1, 1]
    assert rules.apply_triple_rules_on_row(line) == [0, 0, 1, 0, 1, 1]


def test_apply_triple_rules():
    assert rules.apply_triple_rules(1, 1, None) == (1, 1, 0)


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        ([0, 0, None], (0, 0, 1)),
        ([1, 1, None], (1, 1, 0)),
    ],
)
def test_00x_results_in_001(in_data, out_data):
    assert rules.double_digit_right_rule(*in_data) == out_data


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        ([None, 1, 1], (0, 1, 1)),
        ([None, 0, 0], (1, 0, 0)),
    ],
)
def test_x00_results_in_100(in_data, out_data):
    assert rules.double_digit_left_rule(*in_data) == out_data


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        ([0, None, 0], (0, 1, 0)),
        ([1, None, 1], (1, 0, 1)),
    ],
)
def test_0x0_results_in_010(in_data, out_data):
    assert rules.triple_digit_rule(*in_data) == out_data


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        ([0, None], [0, 1]),
        ([None, None], [None, None]),
        ([0, None, 1, 0], [0, 1, 1, 0]),
        ([None, 1, 1, 0], [0, 1, 1, 0]),
        ([0, None, None, 0], [0, 1, 1, 0]),
    ],
)
def test_equal_numbers(in_data, out_data):
    assert rules.equal_numbers(in_data) == out_data
