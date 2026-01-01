"""
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def liczba_slow_w_zdaniu(zdanie):
    return len(podziel_zdanie_na_slowa(zdanie))


def test_liczba_slow_w_zdaniu():
    assert liczba_slow_w_zdaniu("Ala ma kota.") == 3
    assert liczba_slow_w_zdaniu("Ala ma kota, a kot ma Ale.") == 7


if __name__ == "__main__":
    test_liczba_slow_w_zdaniu()
