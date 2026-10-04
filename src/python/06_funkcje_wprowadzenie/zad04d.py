r"""
ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

Program wczytuje `a`, `b` i `c`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`
* 3. linia: liczba naturalna `c`

### Wyjście

Jedna liczba naturalna: największa z liczb `a`, `b`, `c`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$, $c \ge 0$

### Przykład

**Wejście:**

```
3
2
1
```

**Wyjście:**

```
3
```

### Uwagi

* Pamiętaj o przypadku, gdy dwie lub trzy liczby są równe.
* Wewnątrz funkcji możesz wywołać inną funkcję. Napisz najpierw pomocniczą funkcję `max_z_dwoch(a, b)` (analogiczną do `min_z_dwoch` z zadania ZAD-04A) i wywołaj ją dwa razy.

### Kod startowy

```python
def max_z_trzech(a, b, c):
    pass


a = int(input())
b = int(input())
c = int(input())
print(max_z_trzech(a, b, c))
```

"""


def max_z_dwoch(a, b):
    """Zwraca większą z dwóch liczb."""
    if a > b:
        return a
    return b


def max_z_trzech(a, b, c):
    """Zwraca największą z trzech liczb."""
    return max_z_dwoch(max_z_dwoch(a, b), c)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(max_z_trzech(a, b, c))
