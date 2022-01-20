import utils


def apply(row):
    new_row = equal_numbers(row)
    new_row = apply_triple_rules_on_row(new_row)

    return new_row if row == new_row else apply(new_row)


def apply_triple_rules_on_row(row):
    if len(row) < 3:
        return row

    parts = [apply_triple_rules(*part) for part in utils.line_iter(row)]
    return utils.condenser(parts)


def apply_triple_rules(x, y, z):
    return double_digit_left_rule(*double_digit_right_rule(*triple_digit_rule(x, y, z)))


def double_digit_right_rule(x, y, z):
    return x, y, replace(x, y, z)


def double_digit_left_rule(x, y, z):
    return replace(y, z, x), y, z


def triple_digit_rule(x, y, z):
    return x, replace(x, z, y), z


def replace(a, b, c):
    return 1 if match(a, b, 0) else 0 if match(a, b, 1) else c


def match(x, y, target):
    return (x, y) == (target, target)


def equal_numbers(lst):
    nr_empty = utils.find_empty(lst)
    nr_zeros = utils.find_zeros(lst)
    nr_ones = utils.find_ones(lst)

    marker = 1 if nr_zeros == nr_empty + nr_ones else None
    marker = 0 if nr_ones == nr_empty + nr_zeros else marker

    return [marker if x is None else x for x in lst]
