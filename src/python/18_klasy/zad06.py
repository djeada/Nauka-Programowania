"""
ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operacje`, `math`

### Treść

Zaprojektuj klasę **LiczbaZespolona**:

* konstruktor `(re=0, im=0)`,
* dodawanie, odejmowanie, mnożenie, dzielenie,
* porównania,
* moduł,
* wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).

Program tworzy:

* A = 9 + 12i
* B = -3 - 3i

Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Liczba A: 9 + 12i
Liczba B: -3 - 3i

Suma: 6 + 9i
Różnica A - B: 12 + 15i
Iloczyn: 27 + 63i
Iloraz A / B: -3.5 + 0.5i
```

"""

import math


class Zespolona:
    def __init__(self, rzeczywista=0, urojona=0):
        self.rzeczywista = rzeczywista
        self.urojona = urojona

    def __add__(self, other):
        return Zespolona(
            self.rzeczywista + other.rzeczywista, self.urojona + other.urojona
        )

    def __sub__(self, other):
        return Zespolona(
            self.rzeczywista - other.rzeczywista, self.urojona - other.urojona
        )

    def __mul__(self, other):
        return Zespolona(
            self.rzeczywista * other.rzeczywista - self.urojona * other.urojona,
            self.rzeczywista * other.urojona + self.urojona * other.rzeczywista,
        )

    def __truediv__(self, other):
        return Zespolona(
            (self.rzeczywista * other.rzeczywista + self.urojona * other.urojona)
            / (other.rzeczywista**2 + other.urojona**2),
            (self.urojona * other.rzeczywista - self.rzeczywista * other.urojona)
            / (other.rzeczywista**2 + other.urojona**2),
        )

    def __str__(self):
        return f"{self.rzeczywista:.2f} + {self.urojona:.2f}i"

    def __eq__(self, other):
        return self.rzeczywista == other.rzeczywista and self.urojona == other.urojona

    def __ne__(self, other):
        return self.rzeczywista != other.rzeczywista or self.urojona != other.urojona

    def modul(self):
        return math.sqrt(self.rzeczywista**2 + self.urojona**2)


if __name__ == "__main__":

    zespolona_a = Zespolona(9, 12)
    zespolona_b = Zespolona(-3, -3)

    print(f"Liczba zespolona A: {zespolona_a}")
    print(f"Liczba zespolona B: {zespolona_b}")
    print(f"Suma liczb zespolonych A i B: {zespolona_a + zespolona_b}")
    print(f"Roznica liczb zespolonych A i B: {zespolona_a - zespolona_b}")
    print(f"Iloczyn liczb zespolonych A i B: {zespolona_a * zespolona_b}")
    print(f"Iloraz liczb zespolonych A i B: {zespolona_a / zespolona_b}")
    print(f"Modul liczby zespolonej A: {zespolona_a.modul()}")
    print(f"A == B: {zespolona_a == zespolona_b}")
    print(f"A != B: {zespolona_a != zespolona_b}")
