r"""
ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj listę `n` liczb całkowitych. Wypisz największą, a po niej najmniejszą liczbę z listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna linia: największa i najmniejsza liczba, oddzielone spacją.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
9
4 -7 8 5 6 -9 10 2 -8
```

**Wyjście:**

```
10 -9
```

### Uwagi

* Spróbuj znaleźć obie wartości samodzielnie, w pętli, bez funkcji `max` i `min`.

"""


def znajdz_maks(lista):
    maks = lista[0]
    for element in lista:
        if element > maks:
            maks = element
    return maks


def znajdz_min(lista):
    minimum = lista[0]
    for element in lista:
        if element < minimum:
            minimum = element
    return minimum


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(znajdz_maks(lista), znajdz_min(lista))
