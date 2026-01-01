"""
ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:

* lewy dolny `(x1, y1)`
* prawy górny `(x2, y2)`
  Boki równoległe do osi.

Klasa ma mieć:

1. Konstruktor `(x1, y1, x2, y2)`
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
3. Metodę wypisującą informacje o prostokącie.

Program tworzy:

* A: (3, 4) i (9, 6)
* B: (2, 2) i (7, 5)

Wypisuje oba i pole części wspólnej.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 6
```

"""


class Prostokat:
    def __init__(self, lewo, gora, prawo, dol):
        self.lewo = lewo
        self.gora = gora
        self.prawo = prawo
        self.dol = dol

    def pole(self):
        return (self.prawo - self.lewo) * (self.dol - self.gora)

    @staticmethod
    def pole_czesci_wspolnej(p1, p2):
        if (
            p1.lewo > p2.prawo
            or p1.prawo < p2.lewo
            or p1.gora < p2.dol
            or p1.dol > p2.gora
        ):
            return 0

        pole_x = max(0, min(p1.prawo, p2.prawo) - max(p1.lewo, p2.lewo))
        pole_y = max(0, min(p1.gora, p2.gora) - max(p1.dol, p2.dol))

        return pole_x * pole_y


def test_pole_czesci_wspolnej_pozytwne():
    prostokat_a = Prostokat(2, 7, 5, 2)
    prostokat_b = Prostokat(3, 9, 6, 4)
    wynik = 6
    assert Prostokat.pole_czesci_wspolnej(prostokat_a, prostokat_b) == wynik


def test_pole_czesci_wspolnej_negatywne():
    prostokat_a = Prostokat(1, 1, -1, -1)
    prostokat_b = Prostokat(2, 2, 1, 1)
    wynik = 0
    assert Prostokat.pole_czesci_wspolnej(prostokat_b, prostokat_a) == wynik


if __name__ == "__main__":
    test_pole_czesci_wspolnej_pozytwne()
    test_pole_czesci_wspolnej_negatywne()
