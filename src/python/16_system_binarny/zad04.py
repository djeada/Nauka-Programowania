"""
ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.

ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

"""


# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def przygotuj_tablice():
    """
    Funkcja zwraca tablice zawierajaca ilosc ustawionych bitow dla kazdej liczby w zakresie 0-255.
    """

    def _ustawione_bity(liczba):
        """
        Funkcja zwraca ilosc ustawionych bitow w liczbie.
        """
        suma = 0
        while liczba > 0:
            if liczba & 1:
                suma += 1
            liczba >>= 1
        return suma

    return [_ustawione_bity(x) for x in range(256)]


# Zlozonosc czasowa O(1)
# Zlozonosc pamieciowa O(1)
def ustawione_bity(tablica, n):
    """
    Funkcja zwraca ilosc ustawionych bitow w liczbie.
    """
    return (
        tablica[n & 0xFF]
        + tablica[(n >> 8) & 0xFF]
        + tablica[(n >> 16) & 0xFF]
        + tablica[(n >> 24) & 0xFF]
    )


def test_ustawione_bity():
    tablica = przygotuj_tablice()
    assert ustawione_bity(tablica, 0) == 0
    assert ustawione_bity(tablica, 26) == 3
    assert ustawione_bity(tablica, 9832) == 6
    assert ustawione_bity(tablica, 10000) == 5


if __name__ == "__main__":

    test_ustawione_bity()
