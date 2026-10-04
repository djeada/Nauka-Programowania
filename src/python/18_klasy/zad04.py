r"""
ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy `Wektor2D` (wektor na płaszczyźnie) i `Wektor3D` (wektor w przestrzeni).

Obie klasy mają mieć:

* konstruktor z domyślnymi współrzędnymi równymi 0: `Wektor2D(x=0, y=0)`, `Wektor3D(x=0, y=0, z=0)`,
* dodawanie i odejmowanie wektorów operatorami `+` i `-` (metody `__add__` i `__sub__`) — wynikiem jest nowy wektor tej samej klasy,
* metodę `iloczyn_skalarny(other)` — np. dla 3D: $x_A x_B + y_A y_B + z_A z_B$,
* metodę `dlugosc()` zwracającą długość (moduł) wektora — np. dla 3D: $\sqrt{x^2 + y^2 + z^2}$,
* porównanie `==` (metoda `__eq__`) — wektory są równe, gdy wszystkie współrzędne są równe,
* metodę `__str__()` zwracającą współrzędne w nawiasach, np. `(1, -2)` albo `(1, -2, 3)`.

Dodatkowo klasa `Wektor3D` ma metodę `iloczyn_wektorowy(other)`, która zwraca nowy obiekt `Wektor3D`:
$A \times B = (y_A z_B - z_A y_B,\ z_A x_B - x_A z_B,\ x_A y_B - y_A x_B)$.

Program wczytuje dwa wektory. Jeśli linia zawiera dwie liczby, tworzony jest `Wektor2D`, a jeśli trzy — `Wektor3D`. Następnie wypisuje wyniki działań.

### Wejście

* 1. linia: współrzędne wektora $A$ — dwie albo trzy liczby całkowite oddzielone spacjami
* 2. linia: współrzędne wektora $B$ — tyle samo liczb całkowitych co dla $A$

### Wyjście

Kolejne linie:

```
Wektor A: <A>
Wektor B: <B>
Suma wektorów: <A + B>
Różnica wektorów A - B: <A - B>
Iloczyn skalarny: <A · B>
Iloczyn wektorowy: <A × B>
Długość wektora A: <|A|>
Wektory są równe.
```

* Linię `Iloczyn wektorowy: …` wypisz **tylko** dla wektorów trójwymiarowych.
* Długość wypisz z dokładnością do 2 miejsc po przecinku.
* W ostatniej linii wypisz `Wektory są równe.` albo `Wektory są różne.`

### Ograniczenia

* Współrzędne są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
-3 -3 -3
5 5 5
```

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
Długość wektora A: 5.20
Wektory są różne.
```

### Przykład 2

**Wejście:**

```
3 4
1 -2
```

**Wyjście:**

```
Wektor A: (3, 4)
Wektor B: (1, -2)
Suma wektorów: (4, 2)
Różnica wektorów A - B: (2, 6)
Iloczyn skalarny: -5
Długość wektora A: 5.00
Wektory są różne.
```

### Kod startowy

```python
import math


class Wektor2D:
    def __init__(self, x=0, y=0):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def iloczyn_skalarny(self, other):
        pass

    def dlugosc(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass


class Wektor3D:
    def __init__(self, x=0, y=0, z=0):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def iloczyn_skalarny(self, other):
        pass

    def iloczyn_wektorowy(self, other):
        pass

    def dlugosc(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass


def wczytaj_wektor():
    liczby = [int(x) for x in input().split()]
    if len(liczby) == 2:
        return Wektor2D(liczby[0], liczby[1])
    return Wektor3D(liczby[0], liczby[1], liczby[2])


a = wczytaj_wektor()
b = wczytaj_wektor()

print(f"Wektor A: {a}")
print(f"Wektor B: {b}")
print(f"Suma wektorów: {a + b}")
print(f"Różnica wektorów A - B: {a - b}")
print(f"Iloczyn skalarny: {a.iloczyn_skalarny(b)}")
if isinstance(a, Wektor3D):
    print(f"Iloczyn wektorowy: {a.iloczyn_wektorowy(b)}")
print(f"Długość wektora A: {a.dlugosc():.2f}")
if a == b:
    print("Wektory są równe.")
else:
    print("Wektory są różne.")
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

    def iloczyn_skalarny(self, other):
        return self.x * other.x + self.y * other.y

    def dlugosc(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Wektor3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Wektor3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def iloczyn_skalarny(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def iloczyn_wektorowy(self, other):
        return Wektor3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def dlugosc(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


def wczytaj_wektor():
    liczby = [int(x) for x in input().split()]
    if len(liczby) == 2:
        return Wektor2D(liczby[0], liczby[1])
    return Wektor3D(liczby[0], liczby[1], liczby[2])


if __name__ == "__main__":
    a = wczytaj_wektor()
    b = wczytaj_wektor()

    print(f"Wektor A: {a}")
    print(f"Wektor B: {b}")
    print(f"Suma wektorów: {a + b}")
    print(f"Różnica wektorów A - B: {a - b}")
    print(f"Iloczyn skalarny: {a.iloczyn_skalarny(b)}")
    if isinstance(a, Wektor3D):
        print(f"Iloczyn wektorowy: {a.iloczyn_wektorowy(b)}")
    print(f"Długość wektora A: {a.dlugosc():.2f}")
    if a == b:
        print("Wektory są równe.")
    else:
        print("Wektory są różne.")
