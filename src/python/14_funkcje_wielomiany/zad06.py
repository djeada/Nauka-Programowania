r"""
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję `miejsca_zerowe(a, b, c)`, która zwraca listę wszystkich **rzeczywistych** rozwiązań równania $ax^2 + bx + c = 0$, posortowaną rosnąco. Pierwiastek podwójny umieść na liście tylko raz.

Program wczytuje współczynniki, wywołuje funkcję i wypisuje wynik.

### Wejście

Jedna linia: trzy liczby całkowite `a b c` oddzielone spacją (`a ≠ 0`).

### Wyjście

* Jeśli równanie ma rozwiązania rzeczywiste: jedna linia z rozwiązaniami w kolejności rosnącej, oddzielonymi spacją, każde z dokładnością do **2 miejsc po przecinku** (np. `-1.62 0.62`). Pierwiastek podwójny wypisz raz.
* Jeśli równanie nie ma rozwiązań rzeczywistych: dokładnie `Brak miejsc zerowych`.

### Ograniczenia

* `-100 ≤ a, b, c ≤ 100`, `a ≠ 0`

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
-1.00
```

$\Delta = 2^2 - 4 \cdot 1 \cdot 1 = 0$, więc jest jeden (podwójny) pierwiastek $x = -1$.

### Przykład 2

**Wejście:**

```
1 0 1
```

**Wyjście:**

```
Brak miejsc zerowych
```

### Uwagi

* Oblicz $\Delta = b^2 - 4ac$. Dla $\Delta < 0$ brak rozwiązań, dla $\Delta = 0$ jest jedno: $x = \frac{-b}{2a}$, a dla $\Delta > 0$ dwa: $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$.
* Uważaj na kolejność: gdy $a < 0$, wzór z „$+$” daje **mniejszy** pierwiastek — posortuj wynik.

### Kod startowy

```python
import math


def miejsca_zerowe(a, b, c):
    pass


a, b, c = [int(s) for s in input().split()]
pierwiastki = miejsca_zerowe(a, b, c)
if pierwiastki:
    print(" ".join(f"{x:.2f}" for x in pierwiastki))
else:
    print("Brak miejsc zerowych")
```

"""

import math


def miejsca_zerowe(a, b, c):
    """Zwraca posortowaną listę rzeczywistych pierwiastków równania ax^2 + bx + c = 0."""
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a) + 0.0]  # + 0.0 zamienia ewentualne -0.0 na 0.0
    pierwiastek_delty = math.sqrt(delta)
    x1 = (-b - pierwiastek_delty) / (2 * a)
    x2 = (-b + pierwiastek_delty) / (2 * a)
    return sorted([x1 + 0.0, x2 + 0.0])


if __name__ == "__main__":
    a, b, c = [int(s) for s in input().split()]
    pierwiastki = miejsca_zerowe(a, b, c)
    if pierwiastki:
        print(" ".join(f"{x:.2f}" for x in pierwiastki))
    else:
        print("Brak miejsc zerowych")
