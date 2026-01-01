"""
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

"""

import math


def na_dziesietny(liczba, stara_podstawa):
    """
    Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na reprezentacje w systemie dziesietnym.
    """
    reprezentacja_dziesietna = 0

    for i in range(len(liczba) - 1, -1, -1):

        if liczba[i] >= "A" and liczba[i] < "Z":
            reprezentacja_dziesietna += (ord(liczba[i]) - ord("A") + 10) * math.pow(
                stara_podstawa, (len(liczba) - 1 - i)
            )
        else:
            reprezentacja_dziesietna += (ord(liczba[i]) - ord("0")) * math.pow(
                stara_podstawa, (len(liczba) - 1 - i)
            )

    return int(reprezentacja_dziesietna)


def zmien_podstawe(liczba, stara_podstawa, nowa_podstawa):
    """
    Funkcja zamienia liczbe z reprezentacji w systemie stara_podstaw na
    reprezentacje w systemie nowa_podstawa.
    """

    if stara_podstawa > (10 + ord("Z") - ord("A")):
        raise ValueError("Stara podstawa jest za duza")

    reprezentacja_dziesietna = na_dziesietny(liczba, stara_podstawa)
    liczba = ""
    podstawa = nowa_podstawa

    while reprezentacja_dziesietna > 0:
        reszta = reprezentacja_dziesietna % podstawa
        reprezentacja_dziesietna //= podstawa

        nowy_znak = chr(ord("0") + reszta)

        if nowy_znak > "9":
            nowy_znak = "A" + (nowy_znak - "9") - 1

        liczba += nowy_znak

    return liczba[::-1]


def test_zmien_podstawe():
    assert zmien_podstawe("101", 2, 10) == "5"
    assert zmien_podstawe("101", 2, 16) == "5"
    assert zmien_podstawe("101", 10, 2) == "1100101"
    assert zmien_podstawe("101", 10, 16) == "65"
    assert zmien_podstawe("4301", 10, 4) == "1003031"


if __name__ == "__main__":
    test_zmien_podstawe()
