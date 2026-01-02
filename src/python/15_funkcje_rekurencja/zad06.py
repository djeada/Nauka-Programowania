"""
ZAD-06 — Miejsca zerowe równania kwadratowego

**Poziom:** ★★☆
**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

"""

import math


def pierwiastki_kwadratowe_rek(a, b, c):
    """
    Oblicza pierwiastki równania kwadratowego.
    
    Złożoność czasowa: O(1)
    Złożoność pamięciowa: O(1)
    """
    delta = b * b - 4 * a * c
    
    if delta < 0:
        return []
    elif delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return sorted([x1, x2])


if __name__ == "__main__":
    line = input().strip().split()
    a, b, c = float(line[0]), float(line[1]), float(line[2])
    wynik = pierwiastki_kwadratowe_rek(a, b, c)
    print(str(wynik) if wynik else "[]")
