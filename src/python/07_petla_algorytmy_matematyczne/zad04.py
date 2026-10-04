r"""
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$ obliczone przy użyciu pętli. Przyjmij, że $0! = 1$.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — wartość $n!$.

### Ograniczenia

* `0 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

### Kod startowy

```python
def silnia(n):
    pass


n = int(input())
print(silnia(n))
```

"""


def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


if __name__ == "__main__":
    n = int(input())
    print(silnia(n))
