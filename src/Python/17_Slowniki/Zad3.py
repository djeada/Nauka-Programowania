"""
Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami sa 
imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. 
Baza danych powinna umozliwiac:
a) Dodanie wypozyczonej ksiazki do danego czytelnika.
b) Zwrocenie wypozyczonej ksiazki przez czytelnika.
c) Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.
"""


def dodaj_ksiazke_do_czytelnika(baza_danych, czytelnik, ksiazka):
    """
    Funkcja dodaje ksiazke do listy ksiazek wypozyczonych przez czytelnika w bazie danych.
    """
    if czytelnik in baza_danych:
        baza_danych[czytelnik].add(ksiazka)
    else:
        baza_danych[czytelnik] = {ksiazka}

    return baza_danych


def zwroc_ksiazke_czytelnika(baza_danych, czytelnik, ksiazka):
    """
    Funkcja usuwa ksiazke z listy ksiazek wypozyczonych przez czytelnika w bazie danych.
    """
    if czytelnik in baza_danych:
        baza_danych[czytelnik].remove(ksiazka)

    return baza_danych


def wypisz_liste_wypozyczonych_ksiazek(baza_danych, czytelnik):
    """	
    Funkcja wypisuje liste wypozyczonych ksiazek dla danego czytelnika.
    """
    if czytelnik in baza_danych:
        print(f"Czytelnik {czytelnik} wypozyczyl nastepujace ksiazki:")
        for ksiazka in baza_danych[czytelnik]:
            print(ksiazka)
    else:
        print("Nie ma takiego czytelnika w bazie danych")


def test_dodaj_ksiazke_do_czytelnika():
    assert dodaj_ksiazke_do_czytelnika(
        {"Jan": {"Ksiazka1", "Ksiazka2"}}, "Jan", "Ksiazka3"
    ) == {"Jan": {"Ksiazka1", "Ksiazka2", "Ksiazka3"}}
    assert dodaj_ksiazke_do_czytelnika(
        {"Jan": {"Ksiazka1", "Ksiazka2"}}, "Adam", "Ksiazka3"
    ) == {"Jan": {"Ksiazka1", "Ksiazka2"}, "Adam": {"Ksiazka3"}}
    assert dodaj_ksiazke_do_czytelnika(
        {"Jan": {"Ksiazka1", "Ksiazka2"}}, "Jan", "Ksiazka1"
    ) == {"Jan": {"Ksiazka1", "Ksiazka2"}}


def test_zwroc_ksiazke_czytelnika():
    assert zwroc_ksiazke_czytelnika(
        {"Jan": {"Ksiazka1", "Ksiazka2"}}, "Jan", "Ksiazka1"
    ) == {"Jan": {"Ksiazka2"}}


if __name__ == "__main__":
    test_dodaj_ksiazke_do_czytelnika()
    test_zwroc_ksiazke_czytelnika()
