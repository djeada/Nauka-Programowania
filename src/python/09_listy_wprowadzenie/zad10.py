"""
ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów `A(xA, yA)`, `B(xB, yB)`, `C(xC, yC)`.
Wypisz `Tak`, jeśli punkty **nie są współliniowe** (mogą tworzyć trójkąt), w przeciwnym razie `Nie`.

### Wejście

Sześć liczb całkowitych (każda w osobnej linii):

1. `xA`
2. `yA`
3. `xB`
4. `yB`
5. `xC`
6. `yC`

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
-3
-2
-3
1
-3
0
```

**Wyjście:**

```
Nie
```

### Uwagi

* Sprawdź pole trójkąta: jeśli równe `0`, punkty są współliniowe.

"""


def czy_trojkat(lista):
    xA, yA, xB, yB, xC, yC = lista

    a = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
    b = ((xC - xB) ** 2 + (yC - yB) ** 2) ** 0.5
    c = ((xA - xC) ** 2 + (yA - yC) ** 2) ** 0.5

    if a + b > c and a + c > b and b + c > a:
        return True

    return False


def test_czy_trojkat():
    assert not czy_trojkat([1, 1, 1, 1, 1, 1])
    assert not czy_trojkat([0, 0, 2, -2, 5, -5])
    assert czy_trojkat([-2, 4, 7, 5, 8, -8])


if __name__ == "__main__":

    test_czy_trojkat()
