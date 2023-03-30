"""
Tytul: Wyszukiwanie indeksu klucza w cyklicznie posortowanej liscie.
Tresc: Otrzymujesz cyklicznie posortowana liste oraz klucz. Znajdz indeks pierwszego wystapienia klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Cyklicznie posortowana lista, klucz.
Dane wyjsciowe: Indeks pierwszego wystapienia klucza lub -1.
Przyklad:
Dla cyklicznie posortowanej listy [3, 4, 5, 6, 1, 2] i klucza 4, powinno zostac zwrocone 2.

"""


def znajdz_klucz_v1(lista, klucz):

    lewo = 0
    prawo = len(lista) - 1

    while lewo <= prawo:

        sr = (lewo + prawo) // 2

        if klucz == lista[sr]:
            return sr

        if lista[sr] <= lista[prawo]:

            if lista[sr] < klucz and klucz <= lista[prawo]:
                lewo = sr + 1

            else:
                prawo = sr - 1

        else:

            if lista[lewo] <= klucz and klucz < lista[sr]:
                prawo = sr - 1

            else:
                lewo = sr + 1

    return -1


if __name__ == "__main__":

    lista = [27, 31, 32, 3, 5, 9, 10, 15]
    klucz = 31
    wynik = 1

    assert znajdz_klucz_v1(lista, klucz) == wynik

    lista = [4, 7, 12, 32, 51, 90, 100, 1, 2]
    klucz = -5
    wynik = -1

    assert znajdz_klucz_v1(lista, klucz) == wynik

