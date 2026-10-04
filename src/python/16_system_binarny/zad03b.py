r"""
ZAD-03B — Odejmowanie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a - b$, używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a - b$.

### Ograniczenia

* $0 \le b \le a \le 10^9$ — wynik nigdy nie jest ujemny

### Przykład

**Wejście:**

```
7
5
```

**Wyjście:**

```
2
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* `a ^ b` to różnica bez pożyczek, a `(~a & b) << 1` to pożyczki. Powtarzaj, dopóki pożyczki są niezerowe.

"""


def odejmij(a, b):
    """
    Odejmuje liczby naturalne (a >= b) bez użycia -.
    a ^ b to różnica bez pożyczek, (~a & b) << 1 to pożyczki;
    powtarzamy, dopóki są jakieś pożyczki.
    """
    while b != 0:
        pozyczka = (~a & b) << 1
        a = a ^ b
        b = pozyczka
    return a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(odejmij(a, b))
