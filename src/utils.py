from functools import reduce


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
    base[i : i + 3] = part
    return base


def is_solved(game):
    return not any([row.count(None) for row in game])


def print_game(game):
    print(
        "\n".join(
            ["".join(["N" if r is None else f"{r}" for r in row]) for row in game]
        )
    )
    print()
