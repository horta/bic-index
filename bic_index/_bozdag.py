from ._misc import biclusters2pclusters


def bozdag_uncovered(ba, bb, nr):
    from numpy import unique, intersect1d

    pba = biclusters2pclusters(ba, nr)
    pbb = biclusters2pclusters(bb, nr)

    uniona = unique([e for c in pba for e in c])
    unionb = unique([e for c in pbb for e in c])

    return len(intersect1d(uniona, unionb)) / len(unionb)


def bozdag_extra(ba, bb, nr):

    return bozdag_uncovered(bb, ba, nr)
