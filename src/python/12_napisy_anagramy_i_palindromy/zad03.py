r"""
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `anagram`, `sortowanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami, czyli czy jedno da się utworzyć przez przestawienie liter drugiego (każda litera musi wystąpić w obu słowach tyle samo razy).
Wielkość liter nie ma znaczenia. Słowo jest też anagramem samego siebie.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowa są anagramami,
* `Fałsz` — w przeciwnym razie.

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

* Najprościej porównać posortowane litery obu słów (np. `sorted(s1.lower())`) albo liczbę wystąpień każdej litery.

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
