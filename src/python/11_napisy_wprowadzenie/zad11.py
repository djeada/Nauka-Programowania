r"""
ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość jego słów (zgodnie z konwencją rozdziału — interpunkcja nie wlicza się do długości słowa).
Wynikiem jest **część całkowita** średniej, czyli `suma_długości // liczba_słów`.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

Jedna linia: część całkowita średniej długości słów.

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

Słowa `Zepsuty` i `rower` mają razem $7 + 5 = 12$ liter, a `12 // 2` to `6`.

"""

import string


def podziel_na_slowa(zdanie):
    slowa = []
    for fragment in zdanie.split():
        slowo = fragment.strip(string.punctuation)
        if slowo:
            slowa.append(slowo)
    return slowa


def srednia_dlugosc_slow(zdanie):
    slowa = podziel_na_slowa(zdanie)
    suma_dlugosci = 0
    for slowo in slowa:
        suma_dlugosci += len(slowo)
    return suma_dlugosci // len(slowa)


if __name__ == "__main__":
    zdanie = input()
    print(srednia_dlugosc_slow(zdanie))
