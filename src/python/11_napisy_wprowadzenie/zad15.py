"""
ZAD-15 — Słowa jako lista

**Poziom:** ★☆☆
**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: lista słów (jak w przykładzie)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
["Ala", "ma", "kota"]
```

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def test_podziel_zdanie_na_slowa():
    assert podziel_zdanie_na_slowa("Ala ma kota.") == ["Ala", "ma", "kota"]


if __name__ == "__main__":

    test_podziel_zdanie_na_slowa()
