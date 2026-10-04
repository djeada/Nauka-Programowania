r"""
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `min/max`

### Treść

Wczytaj zdanie i znajdź w nim (zgodnie z konwencją rozdziału — bez interpunkcji):

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli kilka słów ma tę samą długość, wybierz to, które występuje w zdaniu **wcześniej**.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

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

Słowa `Kaczka` i `wiosnę` mają po 6 liter — wygrywa wcześniejsze `Kaczka`.

"""

import string


def podziel_na_slowa(zdanie):
    slowa = []
    for fragment in zdanie.split():
        slowo = fragment.strip(string.punctuation)
        if slowo:
            slowa.append(slowo)
    return slowa


def najdluzsze_slowo(slowa):
    najdluzsze = slowa[0]
    for slowo in slowa:
        if len(slowo) > len(najdluzsze):
            najdluzsze = slowo
    return najdluzsze


def najkrotsze_slowo(slowa):
    najkrotsze = slowa[0]
    for slowo in slowa:
        if len(slowo) < len(najkrotsze):
            najkrotsze = slowo
    return najkrotsze


if __name__ == "__main__":
    slowa = podziel_na_slowa(input())
    print(najdluzsze_slowo(slowa))
    print(najkrotsze_slowo(slowa))
