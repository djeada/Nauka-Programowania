r"""
ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy liczb całkowitych. Jeśli mają tę samą długość, utwórz macierz o dwóch kolumnach, w której wiersz `i` to `lista1[i] lista2[i]`, i wypisz ją.
Jeśli długości list są różne, wypisz `Pusta macierz`.

### Wejście

* 1. linia: `n` — długość pierwszej listy
* 2. linia: `m` — długość drugiej listy
* następnie `n` linii, w każdej jedna liczba całkowita (pierwsza lista)
* następnie `m` linii, w każdej jedna liczba całkowita (druga lista)

### Wyjście

* Jeśli `n = m`: `n` linii postaci `x y`, gdzie `x` pochodzi z pierwszej listy, a `y` z drugiej.
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`.

### Ograniczenia

* `1 ≤ n, m ≤ 100`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

"""


def polacz_listy_w_macierz(lista_a, lista_b):
    """
    Zwraca macierz o dwóch kolumnach: w i-tym wierszu są lista_a[i] i lista_b[i].
    Dla list różnej długości zwraca pustą macierz.
    """
    if len(lista_a) != len(lista_b):
        return []
    macierz = []
    for i in range(len(lista_a)):
        macierz.append([lista_a[i], lista_b[i]])
    return macierz


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    lista_a = [int(input()) for _ in range(n)]
    lista_b = [int(input()) for _ in range(m)]

    macierz = polacz_listy_w_macierz(lista_a, lista_b)
    if not macierz:
        print("Pusta macierz")
    else:
        for wiersz in macierz:
            print(" ".join(str(x) for x in wiersz))
