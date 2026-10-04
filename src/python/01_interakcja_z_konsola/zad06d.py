r"""
ZAD-06D — Euro → złotówki (kurs stały)

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj kwotę w euro `eur` i przelicz ją na złotówki przy stałym kursie 4,40 zł za 1 euro: $pln = eur \cdot 4.4$.

### Wejście

* 1 linia: `eur` — liczba rzeczywista, $eur \ge 0$

### Wyjście

Jedna linia: `pln` do **2 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
13.20
```

"""

KURS_EURO = 4.4


def euro_na_zlotowki(euro):
    return euro * KURS_EURO


if __name__ == "__main__":
    euro = float(input())
    print(f"{euro_na_zlotowki(euro):.2f}")
