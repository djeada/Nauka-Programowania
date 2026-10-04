r"""
ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj liczby `a` i `b`. Utwórz macierz złożoną z `a` identycznych wierszy, w których są kolejne liczby od `0` do `b` włącznie, i wypisz ją.

### Wejście

* 1. linia: `a` — liczba wierszy
* 2. linia: `b` — ostatnia liczba w wierszu

### Wyjście

`a` linii, w każdej liczby `0 1 2 … b` oddzielone spacjami.

### Ograniczenia

* `1 ≤ a ≤ 20`
* `0 ≤ b ≤ 20`

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
    """Zwraca macierz złożoną z a wierszy, z których każdy to liczby 0, 1, ..., b."""
    macierz = []
    for _ in range(a):
        wiersz = []
        for j in range(b + 1):
            wiersz.append(j)
        macierz.append(wiersz)
    return macierz


def wypisz_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(str(x) for x in wiersz))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    wypisz_macierz(stworz_macierz(a, b))
