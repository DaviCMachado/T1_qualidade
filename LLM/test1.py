import convns as N

def test_N1():
    assert N.N1 == 16

def test_N2():
    assert N.N2 == 1 + (64 - 6) // 2  # 1 + 58 // 2 = 30

def test_N3():
    assert N.N3 == N.N1 * N.N2 * N.N2

def test_N4():
    assert N.N4 == N.N1  # padding não muda canais

def test_N5():
    assert N.N5 == 1 + (N.N2 - 2) // 2

def test_N6():
    assert N.N6 == N.N4 * N.N5 * N.N5

def test_N7():
    assert N.N7 == 32

def test_N8():
    assert N.N8 == 1 + (N.N5 - 3) // 1

def test_N9():
    assert N.N9 == N.N7 * N.N8 * N.N8

def test_N10():
    assert N.N10 == N.N7

def test_N11():
    assert N.N11 == 1 + (N.N8 - 2) // 2

def test_N12():
    assert N.N12 == N.N10 * N.N11 * N.N11

def test_N13():
    assert N.N13 == 10  # número de classes
