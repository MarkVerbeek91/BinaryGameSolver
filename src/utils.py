from functools import reduce
from copy import deepcopy


def find_zeros(lst):
    return counter(lst, 0)


def find_ones(lst):
    return counter(lst, 1)


def find_empty(lst):
    return counter(lst, None)


def counter(lst, target):
    return lst.count(target)


def transpose(game):
    return [list(column) for column in zip(*game)]


def line_iter(line):
    for i in range(len(line) - 2):
        yield line[i], line[i + 1], line[i + 2]


def condenser(parts):
    n = len(parts) + 2
    rows = [extend(part, i, n) for i, part in enumerate(parts)]

    def func(x, y):
        return x if y is None else y

    row = [reduce(func, x) for x in zip(*rows)]

    return row


def extend(part, i, n):
    base = [None] * n
    base[i: i + 3] = part
    return base


def is_solved(game):
    return not any([row.count(None) for row in game])


def print_game(game):
    print(
        "\n".join(
            [" ".join([" " if r is None else f"{r}" for r in row]) for row in game]
        )
    )
    print("-" * 6)


def mutate(game):
    for i, row in enumerate(game):
        for j, num in enumerate(row):
            if num is not None:
                continue
            coordinate = (i, j)
            yield get_mutated_game(deepcopy(game), coordinate, 0)
            yield get_mutated_game(deepcopy(game), coordinate, 1)


def get_mutated_game(game, coordinate, digit):
    game[coordinate[0]][coordinate[1]] = digit
    return game


def to_short_notation(game):
    return "\n".join(
        [" ".join([" " if r is None else f"{r}" for r in row]) for row in game]
    )


def from_short_notation(string):
    # return [ [int(x) if ]]
    paas
