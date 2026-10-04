r"""
ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `pętle`, `układ równań`, `arytmetyka`

### Treść

Na farmie są wyłącznie kury i owce. Każde zwierzę ma jedną głowę, kura ma 2 nogi, a owca 4 nogi.
Znając łączną liczbę głów `a` i łączną liczbę nóg `b`, oblicz, ile jest kur, a ile owiec.

### Wejście

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Wyjście

Dwie liczby całkowite, każda w osobnej linii:

1. liczba kur,
2. liczba owiec.

### Ograniczenia

* Dane są poprawne: istnieje dokładnie jedno rozwiązanie w liczbach całkowitych nieujemnych.

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

30 kur ma 60 nóg, a 10 owiec ma 40 nóg — razem 40 głów i 100 nóg.

### Uwagi

* Możesz sprawdzać w pętli kolejne możliwe liczby kur (od `0` do `a`) i szukać tej, dla której zgadza się liczba nóg.

"""


def kury_i_owce(glowy, nogi):
    """Zwraca parę (kury, owce) pasującą do podanej liczby głów i nóg."""
    for kury in range(glowy + 1):
        owce = glowy - kury
        if 2 * kury + 4 * owce == nogi:
            return kury, owce
    return None


if __name__ == "__main__":
    glowy = int(input())
    nogi = int(input())

    kury, owce = kury_i_owce(glowy, nogi)
    print(kury)
    print(owce)
