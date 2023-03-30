"""
Tytul: Klucz to imie, wartosc lista wypozyczonych ksiazek.
Tresc: Zbuduj prosta baze danych dla biblioteki oparta o slownik, w ktorym kluczami sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. Baza danych powinna umozliwiac:
1. Dodanie wypozyczonej ksiazki do danego czytelnika.
2. Zwrocenie wypozyczonej ksiazki przez czytelnika.
3. Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.

"""

def sortuj_wzgledem_kluczy(slownik):
    """
    Funkcja sortuje slownik wzgledem kluczy.
    """
    return sorted(slownik.items(), key=lambda x: x[0])

def sortuj_wzgledem_wartosci(slownik):
    """
    Funkcja sortuje slownik wzgledem wartosci.
    """
    return sorted(slownik.items(), key=lambda x: x[1])

def test_sortuj_wzgledem_kluczy():
    assert sortuj_wzgledem_kluczy({"a": 2, "c": 1, "b": 3}) == [
        ("a", 2),
        ("b", 3),
        ("c", 1),
    ]

def test_sortuj_wzgledem_wartosci():
    assert sortuj_wzgledem_wartosci({"a": 2, "c": 1, "b": 3}) == [
        ("c", 1),
        ("a", 2),
        ("b", 3),
    ]

if __name__ == "__main__":

    test_sortuj_wzgledem_kluczy()
    test_sortuj_wzgledem_wartosci()

