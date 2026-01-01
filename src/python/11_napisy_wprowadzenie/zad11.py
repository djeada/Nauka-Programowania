"""
ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

### Uwagi

* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def srednia_dlugosc_slow(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    wynik = sum(len(slowo) for slowo in slowa) / len(slowa)
    return int(wynik)


def test_srednia_dlugosc_slow():
    assert srednia_dlugosc_slow("Kaczka lubi wiosne.") == 5
    assert srednia_dlugosc_slow("Ile to   ma :  slow w swoim zdaniu na   koniec?") == 3


if __name__ == "__main__":
    test_srednia_dlugosc_slow()
