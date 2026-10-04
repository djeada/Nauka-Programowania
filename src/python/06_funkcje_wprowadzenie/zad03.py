r"""
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca **krotkę** czterech wartości logicznych, odpowiadających kolejno pytaniom:

a) Czy $a > b$?
b) Czy $a + b < 10$?
c) Czy obie liczby są nieparzyste?
d) Czy większa z liczb jest mniejsza od kwadratu `a`, czyli czy $\max(a, b) < a^2$?

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje cztery zwrócone wartości.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Cztery linie z wartościami `True` albo `False` — odpowiedzi na pytania a), b), c), d) w tej kolejności.

### Ograniczenia

* $a \ge 0$, $b \ge 0$

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
True
True
False
True
```

$3 > 2$, $3 + 2 = 5 < 10$, liczba $2$ jest parzysta, $\max(3, 2) = 3 < 9$.

### Uwagi

* Kilka wartości zwrócisz naraz instrukcją `return w1, w2, w3, w4` — Python spakuje je w krotkę.

### Kod startowy

```python
def sprawdz_warunki(a, b):
    pass


a = int(input())
b = int(input())
w1, w2, w3, w4 = sprawdz_warunki(a, b)
print(w1)
print(w2)
print(w3)
print(w4)
```

"""


def sprawdz_warunki(a, b):
    """Zwraca krotkę czterech wartości logicznych opisanych w treści zadania."""
    pierwsza_wieksza = a > b
    suma_mniejsza_od_10 = a + b < 10
    obie_nieparzyste = a % 2 == 1 and b % 2 == 1
    wieksza_mniejsza_od_kwadratu_a = max(a, b) < a**2
    return (
        pierwsza_wieksza,
        suma_mniejsza_od_10,
        obie_nieparzyste,
        wieksza_mniejsza_od_kwadratu_a,
    )


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    w1, w2, w3, w4 = sprawdz_warunki(a, b)
    print(w1)
    print(w2)
    print(w3)
    print(w4)
