"""
Zaimplementuj sortowanie przez wstawianie.
"""

# Zlozonosc czasowa O(n^2)
def sortuj_v1(tablica):

    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1

        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j -= 1

        tablica[j + 1] = klucz


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


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
