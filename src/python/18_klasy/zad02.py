"""
ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę **Punkt**:

1. Konstruktor `(x=0, y=0)`.
2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
3. Metoda wypisująca współrzędne.
4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).

Program tworzy:

* A = (5, 5)
* B = (-3, -3)

Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.3137
```

"""

import math


class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def odleglosc(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


if __name__ == "__main__":
    punkt_a = Punkt(5, 5)
    punkt_b = Punkt(-3, -3)
    print(
        f"Odleglosc miedzy punktami A {punkt_a} i B {punkt_b} wynosi: {Punkt.odleglosc(punkt_a, punkt_b):.2f}."
    )
