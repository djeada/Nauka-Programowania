r"""
ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów $A(x_A, y_A)$, $B(x_B, y_B)$, $C(x_C, y_C)$.
Wypisz `Tak`, jeśli punkty mogą być wierzchołkami trójkąta (czyli **nie leżą** na jednej prostej), a w przeciwnym razie `Nie`.

### Wejście

Trzy linie — w każdej dwie liczby całkowite `x y` oddzielone spacją:

* 1. linia: współrzędne punktu `A`
* 2. linia: współrzędne punktu `B`
* 3. linia: współrzędne punktu `C`

### Wyjście

Jedno słowo: `Tak` albo `Nie`.

### Przykład

**Wejście:**

```
-3 -2
-3 1
-3 0
```

**Wyjście:**

```
Nie
```

Wszystkie trzy punkty leżą na prostej $x = -3$.

### Uwagi

* Punkty leżą na jednej prostej wtedy i tylko wtedy, gdy $(x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A) = 0$ (to wyrażenie jest równe podwojonemu polu trójkąta $ABC$, z dokładnością do znaku).
* Jeśli dwa punkty się pokrywają, trójkąta nie da się zbudować.

"""


def czy_trojkat(a, b, c):
    """Sprawdza, czy punkty a, b, c (listy [x, y]) nie leżą na jednej prostej."""
    xA, yA = a
    xB, yB = b
    xC, yC = c
    podwojone_pole = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)
    return podwojone_pole != 0


if __name__ == "__main__":
    punkty = []
    for _ in range(3):
        punkty.append([int(x) for x in input().split()])
    print("Tak" if czy_trojkat(*punkty) else "Nie")
