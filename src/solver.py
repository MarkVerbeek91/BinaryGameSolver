import rules
import utils

DEBUG = True


def debug_print(func):
    def wrapper(game):
        game = func(game)
        utils.print_game(game) if DEBUG else None
        return game

    return wrapper


def solver(game):
    if len(game) % 2 or len(game[0]) % 2:
        raise TypeError("Format not correct")

    game = solve(game)

    if not utils.is_solved(game):
        game = solve_with_mutation(game)

    if not utils.is_solved(game):
        for mutated_game in utils.mutate(game):
            solved_game = solve_with_mutation(mutated_game)

            if utils.is_solved(solved_game):
                game = solved_game
                break

    return game


def solve_with_mutation(game):
    for mutated_game in utils.mutate(game):
        solved_game = solve(mutated_game)

        if utils.is_solved(solved_game):
            game = solved_game
            break

    return game


# @debug_print
def solve(game):
    if utils.is_solved(game):
        return game

    game = [rules.apply(row) for row in game]

    return solve_transpose(game)


def solve_transpose(game):
    if utils.is_solved(game):
        return game

    game_changed = utils.transpose(game)
    game_changed = [rules.apply(row) for row in game_changed]
    game_changed = utils.transpose(game_changed)

    return solve(game_changed) if game_changed != game else game


