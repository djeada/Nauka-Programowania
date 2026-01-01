"""
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

"""


def wielkie_na_male(slowo):
    """
    Funkcja zamienia wielkie litery na male litery.
    """
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) | ord(" "))

    return wynik


def male_na_wielkie(slowo):
    """
    Funkcja zamienia male litery na wielkie litery.
    """
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) & ord("_"))

    return wynik


def odwroc_wielkosc_liter(slowo):
    """
    Funkcja zamienia male litery na wielkie litery i wielkie litery na male litery.
    """
    wynik = ""

    for litera in slowo:
        if litera >= "a" and litera <= "z":
            wynik += chr(ord(litera) ^ ord(" "))

        elif litera >= "A" and litera <= "Z":
            wynik += chr(ord(litera) ^ ord(" "))

        else:
            wynik += litera

    return wynik


def test_wielkie_na_male():
    assert wielkie_na_male("KURCZAKU") == "kurczaku"


def test_male_na_wielkie():
    assert male_na_wielkie("piesek") == "PIESEK"


def test_odwroc_wielkosc_liter():
    assert (
        odwroc_wielkosc_liter("wszedl Kotek na PloteK i mrUga")
        == "WSZEDL kOTEK NA pLOTEk I MRuGA"
    )


if __name__ == "__main__":

    test_wielkie_na_male()
    test_male_na_wielkie()
    test_odwroc_wielkosc_liter()
