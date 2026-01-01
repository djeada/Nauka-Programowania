"""
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

* 1 linia: lista miast po sortowaniu a)
* 2 linia: lista miast po sortowaniu b)

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

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
