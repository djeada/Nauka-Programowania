"""
Tytul: Sortowanie listy miast.
Tresc: Klasa Miasto ma dwie wlasciwosci: nazwa (napis) oraz liczba_mieszkancow (liczba naturalna). Posortuj liste miast wzgledem nazwy oraz wzgledem liczby mieszkancow.
Dane wejsciowe: Lista miast.
Dane wyjsciowe: Posortowana lista miast.
Przyklad:
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)].
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("Paris", 2150000), Miasto("New York", 8400000)].

"""


class Miasto:
    def __init__(self, nazwa, liczba_mieszkancow):
        self.nazwa = nazwa
        self.liczba_mieszkancow = liczba_mieszkancow

    def __repr__(self):
        return self.nazwa + " : " + str(self.liczba_mieszkancow)


def sortuj_liste_miast_wzgledem_nazwy(lista_miast):
    return sorted(lista_miast, key=lambda x: x.nazwa)


def sortuj_liste_miast_wzgledem_liczby_mieszkancow(lista_miast):
    return sorted(lista_miast, key=lambda x: x.liczba_mieszkancow)


def test_sortuj_liste_miast_wzgledem_nazwy():
    miasta = [
        Miasto("New York", 8400000),
        Miasto("Paris", 2150000),
        Miasto("Berlin", 3800000),
    ]

    oczekiwana = [
        Miasto("Berlin", 3800000),
        Miasto("New York", 8400000),
        Miasto("Paris", 2150000),
    ]

    assert sortuj_liste_miast_wzgledem_nazwy(miasta) == oczekiwana


def test_sortuj_liste_miast_wzgledem_liczby_mieszkancow():
    miasta = [
        Miasto("New York", 8400000),
        Miasto("Paris", 2150000),
        Miasto("Berlin", 3800000),
    ]

    oczekiwana = [
        Miasto("New York", 8400000),
        Miasto("Paris", 2150000),
        Miasto("Berlin", 3800000),
    ]

    assert sortuj_liste_miast_wzgledem_liczby_mieszkancow(miasta) == oczekiwana


if __name__ == "__main__":
    test_sortuj_liste_miast_wzgledem_nazwy()
    test_sortuj_liste_miast_wzgledem_liczby_mieszkancow()

