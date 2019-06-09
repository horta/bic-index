from ._misc import to_set


def ayadi(ba, bb):
    from math import inf

    ba = to_set(ba)
    bb = to_set(bb)

    r = 0
    for i in range(len(ba)):

        maior = -inf
        for j in range(len(bb)):

            top = _is(ba[i][0], bb[j][0]) * _is(ba[i][1], bb[j][1])
            bottom = _us(ba[i][0], bb[j][0]) * _us(ba[i][1], bb[j][1])

            maior = max(maior, top / bottom)
        r = r + maior

    return r / len(ba)


def _us(a, b):
    return len(a.union(b))


def _is(a, b):
    return len(a.intersection(b))

