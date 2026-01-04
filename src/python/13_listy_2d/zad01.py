"""
ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

* `a` wierszy, w każdym: `0 1 2 ... b`

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

"""


def stworz_macierz(a, b):
    """
    Funkcja tworzy macierz o wymiarach a x (b+1).
    Kazdy wiersz sklada sie z liczb od 0 do b włącznie.

    Złożoność czasowa: O(a * b)
    Złożoność pamięciowa: O(a * b)
    """
    macierz = []
    for i in range(a):
        macierz.append([])
        for j in range(b + 1):
            macierz[i].append(j)
    return macierz


def test_stworz_macierz():
    assert stworz_macierz(2, 3) == [[0, 1, 2], [0, 1, 2]]
    assert stworz_macierz(3, 2) == [[0, 1], [0, 1], [0, 1]]


if __name__ == "__main__":
    # Wczytanie wartości a i b z wejścia
    a = int(input().strip())
    b = int(input().strip())

    # Utworzenie macierzy
    # Złożoność czasowa: O(a * b), gdzie a to liczba wierszy, b to liczba elementów w wierszu
    # Złożoność pamięciowa: O(a * b) dla przechowania macierzy
    macierz = stworz_macierz(a, b)

    # Wypisanie macierzy
    for wiersz in macierz:
        print(" ".join(map(str, wiersz)))
