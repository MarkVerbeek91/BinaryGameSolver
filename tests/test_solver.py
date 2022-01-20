import pytest

from solver import solver

N = None  # one letter None


@pytest.mark.parametrize(
    "invalid_game",
    [
        ([[0]]),
        ([[0, 1]]),
        ([[0, 1, 0]]),
        ([[0], [0], [0]]),
    ],
)
def test_invalid_games(invalid_game):
    with pytest.raises(TypeError):
        solver(invalid_game)


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        ([[None, 1], [0, 1]], [[0, 1], [0, 1]]),
        ([[0, None], [0, 1]], [[0, 1], [0, 1]]),
    ],
)
def test_0_results_in_0(test_input, expected_result):
    assert solver(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        ([[0, N, N, 1], [1, 0, 1, 0]], [[0, 1, 0, 1], [1, 0, 1, 0]]),
    ],
)
def test_also_run_on_columns(test_input, expected_result):
    assert solver(test_input) == expected_result


def test_need_second_iteration():
    game = [[0, N, N, 1], [N, N, 1, N]]

    assert solver(game) == [[0, 1, 0, 1], [1, 0, 1, 0]]
