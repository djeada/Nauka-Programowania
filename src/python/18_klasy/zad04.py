"""
ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

* konstruktor z domyślnymi współrzędnymi 0,
* dodawanie, odejmowanie,
* iloczyn skalarny,
* porównania `==` i `!=`,
* moduł (długość),
* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

* iloczyn wektorowy.

Program tworzy:

* A = (-3, -3, -3)
* B = (5, 5, 5)

Wypisuje A, B oraz:

* A + B
* A - B
* A · B
* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

"""

import math


class Wektor2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Wektor2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Wektor2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int) or isinstance(other, float):
            return Wektor2D(self.x * other, self.y * other)
        else:
            raise TypeError

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def modul(self):
        return math.sqrt(self.x**2 + self.y**2)


class Wektor3D(Wektor2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Wektor3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Wektor3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Wektor3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def modul(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def iloczyn_wektorowy(a, b):
        return Wektor3D(
            a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x
        )


if __name__ == "__main__":
    wektor_a = Wektor3D(-3, -3, -3)
    wektor_b = Wektor3D(5, 5, 5)

    print(f"Wektor A: {wektor_a}")
    print(f"Wektor B: {wektor_b}")
    print(f"Suma wektorow: {wektor_a + wektor_b}")
    print(f"Roznica wektorow: {wektor_a - wektor_b}")
    print(f"Iloczyn skalarny: {wektor_a * wektor_b}")
    print(f"Iloczyn wektorowy: {Wektor3D.iloczyn_wektorowy(wektor_a, wektor_b)}")
    print(f"Iloczyn skalarny wektora A: {wektor_a} i liczby 5: {wektor_a * 5}")
    print(f"Iloczyn skalarny wektora B: {wektor_b} i liczby 2: {wektor_b * 2}")
