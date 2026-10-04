r"""
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `napisy`, `zliczanie`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.
Wielkość liter ma znaczenie: `A` i `a` to różne znaki.

### Wejście

* 1. linia: napis (może zawierać spacje)
* 2. linia: jeden znak (różny od spacji)

### Wyjście

Jedna linia: liczba wystąpień znaku (może być `0`).

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

"""


def liczba_wystapien(napis, szukany):
    licznik = 0
    for znak in napis:
        if znak == szukany:
            licznik += 1
    return licznik


if __name__ == "__main__":
    napis = input()
    szukany = input()
    print(liczba_wystapien(napis, szukany))
