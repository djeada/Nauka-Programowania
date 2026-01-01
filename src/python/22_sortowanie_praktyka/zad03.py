"""
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

* 1 linia: lista par posortowana jak w podpunkcie a)
* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

"""


def posortuj_liste_wzgledem_liczb(lista):
    """
    Funkcja zwraca liste par napisow i liczb posortowanych wzgledem liczb.
    """
    return sorted(lista, key=lambda x: x[1])


def posortuj_liste_wzgledem_dlugosci_napisow(lista):
    """
    Funkcja zwraca liste par napisow i liczb posortowanych wzgledem dlugosci napisow.
    """
    return sorted(lista, key=lambda x: len(x[0]))


def test_posortuj_liste_wzgledem_liczb():
    assert posortuj_liste_wzgledem_liczb([("c", 3), ("b", 2), ("a", 1)]) == [
        ("a", 1),
        ("b", 2),
        ("c", 3),
    ]


def test_posortuj_liste_wzgledem_dlugosci_napisow():
    assert posortuj_liste_wzgledem_dlugosci_napisow(
        [("ccc", 3), ("z", 1), ("xx", 2)]
    ) == [("z", 1), ("xx", 2), ("ccc", 3)]


if __name__ == "__main__":
    test_posortuj_liste_wzgledem_liczb()
    test_posortuj_liste_wzgledem_dlugosci_napisow()
