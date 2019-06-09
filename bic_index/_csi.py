from ._misc import biclusters2pclusters


def csi(ba, bb, n, p):
    from numpy import zeros

    pa = biclusters2pclusters(ba, n)
    pa = sort_clusters(pa)

    pb = biclusters2pclusters(bb, n)
    pb = sort_clusters(pb)

    cc = collide_clusters(pa + pb)

    cpa = []
    cpb = []
    mult = zeros(len(cc))
    for i in range(len(cc)):

        obj = min(cc[i])
        mult[i] = len(cc[i])
        cpa = insert_obj(cpa, pa, i, obj)
        cpb = insert_obj(cpb, pb, i, obj)

    return _csi(cpa, cpb, mult, n * p)


def sort_clusters(clusters):

    for i in range(len(clusters)):
        clusters[i] = sorted(clusters[i])

    return clusters


def insert_obj(cpp, pp, index, obj):

    for i in range(len(pp)):
        if obj in pp[i]:
            while len(cpp) <= i:
                cpp.append([])
            cpp[i].append(index)

    return cpp


def collide_clusters(pp):

    qin = pp
    qout = []

    while len(qin) > 0:

        spot = qin[-1]
        qin = qin[:-1]

        qaux = []
        for i in range(len(qout)):

            res = intersect_sorted(spot, qout[i])
            if len(res) == 0:
                qaux.append(qout[i])
            else:
                qaux.append(res)
                spot = setdiff_sorted(spot, res)
                qoutres = setdiff_sorted(qout[i], res)
                if len(qoutres) > 0:
                    qaux.append(qoutres)
            if len(spot) == 0:
                break

        if len(spot) > 0:
            qaux.append(spot)
        qout = qaux

    return qout


def _csi(cpa, cpb, mult, ntotal):
    from numpy import triu, minimum

    n = len(mult)

    alphaU, betaU = alphabeta(cpa, n)
    alphaV, betaV = alphabeta(cpb, n)

    Ag = minimum(alphaU, alphaV)
    Dg = abs(alphaU - alphaV)

    minbeta = minimum(betaU, betaV)
    absbeta = abs(betaU - betaV)

    for t in range(n):

        Ag[t, t:n] = Ag[t, t:n] + minbeta[t] + minbeta[t:n]
        Ag[t:n, t] = Ag[t, t:n]
        Dg[t, t:n] = Dg[t, t:n] + absbeta[t] + absbeta[t:n]
        Dg[t:n, t] = Dg[t, t:n]

    for i in range(n - 1):
        for j in range(i + 1, n):
            Ag[i, j] = Ag[i, j] * mult[i] * mult[j]
            Dg[i, j] = Dg[i, j] * mult[i] * mult[j]

    for i in range(n):
        if mult[i] == 1:
            Ag[i, i] = 0
            Dg[i, i] = 0
        else:
            Ag[i, i] = Ag[i, i] * nchoosek(mult[i], 2)
            Dg[i, i] = Dg[i, i] * nchoosek(mult[i], 2)

    ag = triu(Ag).sum()
    dg = triu(Dg).sum()

    ag = ag + (ntotal - mult.sum()) * (mult * minbeta).sum()
    dg = dg + (ntotal - mult.sum()) * (mult * absbeta).sum()

    if ag + dg == 0:
        w = 1
    else:
        w = ag / (ag + dg)

    return w


def alphabeta(clusters, n):
    from numpy import zeros

    alpha = zeros((n, n))
    beta = zeros(n)

    k = len(clusters)

    for i in range(k):

        for t in range(len(clusters[i])):

            i0 = clusters[i][t]
            i1 = clusters[i][t : len(clusters[i])]
            alpha[i0, i1] = alpha[i0, i1] + 1
            alpha[i1, i0] = alpha[i0, i1]

        beta[clusters[i]] = beta[clusters[i]] + 1

    beta = beta - 1
    # to handle singletons not in |clusters|
    beta[beta == -1] = 0

    return alpha, beta


def intersect_sorted(veca, vecb):
    return list(set(veca).intersection(vecb))


def setdiff_sorted(veca, vecb):
    return list(set(veca) - set(vecb))


def nchoosek(n, k):
    if k == 0:
        r = 1
    else:
        r = n / k * nchoosek(n - 1, k - 1)
    return round(r)
