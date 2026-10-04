r"""
ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Jedna liczba naturalna: mniejsza z liczb `a` i `b`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$

### Przykład

**Wejście:**

```
3
1
```

**Wyjście:**

```
1
```

### Uwagi

* Spróbuj napisać funkcję bez wbudowanej funkcji `min` — porównaj liczby instrukcją `if`.
* Jeśli liczby są równe, zwróć dowolną z nich.

### Kod startowy

```python
def min_z_dwoch(a, b):
    pass


a = int(input())
b = int(input())
print(min_z_dwoch(a, b))
```

"""


def min_z_dwoch(a, b):
    """Zwraca mniejszą z dwóch liczb."""
    if a < b:
        return a
    return b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(min_z_dwoch(a, b))
