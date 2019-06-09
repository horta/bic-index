from math import inf, sqrt

from ._misc import to_set


def prelic_relevance(ba, bb):
    ba = to_set(ba)
    bb = to_set(bb)
    return sqrt(_prelic_dim(ba, bb, 0) * _prelic_dim(ba, bb, 1))


def prelic_recovery(ba, bb):
    return prelic_relevance(bb, ba)


def _prelic_dim(ba, bb, dim):

    r = 0
    for a in ba:

        rbest = -inf
        for b in bb:
            nom = len(a[dim].intersection(b[dim]))
            denom = len(a[dim].union(b[dim]))
            rbest = max(rbest, nom / denom)
        r = r + rbest

    return r / len(ba)
