"""
ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `split`, `string`

### Treść

Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.

### Wejście

* 1. linia: zdanie

### Wyjście

* wiele linii: słowa w kolejności występowania

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Ala
ma
kota
```

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def wypisz_pionowo(zdanie):
    for slowo in podziel_zdanie_na_slowa(zdanie):
        print(slowo)


if __name__ == "__main__":
    zdanie = "Ala ma kota, a kot ma Ale."
    wypisz_pionowo(zdanie)
