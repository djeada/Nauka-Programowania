"""
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

"""


def czy_anagramy(slowo1, slowo2):
    """
    Sprawdza czy dwa słowa są anagramami.
    
    Złożoność czasowa: O(n log n), gdzie n to długość słowa (sortowanie)
    Złożoność pamięciowa: O(n) dla posortowanych kopii słów
    """
    # Ignorowanie wielkości liter
    slowo1_male = slowo1.lower()
    slowo2_male = slowo2.lower()
    
    # Anagramy muszą mieć tę samą długość
    if len(slowo1_male) != len(slowo2_male):
        return False
    
    # Porównanie posortowanych liter
    return sorted(slowo1_male) == sorted(slowo2_male)


if __name__ == "__main__":
    # Wczytanie dwóch słów z wejścia
    slowo1 = input().strip()
    slowo2 = input().strip()
    
    # Sprawdzenie czy słowa są anagramami
    if czy_anagramy(slowo1, slowo2):
        print("Prawda")
    else:
        print("Fałsz")
