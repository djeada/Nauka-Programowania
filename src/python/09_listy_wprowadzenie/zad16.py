r"""
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `listy`, `indeksy`, `pętle zagnieżdżone`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Znajdź indeksy `i`, `j` (gdzie $i < j$) takie, że `lista[i] + lista[j] == x`.

Jeśli takich par jest kilka, wybierz tę o najmniejszym `i`, a przy równym `i` — o najmniejszym `j`. Jeśli nie ma żadnej — wypisz `-1 -1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Jedna linia: dwie liczby `i j` oddzielone spacją albo `-1 -1`.

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
5
1 3 4 5 2
5
```

**Wyjście:**

```
0 2
```

Sumę $5$ dają pary indeksów $(0, 2)$: $1 + 4$ oraz $(1, 4)$: $3 + 2$. Pierwsza z nich ma mniejsze `i`.

### Uwagi

* Para składa się z dwóch **różnych** pozycji w liście — elementu nie można dodać do samego siebie.
* Wystarczą dwie zagnieżdżone pętle: zewnętrzna po `i`, wewnętrzna po `j` od `i + 1` do końca listy. Szybszy sposób, ze słownikiem, poznasz w rozdziale 17.

"""


def znajdz_pare(lista, x):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                return i, j
    return -1, -1


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    x = int(input())
    i, j = znajdz_pare(lista, x)
    print(i, j)
