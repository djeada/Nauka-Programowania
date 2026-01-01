"""
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

"""


def czy_palindrom(liczba):
    """
    Funkcja sprawdza czy podana liczba jest palindromem.
    """

    odwrocona = 0

    k = liczba
    while k > 0:
        odwrocona = (odwrocona << 1) | (k & 1)
        k >>= 1

    return odwrocona == liczba


def test_czy_palindrom():

    assert czy_palindrom(0)
    assert czy_palindrom(27)
    assert not czy_palindrom(2)
    assert not czy_palindrom(77)


if __name__ == "__main__":

    test_czy_palindrom()
