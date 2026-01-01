"""
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

"""


def stworz_slownik(lista_a, lista_b):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace elementami
    pierwszej listy i wartosci bedace elementami drugiej listy.
    """

    if len(lista_a) != len(lista_b):
        return {}

    return dict(zip(lista_a, lista_b))


def test_stworz_slownik():
    assert stworz_slownik([1, 2, 3], [4, 5, 6]) == {1: 4, 2: 5, 3: 6}
    assert stworz_slownik([1, 2, 3], [4, 5]) == {}


if __name__ == "__main__":

    test_stworz_slownik()
