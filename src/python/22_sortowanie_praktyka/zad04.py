"""
ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: napis (bez spacji)

### Wyjście

* 1 linia: lista napisów posortowana jak w przykładzie

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
['a', 'ab', 'abc', 'abcd']
```

"""


def posortuj_liste_wzgledem_dlugosci_napisow(lista_napisow):
    """
    Funkcja sortuje liste napisow wzgledem dlugosci napisow.
    """
    return sorted(lista_napisow, key=len)


def test_posortuj_liste_wzgledem_dlugosci_napisow():
    assert posortuj_liste_wzgledem_dlugosci_napisow(
        ["Ala", "ma", "kota", "a", "kot", "ma", "Ale"]
    ) == ["a", "ma", "ma", "Ala", "kot", "Ale", "kota"]


if __name__ == "__main__":
    test_posortuj_liste_wzgledem_dlugosci_napisow()
