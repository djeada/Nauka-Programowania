r"""
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `palindrom`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem, czyli czy czytane od lewej do prawej i od prawej do lewej jest takie samo.
Wielkość liter nie ma znaczenia — `Kajak` też jest palindromem.

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem,
* `Fałsz` — w przeciwnym razie.

### Przykład 1

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
Kotek
```

**Wyjście:**

```
Fałsz
```

"""


def czy_palindrom(slowo):
    """
    Sprawdza czy słowo jest palindromem.

    Złożoność czasowa: O(n), gdzie n to długość słowa
    Złożoność pamięciowa: O(n) - tworzenie odwróconej wersji słowa
    """
    # Konwersja na małe litery dla porównania bez uwzględniania wielkości liter
    slowo_male = slowo.lower()

    # Porównanie słowa z jego odwróconą wersją
    return slowo_male == slowo_male[::-1]


if __name__ == "__main__":
    # Wczytanie słowa z wejścia
    slowo = input().strip()

    # Sprawdzenie czy słowo jest palindromem
    if czy_palindrom(slowo):
        print("Prawda")
    else:
        print("Fałsz")
