from ._misc import biclusters2pclusters


def eren_relevance(ba, bb, nr, nc):
    from math import inf

    pclustersa = biclusters2pclusters(ba, nr)
    pclustersb = biclusters2pclusters(bb, nr)

    r = 0
    for i in range(len(pclustersa)):

        best = -inf
        for j in range(len(pclustersb)):

            int = len(pclustersa[i].intersection(pclustersb[j]))
            uni = len(pclustersa[i].union(pclustersb[j]))
            t = int / uni

            if t > best:
                best = t
        r = r + best

    return r / len(pclustersa)


def eren_recovery(ba, bb, nr, nc):

    return eren_relevance(bb, ba, nr, nc)
