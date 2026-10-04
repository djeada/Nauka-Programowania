r"""
ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik.

### Wejście

Jedna liczba naturalna `n`.

### Wyjście

Jedna liczba naturalna: suma cyfr liczby `n`.

### Ograniczenia

* $n \ge 0$

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
10
```

$1 + 3 + 2 + 3 + 1 = 10$.

### Uwagi

* Dla $n = 0$ suma cyfr wynosi `0`.
* Ostatnią cyfrę liczby otrzymasz jako `n % 10`, a liczbę bez ostatniej cyfry jako `n // 10`.

### Kod startowy

```python
def suma_cyfr(n):
    pass


n = int(input())
print(suma_cyfr(n))
```

"""


def suma_cyfr(n):
    """Zwraca sumę cyfr liczby naturalnej n."""
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


if __name__ == "__main__":
    n = int(input())
    print(suma_cyfr(n))
