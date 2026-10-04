r"""
ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m`. **Klepsydra** to 7 pól wyciętych z dowolnego kwadratu `3×3` macierzy: cały górny wiersz, środkowe pole i cały dolny wiersz.

```
a b c
  d
e f g
```

Suma klepsydry to $a + b + c + d + e + f + g$. Wypisz największą sumę spośród wszystkich klepsydr w macierzy.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych (mogą być ujemne)

### Wyjście

Jedna liczba całkowita: największa suma klepsydry.

### Ograniczenia

* `3 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

Największą sumę ma klepsydra ze środkiem w polu o wartości `7`: $8 + 10 + 8 + 7 + 9 + 19 + 14 = 75$.

### Uwagi

* Gdy wszystkie liczby są ujemne, wynik też jest ujemny — nie zaczynaj szukania maksimum od `0`.

"""


def suma_klepsydry(macierz, wiersz, kolumna):
    """Zwraca sumę klepsydry, której lewy górny róg leży w polu [wiersz][kolumna]."""
    gora = (
        macierz[wiersz][kolumna]
        + macierz[wiersz][kolumna + 1]
        + macierz[wiersz][kolumna + 2]
    )
    srodek = macierz[wiersz + 1][kolumna + 1]
    dol = (
        macierz[wiersz + 2][kolumna]
        + macierz[wiersz + 2][kolumna + 1]
        + macierz[wiersz + 2][kolumna + 2]
    )
    return gora + srodek + dol


def najwieksza_klepsydra(macierz):
    """Zwraca największą sumę klepsydry w macierzy (co najmniej 3×3)."""
    n = len(macierz)
    m = len(macierz[0])
    najwieksza = suma_klepsydry(macierz, 0, 0)
    for wiersz in range(n - 2):
        for kolumna in range(m - 2):
            suma = suma_klepsydry(macierz, wiersz, kolumna)
            if suma > najwieksza:
                najwieksza = suma
    return najwieksza


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    macierz = [[int(x) for x in input().split()] for _ in range(n)]

    print(najwieksza_klepsydra(macierz))
