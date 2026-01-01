"""
ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

"""


def bity_do_zmiany(liczba_a, liczba_b):
    """
    Funkcja zwraca ilosc bitow do zmiany liczby A w liczbe B.
    """

    n = liczba_a ^ liczba_b

    licznik_jedynek = 0
    while n:
        n &= n - 1
        licznik_jedynek += 1

    return licznik_jedynek


def test_bity_do_zmiany():
    assert bity_do_zmiany(0, 0) == 0
    assert bity_do_zmiany(1, 2) == 31
    assert bity_do_zmiany(34, 73) == 5


if __name__ == "__main__":

    test_bity_do_zmiany()
