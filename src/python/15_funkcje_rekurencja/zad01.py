"""
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `Horner`, `I/O`

### Treść

Wczytaj współczynniki wielomianu ( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 ) oraz liczbę ( x ). Oblicz wartość wielomianu w punkcie ( x ).

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

### Uwagi o formatowaniu

* Użyj schematu Hornera (jest najprostszy i najszybszy).

"""


def liczby(n):
    """
    Funkcja zwraca napis skladajacy sie z liczb naturalnych
    mniejszych od podanej liczby n.
    """

    if n <= 0:
        return ""

    if n == 1:
        return "1"
    else:
        return str(n) + ", " + liczby(n - 1)


def test_liczby():

    assert liczby(0) == ""
    assert liczby(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"


if __name__ == "__main__":

    test_liczby()
