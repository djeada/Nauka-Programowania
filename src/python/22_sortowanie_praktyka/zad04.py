r"""
ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Wczytaj listę napisów i posortuj ją rosnąco według długości napisów. Napisy o tej samej długości zachowują kolejność z wejścia.

### Wejście

* 1. linia: liczba napisów $N$
* kolejne $N$ linii: napis (bez spacji)

### Wyjście

* 1. linia: posortowane napisy oddzielone pojedynczymi spacjami

### Ograniczenia

* $1 \le N \le 50$

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
a ab abc abcd
```

### Uwagi

* Wystarczy `sorted(napisy, key=len)`.

"""


def sortuj_wedlug_dlugosci(napisy):
    return sorted(napisy, key=len)


if __name__ == "__main__":
    n = int(input())
    napisy = [input() for _ in range(n)]
    print(" ".join(sortuj_wedlug_dlugosci(napisy)))
