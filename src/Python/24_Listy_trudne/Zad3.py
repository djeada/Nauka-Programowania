"""
Znajdz najmniejszy iloczyn dla trojek z listy.
"""

# Wersja 1
# Zlozonosc czasowa O(nlogn)
# Zlozonosc pamieciowa O(1)
def min_iloczyn_v1(lista):

    n = len(lista)

    if n <= 2:
        raise ValueError("Listy musza byc rownej dlugosci.")

    lista.sort()

    return min(lista[n - 1] * lista[n - 2] * lista[0], lista[0] * lista[1] * lista[2])


# Wersja 2
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def min_iloczyn_v2(lista):

    n = len(lista)

    if n <= 2:
        raise ValueError("Listy musza byc rownej dlugosci.")

    maks_lewo, maks_prawo, min_lewo, min_prawo = [0] * n, [0] * n, [0] * n, [0] * n

    minimum = float("inf")
    maksimum = float("-inf")

    for i in range(n):
        min_lewo[i] = minimum
        maks_lewo[i] = maksimum

        minimum = min(minimum, lista[i])
        maksimum = max(maksimum, lista[i])

    minimum = float("inf")
    maksimum = float("-inf")

    for i in reversed(range(n)):
        min_prawo[i] = minimum
        maks_prawo[i] = maksimum

        minimum = min(minimum, lista[i])
        maksimum = max(maksimum, lista[i])

    wynik = float("inf")

    for i in range(n - 2):
        wynik = min(
            wynik,
            min(
                lista[i + 1] * min_lewo[i + 1] * min_prawo[i + 1],
                lista[i + 1] * min_lewo[i + 1] * maks_prawo[i + 1],
                lista[i + 1] * maks_lewo[i + 1] * min_prawo[i + 1],
                lista[i + 1] * maks_lewo[i + 1] * maks_prawo[i + 1],
            ),
        )

    return wynik


# Wersja 3
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def min_iloczyn_v3(lista):

    n = len(lista)

    if n <= 2:
        raise ValueError("Listy musza byc rownej dlugosci.")

    min1, min2, min3, maks1, maks2 = lista[0], lista[0], lista[0], lista[0], lista[0]

    for x in lista:
        if x < min1:
            min3 = min2
            min2 = min1
            min1 = x

        elif x < min2:
            min3 = min2
            min2 = x

        elif x < min3:
            min3 = x

        if x > maks1:
            maks2 = maks1
            maks1 = x

        elif x > maks2:
            maks2 = x

    return min(maks1 * maks2 * min1, min1 * min2 * min3)


# Testy Poprawnosci
def test_1():
    lista = [3, -1, -3, 2, 9, 4]
    wynik = -108

    assert min_iloczyn_v3(lista) == wynik
    assert min_iloczyn_v2(lista) == wynik
    assert min_iloczyn_v1(lista) == wynik


def test_2():
    lista = [3, 2, 1, 7, 8]
    wynik = 6

    assert min_iloczyn_v3(lista) == wynik
    assert min_iloczyn_v2(lista) == wynik
    assert min_iloczyn_v1(lista) == wynik


def test_3():
    lista = [1, 20, 2, -2, -4, -3]
    wynik = -160

    assert min_iloczyn_v3(lista) == wynik
    assert min_iloczyn_v2(lista) == wynik
    assert min_iloczyn_v1(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
