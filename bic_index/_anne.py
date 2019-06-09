from ._misc import to_list


def anne_rnia(biclustersa, biclustersb, n, p):
    from numpy import minimum, maximum

    biclustersa = to_list(biclustersa)
    biclustersb = to_list(biclustersb)

    Na = anne_num_cluster_belonging_to(biclustersa, n, p)
    Nb = anne_num_cluster_belonging_to(biclustersb, n, p)

    Is = minimum(Na, Nb).sum()
    Us = maximum(Na, Nb).sum()

    return 1 - ((Us - Is) / Us)


def anne_num_cluster_belonging_to(biclusters, n, p):
    from numpy import zeros

    N = zeros((n, p))

    for i in range(len(biclusters)):

        cols = biclusters[i][1]
        rows = biclusters[i][0]

        for j in range(len(cols)):

            N[rows, cols[j]] = N[rows, cols[j]] + 1

    return N


def anne_union_size(a, b, n, p):
    from numpy import maximum

    Na = anne_num_cluster_belonging_to(a, n, p)
    Nb = anne_num_cluster_belonging_to(b, n, p)

    return maximum(Na, Nb).sum()
