r"""
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `napisy`, `pętle`, `konkatenacja`

### Treść

Wczytaj liczbę `n` i zbuduj napis złożony z kolejnych liczb od 1 do `n` zapisanych jedna za drugą, bez separatorów. Wypisz ten napis.

### Wejście

* 1. linia: liczba naturalna `n` ($n \ge 1$)

### Wyjście

Jedna linia: napis `123…n`.

### Przykład

**Wejście:**

```
11
```

**Wyjście:**

```
1234567891011
```

"""


def napis_z_liczb(n):
    napis = ""
    for liczba in range(1, n + 1):
        napis += str(liczba)
    return napis


if __name__ == "__main__":
    n = int(input())
    print(napis_z_liczb(n))
