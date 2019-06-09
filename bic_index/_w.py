from ._dice import calculate_dice
from ._jaccard import calculate_jaccard
from ._misc import biclusters2pclusters


def wjac(ba, bb, nr):

    J = calculate_jaccard(ba, bb, nr)
    pclustersa = biclusters2pclusters(ba, nr)

    k = len(ba)

    up = 0
    down = 0

    for i in range(k):

        val = J[i, :].max()

        up = up + len(pclustersa[i]) * val

        down = down + len(pclustersa[i])

    return up / down


def wdic(ba, bb, nr, nc):

    D = calculate_dice(ba, bb, nr, nc)
    pclustersa = biclusters2pclusters(ba, nr)

    k = len(ba)

    up = 0
    down = 0

    for i in range(k):

        val = D[i, :].max()
        up = up + len(pclustersa[i]) * val

        down = down + len(pclustersa[i])

    return up / down
