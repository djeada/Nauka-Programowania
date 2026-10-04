r"""
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, a w przeciwnym razie `False`.

Liczba pierwsza to liczba naturalna większa od `1`, której jedynymi dzielnikami są `1` i ona sama.

Program wczytuje `n`, wywołuje funkcję i wypisuje zwróconą wartość logiczną (`print(czy_pierwsza(n))`).

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Jedno słowo: `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
True
```

### Przykład 2

**Wejście:**

```
4
```

**Wyjście:**

```
False
```

### Uwagi

* `1` nie jest liczbą pierwszą.
* W prostym rozwiązaniu sprawdzasz dzielniki od `2` do `n - 1`. Wystarczy jednak sprawdzać dzielniki `d` spełniające $d \cdot d \leq n$, czyli do $\lfloor \sqrt{n} \rfloor$.

### Kod startowy

```python
def czy_pierwsza(n):
    pass


n = int(input())
print(czy_pierwsza(n))
```

"""


def czy_pierwsza(n):
    if n < 2:
        return False

    dzielnik = 2
    while dzielnik * dzielnik <= n:
        if n % dzielnik == 0:
            return False
        dzielnik += 1
    return True


if __name__ == "__main__":
    n = int(input())
    print(czy_pierwsza(n))
