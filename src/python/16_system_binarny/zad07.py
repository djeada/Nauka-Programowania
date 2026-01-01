"""
ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

### Uwagi

* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

"""


def zamien_sasiadow(liczba):
    """
    Funkcja zamienia sasiadujace bity w binarnym zapisie liczby.
    """
    parzyste = liczba & 0xAAAAAAAA
    nieparzyste = liczba & 0x55555555

    parzyste >>= 1
    nieparzyste <<= 1

    return parzyste | nieparzyste


def test_zamien_sasiadow():
    assert zamien_sasiadow(9131) == 4951


if __name__ == "__main__":
    test_zamien_sasiadow()
