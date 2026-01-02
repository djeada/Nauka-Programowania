"""
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

"""


def czy_palindrom(slowo):
    """
    Sprawdza czy słowo jest palindromem.
    
    Złożoność czasowa: O(n), gdzie n to długość słowa
    Złożoność pamięciowa: O(1) - porównanie bez tworzenia nowych struktur
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
