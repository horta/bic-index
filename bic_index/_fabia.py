from ._jaccard import calculate_jaccard


def fabia(ba, bb, nr):
    from munkres import Munkres

    J = calculate_jaccard(ba, bb, nr)

    k = len(ba)
    q = len(bb)

    A = Munkres().compute(-1 * J)

    r = 0
    for i in range(min(k, q)):
        r = r + J[A[i][0], A[i][0]]

    return r / max(k, q)

