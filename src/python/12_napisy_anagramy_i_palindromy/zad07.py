"""
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

"""

from collections import Counter


def minimalne_usuniecia(slowo1, slowo2):
    """
    Oblicza minimalną liczbę znaków do usunięcia, aby słowa były anagramami.
    
    Złożoność czasowa: O(n + m), gdzie n i m to długości słów
    Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
    """
    # Jeśli słowa mają różne długości, zwróć -1
    if len(slowo1) != len(slowo2):
        return -1
    
    # Zliczenie wystąpień znaków w obu słowach
    licznik1 = Counter(slowo1)
    licznik2 = Counter(slowo2)
    
    # Suma różnic w liczbie wystąpień każdej litery
    suma_roznic = 0
    
    # Zbieramy wszystkie unikalne znaki z obu słów
    wszystkie_znaki = set(licznik1.keys()) | set(licznik2.keys())
    
    for znak in wszystkie_znaki:
        # Obliczenie różnicy wystąpień danego znaku
        roznica = abs(licznik1.get(znak, 0) - licznik2.get(znak, 0))
        suma_roznic += roznica
    
    return suma_roznic


if __name__ == "__main__":
    # Wczytanie dwóch słów z wejścia
    slowo1 = input().strip()
    slowo2 = input().strip()
    
    # Obliczenie minimalnej liczby usunięć
    wynik = minimalne_usuniecia(slowo1, slowo2)
    
    print(wynik)
