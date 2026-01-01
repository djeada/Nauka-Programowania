"""
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

"""

if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    maks_ab = a if a > b else b

    maks_cd = c if c > d else d

    maks = maks_ab if maks_ab > maks_cd else maks_cd

    print(maks)
