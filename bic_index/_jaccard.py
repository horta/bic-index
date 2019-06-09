from ._misc import biclusters2pclusters


def calculate_jaccard(ba, bb, nr):
    from numpy import zeros

    pclustersa = biclusters2pclusters(ba, nr)
    pclustersb = biclusters2pclusters(bb, nr)

    k = len(ba)
    q = len(bb)

    J = zeros((k, q))

    for i in range(k):

        for j in range(q):

            ii = len(pclustersa[i].intersection(pclustersb[j]))
            ui = len(pclustersa[i].union(pclustersb[j]))

            J[i, j] = ii / ui

    return J
