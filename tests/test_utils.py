import utils
from utils import (condenser, extend, find_empty, find_ones, find_zeros,
                   line_iter)


def test_find_zeros():
    assert find_zeros([0]) == 1
    assert find_zeros([1]) == 0
    assert find_zeros([0, 0]) == 2
    assert find_zeros([0, 1]) == 1


def test_find_ones():
    assert find_ones([1]) == 1
    assert find_ones([0]) == 0
    assert find_ones([1, 0]) == 1
    assert find_ones([1, 1]) == 2


def test_find_empty():
    assert find_empty([None]) == 1
    assert find_empty([0]) == 0
    assert find_empty([None, 0]) == 1
    assert find_empty([None, None]) == 2


def test_transpose():
    game = [[0]]
    assert utils.transpose(game) == [[0]]

    game = [[0, 0], [1, 1]]
    assert utils.transpose(game) == [[0, 1], [0, 1]]

    game = [[0, 0, 1, 1], [1, 1, 0, 0]]
    assert utils.transpose(game) == [[0, 1], [0, 1], [1, 0], [1, 0]]


def test_line_iter():
    line = [0, 0, 1, 1]

    iter_inst = iter(line_iter(line))
    assert next(iter_inst) == (0, 0, 1)
    assert next(iter_inst) == (0, 1, 1)


def test_condenser():
    line_parts = [(0, 1, 1), (1, 1, 0)]
    assert condenser(line_parts) == [0, 1, 1, 0]

    line_parts = [(1, 0, 1), (0, 1, 1), (1, 1, 0)]
    assert condenser(line_parts) == [1, 0, 1, 1, 0]


def test_extend():
    assert extend((1, 1, 0), 1, 5) == [None, 1, 1, 0, None]


def test_game_unsolved():
    assert utils.is_solved([[0]])
    assert not utils.is_solved([[1, 0], [0, None]])


def test_mutate_game():
    game = [[None, 1], [None, None]]

    game_mutate = utils.mutate(game)

    assert next(game_mutate) == [[0, 1], [None, None]]
    assert next(game_mutate) == [[1, 1], [None, None]]
    assert next(game_mutate) == [[None, 1], [0, None]]



