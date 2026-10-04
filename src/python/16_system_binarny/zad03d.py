r"""
ZAD-03D — Dzielenie całkowite bitowe

**Poziom:** ★★★
**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz iloraz całkowity $\lfloor a / b \rfloor$ (w Pythonie `a // b`), używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: iloraz całkowity `a` przez `b`.

### Ograniczenia

* $0 \le a \le 10^9$
* $1 \le b \le 10^9$ (dzielenie przez zero nie występuje)

### Przykład

**Wejście:**

```
9
3
```

**Wyjście:**

```
3
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* Postępuj jak w dzieleniu pisemnym: znajdź największe `b << k` nie większe od `a`, a potem dla kolejnych `k` (malejąco) odejmuj `b << k` od `a`, jeśli się mieści, i ustawiaj bit `k` ilorazu. Odejmowanie wykonaj bitowo, tak jak w ZAD-03B.

"""


def odejmij(a, b):
    """Odejmuje liczby naturalne (a >= b) wyłącznie operacjami bitowymi."""
    while b != 0:
        pozyczka = (~a & b) << 1
        a = a ^ b
        b = pozyczka
    return a


def podziel(a, b):
    """
    Dzielenie całkowite a // b (b > 0) jak dzielenie pisemne w systemie
    dwójkowym: od największego b * 2^k nie większego od a w dół do b * 1
    odejmujemy b * 2^k, jeśli się mieści, i ustawiamy bit k ilorazu.
    """
    dzielnik = b
    bit = 1
    while (dzielnik << 1) <= a:
        dzielnik <<= 1
        bit <<= 1

    iloraz = 0
    while bit != 0:
        if dzielnik <= a:
            a = odejmij(a, dzielnik)
            iloraz |= bit
        dzielnik >>= 1
        bit >>= 1
    return iloraz


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(podziel(a, b))
