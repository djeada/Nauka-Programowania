r"""
ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Niech `lo` będzie mniejszą, a `hi` większą z nich.

a) Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `lo < x < hi`.

b) Następnie wypisz w kolejności rosnącej te z nich, które są podzielne przez `3`.

### Wejście

* 1. linia: `a` — liczba naturalna
* 2. linia: `b` — liczba naturalna

### Wyjście

Najpierw liczby z podpunktu a), potem liczby z podpunktu b) — każda w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

Między `5` a `9` leżą liczby `6`, `7`, `8` (podpunkt a); spośród nich przez `3` dzieli się tylko `6` (podpunkt b).

### Uwagi

* Liczby `a` i `b` nie należą do przedziału (nierówności są ostre).
* Nie wypisuj nagłówków typu „a)” i „b)” ani pustej linii między podpunktami.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, ta część wyjścia jest pusta.

"""


def wypisz_przedzial(lo, hi):
    for x in range(lo + 1, hi):
        print(x)


def wypisz_podzielne_przez_3(lo, hi):
    for x in range(lo + 1, hi):
        if x % 3 == 0:
            print(x)


if __name__ == "__main__":
    a = int(input())
    b = int(input())

    lo = min(a, b)
    hi = max(a, b)

    wypisz_przedzial(lo, hi)
    wypisz_podzielne_przez_3(lo, hi)
