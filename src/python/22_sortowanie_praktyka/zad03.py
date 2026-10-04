r"""
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Wczytaj listę par `(napis, liczba)` i zapisz je jako krotki.

a) Posortuj pary rosnąco według liczby.
b) Posortuj pary rosnąco według długości napisu.

Przy remisie (ta sama liczba w a), ta sama długość napisu w b)) pary zachowują kolejność z wejścia.

### Wejście

* 1. linia: liczba par $N$
* kolejne $N$ linii: napis (bez spacji) i liczba całkowita, oddzielone spacją

### Wyjście

* 1. linia: lista par posortowana według podpunktu a)
* 2. linia: lista par posortowana według podpunktu b)

Listy wypisz w formacie Pythona — tak, jak robi to `print(lista)` dla listy krotek, np. `[('bca', 1), ('c', 2), ('ab', 3)]`.

### Ograniczenia

* $1 \le N \le 20$

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

### Uwagi

* Kryterium sortowania podaj w parametrze `key`, np. `sorted(pary, key=lambda para: para[1])`.

"""


def sortuj_wedlug_liczby(pary):
    return sorted(pary, key=lambda para: para[1])


def sortuj_wedlug_dlugosci_napisu(pary):
    return sorted(pary, key=lambda para: len(para[0]))


if __name__ == "__main__":
    n = int(input())
    pary = []
    for _ in range(n):
        napis, liczba = input().split()
        pary.append((napis, int(liczba)))

    print(sortuj_wedlug_liczby(pary))
    print(sortuj_wedlug_dlugosci_napisu(pary))
