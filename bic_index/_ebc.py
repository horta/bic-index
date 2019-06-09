def ebc(ba, bb, nr, nc):
    U = biclusters2UBackground(ba, nr, nc)
    V = biclusters2UBackground(bb, nr, nc)

    return exbcubed(U, V)


def biclusters2UBackground(clusters, nr, nc):
    from numpy import ones, zeros, asarray, where

    # nr: number of rows
    # nc: number of columns

    k = len(clusters)

    noise = ones(nr * nc)

    for i in range(k):

        rows = asarray(clusters[i][0], int)
        cols = clusters[i][1]

        for s in range(len(cols)):

            noise[rows + nr * cols[s]] = 0

    nnoise = int(noise.sum())

    U = zeros((k + nnoise, nr * nc))

    for i in range(k):

        rows = asarray(clusters[i][0], int)
        cols = clusters[i][1]

        for s in range(len(cols)):

            U[i, rows + nr * cols[s]] = 1

    noise = where(noise == 1)[0]
    t = asarray(range(k, k + nnoise), int)
    shape = U.shape
    U = U.ravel(order="F")
    U[t + (noise * (k + nnoise))] = 1
    U = U.reshape(shape, order="F")

    return U


def exbcubed(U, V):
    # E. Amigo, J. Gonzalo, J. Artiles, and F. Verdejo, "A comparison of
    # extrinsic clustering evaluation metrics based on formal constraints,"
    # Inf. Retr., vol. 12, no. 4, pp. 461?486, Aug. 2009.

    Mu = U.T @ U
    Mv = V.T @ V

    prec = ExBCubedPrecision(Mu, Mv)
    recall = ExBCubedRecall(Mu, Mv)

    return 1 / (0.5 * (1 / prec + 1 / recall))


def ExBCubedPrecision(Mu, Mv):
    from numpy import mean, minimum

    n = Mu.shape[0]

    MM = minimum(Mu, Mv)

    r = 0
    for i in range(n):

        indices = Mu[i, :] > 0

        prec = MM[i, indices] / Mu[i, indices]

        r = r + mean(prec)
    return r / n


def ExBCubedRecall(Mu, Mv):

    return ExBCubedPrecision(Mv, Mu)
