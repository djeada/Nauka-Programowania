r"""
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `split`, `pętle`

### Treść

Wczytaj zdanie i odwróć kolejność liter **w każdym słowie osobno**, zachowując kolejność słów w zdaniu.
Znaki interpunkcyjne na początku i na końcu słowa zostają na swoim miejscu (np. `kota,` → `atok,`).

### Wejście

* 1. linia: zdanie, w którym słowa są oddzielone pojedynczymi spacjami

### Wyjście

Jedna linia: zdanie z odwróconymi słowami (słowa oddzielone pojedynczymi spacjami).

### Przykład 1

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

### Przykład 2

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
alA am atok, a tok am ęlA.
```

"""

import string


def odwroc_slowo(fragment):
    poczatek = 0
    while poczatek < len(fragment) and fragment[poczatek] in string.punctuation:
        poczatek += 1
    koniec = len(fragment)
    while koniec > poczatek and fragment[koniec - 1] in string.punctuation:
        koniec -= 1
    return fragment[:poczatek] + fragment[poczatek:koniec][::-1] + fragment[koniec:]


def odwroc_slowa(zdanie):
    odwrocone = []
    for fragment in zdanie.split():
        odwrocone.append(odwroc_slowo(fragment))
    return " ".join(odwrocone)


if __name__ == "__main__":
    zdanie = input()
    print(odwroc_slowa(zdanie))
