"""
Zaimplementuj sortowanie szybkie.
"""

import random

# Zlozonosc czasowa O(nlogn)
def sortuj_v1(tablica):
    def _sortuj(tablica, start, stop):

        if stop - start < 2:
            return

        i = random.randint(start, stop - 1)
        tablica[i], tablica[stop - 1] = tablica[stop - 1], tablica[i]
        i = partycja(tablica, start, stop)
        _sortuj(tablica, start, i)
        _sortuj(tablica, i + 1, stop)

    def partycja(tablica, start, stop):
        i = start
        j = stop - 2
        klucz = tablica[stop - 1]

        while i <= j:
            if tablica[i] <= klucz:
                i += 1
            elif tablica[j] >= klucz:
                j -= 1
            else:
                tablica[i], tablica[j] = tablica[j], tablica[i]
                i += 1
                j -= 1
        tablica[i], tablica[stop - 1] = tablica[stop - 1], tablica[i]
        return i

    _sortuj(tablica, 0, len(tablica))


# Zlozonosc czasowa O(nlogn)
def sortuj_v2(tablica):
    def _sortuj(tablica, start, stop):

        if stop - start < 2:
            return

        klucz = tablica[random.randint(start, stop - 1)]
        indeks_1 = indeks_2 = start
        indeks_3 = stop

        while indeks_2 < indeks_3:
            if tablica[indeks_2] < klucz:
                tablica[indeks_2], tablica[indeks_1] = (
                    tablica[indeks_1],
                    tablica[indeks_2],
                )
                indeks_1 += 1
                indeks_2 += 1

            elif tablica[indeks_2] == klucz:
                indeks_2 += 1

            else:
                indeks_3 -= 1
                tablica[indeks_2], tablica[indeks_3] = (
                    tablica[indeks_3],
                    tablica[indeks_2],
                )

        _sortuj(tablica, start, indeks_1)
        _sortuj(tablica, indeks_3, stop)

    _sortuj(tablica, 0, len(tablica))


# Testy Poprawnosci
def test_1():
    tablica = [4, 2, 5, 3, 1]
    wynik = [1, 2, 3, 4, 5]

    sortuj_v1(tablica)

    assert tablica == wynik


def test_2():
    tablica = [6, 5, 1, 2, 3, 1, 4, 3, 5, 2, 3]
    wynik = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

    sortuj_v1(tablica)

    assert tablica == wynik


def test_3():
    tablica = [4, 2, 5, 3, 1]
    wynik = [1, 2, 3, 4, 5]

    sortuj_v2(tablica)

    assert tablica == wynik


def test_4():
    tablica = [6, 5, 1, 2, 3, 1, 4, 3, 5, 2, 3]
    wynik = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

    sortuj_v2(tablica)

    assert tablica == wynik


def main():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == "__main__":
    main()
