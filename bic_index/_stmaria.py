from ._dice import calculate_dice


def stmaria(ba, bb, nr, nc):
    return calculate_dice(ba, bb, nr, nc).sum() / len(ba)
