"""
ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

* `dodaj [imię] [tytuł]`
* `zwróć [imię] [tytuł]`
* `lista [imię]`

Po `lista [imię]` wypisz:

* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

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
