"""
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

"""


def najdluzszy_ciag_zer(liczba):
    """
    Funkcja zwraca dlugosc najdluzszego ciagu zer w dziesietnej
    reprezentacji liczby binarnej.
    """
    liczba_bin = bin(liczba)
    liczba_bin = liczba_bin[2:]
    liczba_bin = liczba_bin.split("1")
    liczba_bin.sort(key=len)
    return len(liczba_bin[-1])


def test_najdluzszy_ciag_zer():
    assert najdluzszy_ciag_zer(0) == 1
    assert najdluzszy_ciag_zer(111) == 1
    assert najdluzszy_ciag_zer(8219) == 8


if __name__ == "__main__":

    test_najdluzszy_ciag_zer()
