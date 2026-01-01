"""
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def najdluzsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return max(slowa, key=len)


def najkrotsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return min(slowa, key=len)


def test_najdluzsze_slowo():
    assert najdluzsze_slowo("Ala ma kota.") == "kota"


def test_najkrotsze_slowo():
    assert najkrotsze_slowo("Ala ma kota.") == "ma"


if __name__ == "__main__":

    test_najdluzsze_slowo()
    test_najkrotsze_slowo()
