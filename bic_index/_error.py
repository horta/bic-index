from ._anne import anne_union_size
from ._misc import biclusters2pclusters, to_list, to_set


def biclustering_error(biclustersa, biclustersb, n, p):
    from numpy import zeros, concatenate, asarray
    from munkres import make_cost_matrix

    biclustersa = to_list(biclustersa)
    biclustersb = to_list(biclustersb)

    ka = len(biclustersa)
    kb = len(biclustersb)

    pa = biclusters2pclusters(biclustersa, n)
    pb = biclusters2pclusters(biclustersb, n)

    biclustersa = to_set(biclustersa)
    biclustersb = to_set(biclustersb)

    M = zeros((ka, kb))
    for i in range(ka):
        for j in range(kb):

            M[i, j] = len(pa[i].intersection(pb[j]))

    if ka < kb:
        M = concatenate((M, zeros((kb - ka, kb))), axis=0)
    elif ka > kb:
        M = concatenate((M, zeros((ka, ka - kb))), axis=1)

    cost = make_cost_matrix(-M)

    dmax = asarray(cost).max()

    biclustersa = to_list(biclustersa)
    biclustersb = to_list(biclustersb)

    Us = anne_union_size(biclustersa, biclustersb, n, p)

    return 1 - ((Us - dmax) / Us)

