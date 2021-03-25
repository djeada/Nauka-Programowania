"""
Znajdz najmniejszy iloczyn dla trojek z listy.
"""

# Wersja 1
# Zlozonosc czasowa O(n^3)
# Zlozonosc pamieciowa O(1)
def minIloczynV1(lista):

    n = len(lista)

    if n <= 2:
        return False

    lista.sort()

    return min(lista[n - 1] * lista[n - 2] * lista[0], lista[0] * lista[1] * lista[2])


# Wersja 2
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def minIloczynV2(lista):

    n = len(lista)

    if n <= 2:
        return False

    maksLewo, maksPrawo, minLewo, minPrawo = [0] * n, [0] * n, [0] * n, [0] * n

    minimum = float("inf")
    maksimum = float("-inf")

    for i in range(n):
        minLewo[i] = minimum
        maksLewo[i] = maksimum

        minimum = min(minimum, lista[i])
        maksimum = max(maksimum, lista[i])

    minimum = float("inf")
    maksimum = float("-inf")

    for i in reversed(range(n)):
        minPrawo[i], maksPrawo[i] = minimum, maksimum
        minimum, maksimum = min(minimum, lista[i]), max(maksimum, lista[i])

    wynik = float("inf")

    for i in range(n - 2):
        wynik = min(
            wynik,
            min(
                lista[i + 1] * minLewo[i + 1] * minPrawo[i + 1],
                lista[i + 1] * minLewo[i + 1] * maksPrawo[i + 1],
                lista[i + 1] * maksLewo[i + 1] * minPrawo[i + 1],
                lista[i + 1] * maksLewo[i + 1] * maksPrawo[i + 1],
            ),
        )

    return wynik


# Wersja 3
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def minIloczynV3(lista):

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


# Testy poprawnosci
lista = [3, -1, -3, 2, 9, 4]
wynik = -108

assert minIloczynV3(lista) == wynik
assert minIloczynV2(lista) == wynik
assert minIloczynV1(lista) == wynik

lista = [3, 2, 1, 7, 8]
wynik = 6

assert minIloczynV3(lista) == wynik
assert minIloczynV2(lista) == wynik
assert minIloczynV1(lista) == wynik

lista = [1, 20, 2, -2, -4, -3]
wynik = -160

assert minIloczynV3(lista) == wynik
assert minIloczynV2(lista) == wynik
assert minIloczynV1(lista) == wynik
