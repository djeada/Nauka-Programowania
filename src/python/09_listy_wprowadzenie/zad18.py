"""
Tytul: Znalezienie indeksu najmniejszego elementu w posortowanej i przesunietej w prawo liscie.
Tresc: Dla otrzymanej listy liczb calkowitych, znajdz indeks najmniejszego elementu. Lista jest posortowana rosnaco, ale zostala przesunieta w prawo o okreslona liczbe miejsc. Przykladowo dla przesuniecia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.
Dane wejsciowe: Lista liczb calkowitych oraz liczba naturalna okreslajaca przesuniecie w prawo.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrocona liczba: 2.

"""


def znajdz_min_indeks(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return i + 1

    return 0


def test_znajdz_min_indeks():
    assert znajdz_min_indeks([7, 8, -1, 4, 5]) == 2
    assert znajdz_min_indeks([2, 3, 4, 5, 6]) == 0
    assert znajdz_min_indeks([8, 9, 10, 11, 1]) == 4


if __name__ == "__main__":

    test_znajdz_min_indeks()
