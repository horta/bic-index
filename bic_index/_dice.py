from ._misc import biclusters2pclusters


def calculate_dice(ba, bb, nr, nc):
    from numpy import zeros

    pclustersa = biclusters2pclusters(ba, nr)
    pclustersb = biclusters2pclusters(bb, nr)

    k = len(ba)
    q = len(bb)

    D = zeros((k, q))

    for i in range(k):

        for j in range(q):

            s = 2 * len(pclustersa[i].intersection(pclustersb[j]))
            D[i, j] = s / (len(pclustersa[i]) + len(pclustersb[j]))

    return D
