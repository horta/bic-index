from numpy.testing import assert_allclose

from bic_index import (
    anne_rnia,
    ayadi,
    biclustering_error,
    bozdag_extra,
    bozdag_uncovered,
    csi,
    ebc,
    eren_recovery,
    eren_relevance,
    fabia,
    lew,
    prelic_recovery,
    prelic_relevance,
    stmaria,
    wdic,
    wjac,
)

a = [([0, 2], [0, 1, 4])]
b = [([0, 2], [0, 1]), ([3, 4], [0, 3, 4])]

nr = 5
nc = 6


def test_prelic_relevance():
    assert_allclose(prelic_relevance(a, b), 0.816496580927726)


def test_prelic_recovery():
    assert_allclose(prelic_recovery(a, b), 0.5400617248673216)


def test_anne_rnia():
    assert_allclose(anne_rnia(a, b, nr, nc), 0.33333333333333337)


def test_biclustering_error():
    assert_allclose(biclustering_error(a, b, nr, nc), 0.33333333333333337)


def test_lew():
    assert_allclose(lew(a, b), 0.8)


def test_stmaria():
    assert_allclose(stmaria(a, b, nr, nc), 0.8)


def test_wjac():
    assert_allclose(wjac(a, b, nr), 0.6666666666666666)


def test_wdic():
    assert_allclose(wdic(a, b, nr, nc), 0.8)


def test_fabia():
    assert_allclose(fabia(a, b, nr), 0.3333333333333333)


def test_bozdag_uncovered():
    assert_allclose(bozdag_uncovered(a, b, nr), 0.4)


def test_bozdag_extra():
    assert_allclose(bozdag_extra(a, b, nr), 0.6666666666666666)


def test_ayadi():
    assert_allclose(ayadi(a, b), 0.6666666666666666)


def test_eren_relevance():
    assert_allclose(eren_relevance(a, b, nr, nc), 0.6666666666666666)


def test_eren_recovery():
    assert_allclose(eren_recovery(a, b, nr, nc), 0.3333333333333333)


def test_csi():
    assert_allclose(csi(a, b, nr, nc), 0.2)


def test_ebc():
    assert_allclose(ebc(a, b, nr, nc), 0.8653846153846154)
