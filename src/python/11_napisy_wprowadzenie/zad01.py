r"""
ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `napisy`, `wycinanie`

### Treść

Wczytaj napis i wypisz go od tyłu — znak po znaku, od ostatniego do pierwszego.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: odwrócony napis.

### Przykład 1

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

### Przykład 2

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
atok am alA
```

Odwracamy kolejność wszystkich znaków (także spacji), a nie tylko kolejność słów.

"""


def odwroc(napis):
    odwrocony = ""
    for znak in napis:
        odwrocony = znak + odwrocony
    return odwrocony


if __name__ == "__main__":
    napis = input()
    print(odwroc(napis))
