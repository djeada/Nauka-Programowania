r"""
ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę `Punkt` opisującą punkt na płaszczyźnie:

1. Konstruktor `__init__(self, x=0, y=0)` zapamiętuje współrzędne.
2. Metoda statyczna `odleglosc(p1, p2)` zwraca odległość między punktami `p1` i `p2`:
   $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
3. Metoda `__str__()` zwraca napis z współrzędnymi w postaci `(x, y)`, np. `(5, -3)`.
4. Metoda `__eq__(other)` sprawdza, czy dwa punkty są równe (obie współrzędne identyczne). Operator `!=` Python wyznaczy wtedy sam.

Program wczytuje współrzędne punktów $A$ i $B$, tworzy dwa obiekty `Punkt`, wypisuje je, podaje odległość między nimi i informuje, czy punkty są równe.

### Wejście

* 1. linia: dwie liczby całkowite $x_A$ i $y_A$ oddzielone spacją
* 2. linia: dwie liczby całkowite $x_B$ i $y_B$ oddzielone spacją

### Wyjście

Cztery linie:

```
Punkt A: (xA, yA)
Punkt B: (xB, yB)
Odległość między punktami A i B: <odległość>
Punkty są równe.
```

Odległość wypisz z dokładnością do 2 miejsc po przecinku. W ostatniej linii wypisz `Punkty są równe.` albo `Punkty są różne.`

### Ograniczenia

* $-1000 \le x, y \le 1000$

### Przykład

**Wejście:**

```
5 5
-3 -3
```

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.31
Punkty są różne.
```

$\sqrt{8^2 + 8^2} = \sqrt{128} \approx 11.3137$.

### Kod startowy

```python
import math


class Punkt:
    def __init__(self, x=0, y=0):
        pass

    @staticmethod
    def odleglosc(p1, p2):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass


x, y = input().split()
a = Punkt(int(x), int(y))
x, y = input().split()
b = Punkt(int(x), int(y))

print(f"Punkt A: {a}")
print(f"Punkt B: {b}")
print(f"Odległość między punktami A i B: {Punkt.odleglosc(a, b):.2f}")
if a == b:
    print("Punkty są równe.")
else:
    print("Punkty są różne.")
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
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    x, y = input().split()
    a = Punkt(int(x), int(y))
    x, y = input().split()
    b = Punkt(int(x), int(y))

    print(f"Punkt A: {a}")
    print(f"Punkt B: {b}")
    print(f"Odległość między punktami A i B: {Punkt.odleglosc(a, b):.2f}")
    if a == b:
        print("Punkty są równe.")
    else:
        print("Punkty są różne.")
