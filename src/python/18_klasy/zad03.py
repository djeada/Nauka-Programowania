r"""
ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę `Prostokat` opisującą prostokąt o bokach równoległych do osi układu współrzędnych. Prostokąt jest wyznaczony przez dwa przeciwległe wierzchołki: lewy dolny $(x_1, y_1)$ i prawy górny $(x_2, y_2)$.

Klasa ma mieć:

1. Konstruktor `__init__(self, x1, y1, x2, y2)`.
2. Metodę `__str__()` zwracającą napis `lewy dolny (x1, y1), prawy górny (x2, y2)`.
3. Metodę statyczną `pole_wspolne(a, b)` zwracającą pole części wspólnej prostokątów `a` i `b`. Jeśli prostokąty nie nachodzą na siebie (albo stykają się tylko bokiem lub wierzchołkiem), pole części wspólnej wynosi `0`.

Program wczytuje dwa prostokąty $A$ i $B$, wypisuje je i podaje pole ich części wspólnej.

### Wejście

* 1. linia: cztery liczby całkowite $x_1$, $y_1$, $x_2$, $y_2$ — prostokąt $A$
* 2. linia: cztery liczby całkowite $x_1$, $y_1$, $x_2$, $y_2$ — prostokąt $B$

### Wyjście

Trzy linie:

```
Prostokąt A: lewy dolny (x1, y1), prawy górny (x2, y2)
Prostokąt B: lewy dolny (x1, y1), prawy górny (x2, y2)
Pole części wspólnej: <pole>
```

Pole jest liczbą całkowitą.

### Ograniczenia

* $-1000 \le x_1 < x_2 \le 1000$, $-1000 \le y_1 < y_2 \le 1000$

### Przykład

**Wejście:**

```
3 4 9 6
2 2 7 5
```

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 4
```

Częścią wspólną jest prostokąt o wierzchołkach $(3, 4)$ i $(7, 5)$, czyli o wymiarach $4 \times 1$.

### Uwagi

* Część wspólna (jeśli istnieje) też jest prostokątem. Jej lewa krawędź leży na $\max$ z lewych krawędzi obu prostokątów, a prawa na $\min$ z prawych krawędzi — analogicznie w pionie.

### Kod startowy

```python
class Prostokat:
    def __init__(self, x1, y1, x2, y2):
        pass

    def __str__(self):
        pass

    @staticmethod
    def pole_wspolne(a, b):
        pass


x1, y1, x2, y2 = [int(x) for x in input().split()]
a = Prostokat(x1, y1, x2, y2)
x1, y1, x2, y2 = [int(x) for x in input().split()]
b = Prostokat(x1, y1, x2, y2)

print(f"Prostokąt A: {a}")
print(f"Prostokąt B: {b}")
print(f"Pole części wspólnej: {Prostokat.pole_wspolne(a, b)}")
```

"""


class Prostokat:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return (
            f"lewy dolny ({self.x1}, {self.y1}), " f"prawy górny ({self.x2}, {self.y2})"
        )

    @staticmethod
    def pole_wspolne(a, b):
        szerokosc = min(a.x2, b.x2) - max(a.x1, b.x1)
        wysokosc = min(a.y2, b.y2) - max(a.y1, b.y1)
        if szerokosc <= 0 or wysokosc <= 0:
            return 0
        return szerokosc * wysokosc


if __name__ == "__main__":
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    a = Prostokat(x1, y1, x2, y2)
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    b = Prostokat(x1, y1, x2, y2)

    print(f"Prostokąt A: {a}")
    print(f"Prostokąt B: {b}")
    print(f"Pole części wspólnej: {Prostokat.pole_wspolne(a, b)}")
