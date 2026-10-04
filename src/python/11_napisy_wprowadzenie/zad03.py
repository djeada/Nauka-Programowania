r"""
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `słowa`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Słowa wyznaczaj zgodnie z konwencją rozdziału: znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; słowa mogą być oddzielone kilkoma spacjami)

### Wyjście

Jedna linia: liczba słów.

### Przykład 1

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Przykład 2

**Wejście:**

```
Ala - jak co dzień - gra.
```

**Wyjście:**

```
5
```

Samotne myślniki nie są słowami, więc słowa to: `Ala`, `jak`, `co`, `dzień`, `gra`.

"""

import string


def podziel_na_slowa(zdanie):
    slowa = []
    for fragment in zdanie.split():
        slowo = fragment.strip(string.punctuation)
        if slowo:
            slowa.append(slowo)
    return slowa


def liczba_slow(zdanie):
    return len(podziel_na_slowa(zdanie))


if __name__ == "__main__":
    zdanie = input()
    print(liczba_slow(zdanie))
