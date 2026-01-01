"""
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

### Uwagi

* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

"""


def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def znaki_na_pozycjach_pierwszych(napis):
    znaki = []
    for i, znak in enumerate(napis):
        if czy_pierwsza(i):
            znaki.append(znak)
    return znaki


def test_znaki_na_pozycjach_pierwszych():
    assert znaki_na_pozycjach_pierwszych("abcd") == ["c", "d"]
    assert znaki_na_pozycjach_pierwszych("Kaczka lubi wiosne.") == [
        "c",
        "z",
        "a",
        "l",
        " ",
        "i",
        "e",
    ]


if __name__ == "__main__":

    test_znaki_na_pozycjach_pierwszych()
