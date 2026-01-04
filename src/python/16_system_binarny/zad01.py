"""
ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

Jedna linia: zapis binarny `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi o formacie

* Dla `n = 0` wypisz `0`.

ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` (ciąg znaków `0` i `1`)

### Wyjście

Jedna linia: liczba w systemie dziesiętnym.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

"""


def na_dziesietny(liczba):
    """
    Funkcja zamienia liczbe binarna na dziesietna.

    Złożoność czasowa: O(n), gdzie n to liczba cyfr
    Złożoność pamięciowa: O(1)
    """
    wynik = 0
    for pozycja, cyfra in enumerate(liczba[::-1]):
        wynik += (2 ** int(pozycja)) * int(cyfra)

    return wynik


def na_binarny(liczba):
    """
    Funkcja zamienia liczbe dziesietna na binarna.

    Złożoność czasowa: O(log n), gdzie n to wartość liczby
    Złożoność pamięciowa: O(log n) dla przechowania wyniku
    """
    if liczba == 0:
        return "0"

    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba = liczba // 2

    return wynik


def test_na_dziesietny():
    assert na_dziesietny("101") == 5
    assert na_dziesietny("1101") == 13
    assert na_dziesietny("1111") == 15


def test_na_binarny():
    assert na_binarny(5) == "101"
    assert na_binarny(13) == "1101"
    assert na_binarny(15) == "1111"


if __name__ == "__main__":
    # Wczytanie wejścia
    wejscie = input().strip()

    # Złożoność czasowa: O(n) lub O(log n) w zależności od konwersji
    # Złożoność pamięciowa: O(log n) dla wyniku

    # Strategia rozpoznawania: jeśli input zawiera tylko 0 i 1 oraz ma więcej niż jedną cyfrę
    # lub zaczyna się od '1' i zawiera tylko 0/1, traktuj jako binarny.
    # W przeciwnym razie traktuj jako dziesiętny.
    if wejscie == "0":
        # Przypadek specjalny: 0 jest taki sam w obu systemach
        print("0")
    elif all(c in "01" for c in wejscie) and (
        len(wejscie) > 2 or (len(wejscie) == 2 and wejscie[0] == "1")
    ):
        # Input wygląda jak liczba binarna (tylko 0 i 1, długość > 2 lub "1X")
        # Konwersja binarna → dziesiętna (ZAD-01B)
        wynik = na_dziesietny(wejscie)
        print(wynik)
    else:
        # Input jest liczbą dziesiętną
        # Konwersja dziesiętna → binarna (ZAD-01A)
        liczba = int(wejscie)
        wynik = na_binarny(liczba)
        print(wynik)
