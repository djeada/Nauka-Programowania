r"""
ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `słowa`

### Treść

Wczytaj zdanie, podziel je na słowa (zgodnie z konwencją rozdziału — bez interpunkcji) i wypisz każde słowo w osobnej linii.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

Słowa w kolejności występowania, każde w osobnej linii.

### Przykład

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
Ala
ma
kota
a
kot
ma
Alę
```

"""

import string


def podziel_na_slowa(zdanie):
    slowa = []
    for fragment in zdanie.split():
        slowo = fragment.strip(string.punctuation)
        if slowo:
            slowa.append(slowo)
    return slowa


if __name__ == "__main__":
    zdanie = input()
    for slowo in podziel_na_slowa(zdanie):
        print(slowo)
