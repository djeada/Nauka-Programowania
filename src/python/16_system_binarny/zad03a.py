r"""
ZAD-03A — Dodawanie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a + b$, używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a + b$.

### Ograniczenia

* $0 \le a, b \le 10^9$ (liczby ujemne nie występują)

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
5
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* `a ^ b` to suma bez przeniesień, a `(a & b) << 1` to przeniesienia. Powtarzaj, dopóki przeniesienia są niezerowe.

"""


def dodaj(a, b):
    """
    Dodaje liczby naturalne bez użycia +.
    a ^ b to suma bez przeniesień, (a & b) << 1 to przeniesienia;
    powtarzamy, dopóki są jakieś przeniesienia.
    """
    while b != 0:
        przeniesienie = (a & b) << 1
        a = a ^ b
        b = przeniesienie
    return a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(dodaj(a, b))
