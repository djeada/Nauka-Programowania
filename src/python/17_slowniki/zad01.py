"""
ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

* 1 linia: `n` (n ≥ 1)

### Wyjście

* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

"""


def stworz_slownik(n):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace kolejnymi
    liczbami naturalnymi mniejszymi od podanej liczby n
    oraz wartosci bedacymi kwadratami kluczy.
    """

    slownik = {}
    for i in range(n):
        slownik[i] = i**2
    return slownik


def test_stworz_slownik():
    assert stworz_slownik(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    assert stworz_slownik(0) == {}


if __name__ == "__main__":

    test_stworz_slownik()
