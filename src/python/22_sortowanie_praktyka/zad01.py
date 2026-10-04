r"""
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Wczytaj napis, posortuj rosnąco wszystkie jego znaki i wypisz napis złożony z posortowanych znaków.

### Wejście

* 1. linia: napis $s$ (co najmniej jeden znak)

### Wyjście

* 1. linia: znaki napisu $s$ posortowane rosnąco według kodów Unicode, sklejone w jeden napis

### Ograniczenia

* $1 \le |s| \le 100$

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
  Aaaaklmot
```

### Uwagi

* Spacje też są znakami i biorą udział w sortowaniu. Spacja ma mniejszy kod niż litery i cyfry, dlatego w przykładzie wynik zaczyna się od **dwóch** spacji (napis `Ala ma kota` zawiera dwie spacje).
* `sorted(napis)` zwraca listę znaków — połącz ją w napis metodą `"".join(…)`.

"""


def sortuj_znaki(napis):
    return "".join(sorted(napis))


if __name__ == "__main__":
    napis = input()
    print(sortuj_znaki(napis))
