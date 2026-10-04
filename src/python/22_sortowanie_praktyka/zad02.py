r"""
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Wczytaj zdanie i podziel je na słowa. Słowa oddzielają od siebie spacje oraz znaki interpunkcyjne: `.` `,` `!` `?` `;` `:` — te znaki nie należą do słów. Posortuj słowa rosnąco (według kodów Unicode, bez zmiany wielkości liter) i wypisz je.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

* 1. linia: posortowane słowa oddzielone pojedynczymi spacjami

Jeśli słowo występuje w zdaniu kilka razy, wypisz je tyle samo razy.

### Ograniczenia

* Zdanie ma co najwyżej 200 znaków.

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
Lemur ciało wygina śmiało
```

### Przykład 2

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
Ala Alę a kot kota ma ma
```

Wielkie litery są przed małymi, a `Ala` jest przed `Alę`, bo `'a' < 'ę'`.

### Uwagi

* Najprościej zamienić każdy znak interpunkcyjny na spację (`napis.replace(".", " ")` itd.), a potem użyć `split()`.

"""

SEPARATORY = ".,!?;:"


def podziel_na_slowa(zdanie):
    for znak in SEPARATORY:
        zdanie = zdanie.replace(znak, " ")
    return zdanie.split()


def sortuj_slowa(zdanie):
    return sorted(podziel_na_slowa(zdanie))


if __name__ == "__main__":
    zdanie = input()
    print(" ".join(sortuj_slowa(zdanie)))
