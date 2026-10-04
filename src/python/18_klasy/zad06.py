r"""
ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasę `LiczbaZespolona` opisującą liczbę zespoloną $a + bi$:

* konstruktor `__init__(self, re=0, im=0)` — część rzeczywista i urojona,
* operatory `+`, `-`, `*`, `/` (metody `__add__`, `__sub__`, `__mul__`, `__truediv__`) zwracające nową liczbę zespoloną:
  * $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$,
  * $\frac{a + bi}{c + di} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i$ (dzielnik jest różny od zera),
* porównanie `==` (metoda `__eq__`) — liczby są równe, gdy mają równe części rzeczywiste i urojone,
* metodę `modul()` zwracającą moduł liczby: $|a + bi| = \sqrt{a^2 + b^2}$,
* metodę `__str__()` zwracającą napis `a + bi` albo `a - bi` (gdy część urojona jest ujemna, wypisz minus i jej wartość bezwzględną). Obie części wypisz z dokładnością do 2 miejsc po przecinku, np. `9.00 + 12.00i`, `-3.00 - 3.00i`.

Program wczytuje liczby $A$ i $B$ i wypisuje wyniki działań.

### Wejście

* 1. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $A$
* 2. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $B$

### Wyjście

Osiem linii:

```
Liczba A: <A>
Liczba B: <B>
Suma: <A + B>
Różnica A - B: <A - B>
Iloczyn: <A * B>
Iloraz A / B: <A / B>
Moduł liczby A: <|A|>
Liczby są równe.
```

* Jeśli $B = 0 + 0i$, zamiast ilorazu wypisz `Iloraz A / B: nie można dzielić przez zero`.
* Moduł wypisz z dokładnością do 2 miejsc po przecinku.
* W ostatniej linii wypisz `Liczby są równe.` albo `Liczby są różne.`

### Ograniczenia

* Części rzeczywiste i urojone są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
9 12
-3 -3
```

**Wyjście:**

```
Liczba A: 9.00 + 12.00i
Liczba B: -3.00 - 3.00i
Suma: 6.00 + 9.00i
Różnica A - B: 12.00 + 15.00i
Iloczyn: 9.00 - 63.00i
Iloraz A / B: -3.50 - 0.50i
Moduł liczby A: 15.00
Liczby są różne.
```

Iloczyn: $(9 + 12i)(-3 - 3i) = (-27 + 36) + (-27 - 36)i = 9 - 63i$.

### Kod startowy

```python
import math


class LiczbaZespolona:
    def __init__(self, re=0, im=0):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __eq__(self, other):
        pass

    def modul(self):
        pass

    def __str__(self):
        pass


re, im = input().split()
a = LiczbaZespolona(int(re), int(im))
re, im = input().split()
b = LiczbaZespolona(int(re), int(im))

print(f"Liczba A: {a}")
print(f"Liczba B: {b}")
print(f"Suma: {a + b}")
print(f"Różnica A - B: {a - b}")
print(f"Iloczyn: {a * b}")
if b == LiczbaZespolona(0, 0):
    print("Iloraz A / B: nie można dzielić przez zero")
else:
    print(f"Iloraz A / B: {a / b}")
print(f"Moduł liczby A: {a.modul():.2f}")
if a == b:
    print("Liczby są równe.")
else:
    print("Liczby są różne.")
```

"""

import math


class LiczbaZespolona:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return LiczbaZespolona(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return LiczbaZespolona(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return LiczbaZespolona(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __truediv__(self, other):
        mianownik = other.re**2 + other.im**2
        return LiczbaZespolona(
            (self.re * other.re + self.im * other.im) / mianownik,
            (self.im * other.re - self.re * other.im) / mianownik,
        )

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def modul(self):
        return math.sqrt(self.re**2 + self.im**2)

    def __str__(self):
        if self.im < 0:
            return f"{self.re:.2f} - {-self.im:.2f}i"
        return f"{self.re:.2f} + {self.im:.2f}i"


if __name__ == "__main__":
    re, im = input().split()
    a = LiczbaZespolona(int(re), int(im))
    re, im = input().split()
    b = LiczbaZespolona(int(re), int(im))

    print(f"Liczba A: {a}")
    print(f"Liczba B: {b}")
    print(f"Suma: {a + b}")
    print(f"Różnica A - B: {a - b}")
    print(f"Iloczyn: {a * b}")
    if b == LiczbaZespolona(0, 0):
        print("Iloraz A / B: nie można dzielić przez zero")
    else:
        print(f"Iloraz A / B: {a / b}")
    print(f"Moduł liczby A: {a.modul():.2f}")
    if a == b:
        print("Liczby są równe.")
    else:
        print("Liczby są różne.")
