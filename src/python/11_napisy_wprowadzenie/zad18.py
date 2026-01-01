"""
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def odwroc(napis):
    return napis[::-1]


def odwroc_slowa(zdanie):

    wynik = " ".join([odwroc(slowo) for slowo in podziel_zdanie_na_slowa(zdanie)])

    for i, znak in enumerate(zdanie):
        if znak in string.punctuation:
            wynik = wynik[:i] + znak + wynik[i:]

    return wynik


def test_odwroc_slowa():
    assert odwroc_slowa("Ala ma kota.") == "alA am atok."


if __name__ == "__main__":

    test_odwroc_slowa()
