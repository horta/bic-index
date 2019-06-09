def to_set(a):
    return [(set(c[0]), set(c[1])) for c in a]


def to_list(a):
    return [(list(c[0]), list(c[1])) for c in a]


def biclusters2pclusters(biclusters, nr):
    from numpy import asarray

    pclusters = []

    for bi in biclusters:

        rows = bi[0]
        cols = bi[1]

        pci = []
        for c in cols:

            pci += list(asarray(rows, int) + nr * c)

        pclusters.append(set(pci))

    return pclusters
