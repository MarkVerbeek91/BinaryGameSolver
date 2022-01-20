import rules
import utils

DEBUG = True


def debug_print(func):
    def wrapper(game):
        utils.print_game(game) if DEBUG else None
        func(game)

    return wrapper


def solver(game):
    if len(game) % 2 or len(game[0]) % 2:
        raise TypeError("Format not correct")

    game = solve(game)

    return game


@debug_print
def solve(game):
    if utils.is_solved(game):
        return game

    changed_game = [rules.apply(row) for row in game]

    return solve_transpose(changed_game) if changed_game != game else game


def solve_transpose(game):
    if utils.is_solved(game):
        return game

    game = utils.transpose(game)
    game = [rules.apply(row) for row in game]
    game = utils.transpose(game)

    return solve(game)
