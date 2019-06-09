from ._misc import to_set


def lew(ba, bb):
    from numpy import zeros

    ba = to_set(ba)
    bb = to_set(bb)

    k = len(ba)
    q = len(bb)

    S = zeros((k, q))

    for i in range(k):

        for j in range(q):

            rrint = ba[i][0].intersection(bb[j][0])
            ccint = ba[i][1].intersection(bb[j][1])

            rruni = ba[i][0].union(bb[j][0])
            ccuni = ba[i][1].union(bb[j][1])

            S[i, j] = (len(rrint) + len(ccint)) / (len(rruni) + len(ccuni))

    return S.max() / k
