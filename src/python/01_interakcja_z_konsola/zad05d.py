r"""
ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★☆☆
**Tagi:** `potęgi`, `float`

### Treść

Wczytaj współczynniki $a$, $b$, $c$, wykładniki $m$, $n$ oraz argument $x$ i oblicz:

$y = a \cdot x^m + b \cdot x^n + c - a$

### Wejście

6 liczb, każda w osobnej linii:

* 1. linia: `a` — liczba rzeczywista
* 2. linia: `b` — liczba rzeczywista
* 3. linia: `c` — liczba rzeczywista
* 4. linia: `m` — liczba całkowita nieujemna
* 5. linia: `n` — liczba całkowita nieujemna
* 6. linia: `x` — liczba rzeczywista

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-100 \le a, b, c, x \le 100$
* $0 \le m, n \le 5$ (liczby całkowite)
* Jeśli $x = 0$, to $m, n \ge 1$ (nie pojawia się wyrażenie $0^0$).

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

Dla $a = b = c = m = n = x = 1$: $y = 1 \cdot 1^1 + 1 \cdot 1^1 + 1 - 1 = 2$.

"""


def wielomian(a, b, c, m, n, x):
    return a * x**m + b * x**n + c - a


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    m = int(input())
    n = int(input())
    x = float(input())
    print(f"{wielomian(a, b, c, m, n, x):.3f}")
