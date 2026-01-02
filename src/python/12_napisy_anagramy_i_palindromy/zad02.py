"""
ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `permutacje`, `backtracking`

### Treść

Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.

### Wejście

* 1. linia: słowo (litery nie powtarzają się)

### Wyjście

Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.

### Przykład

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Uwagi o formatowaniu

* Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.

"""


def generuj_permutacje(slowo):
    """
    Generuje wszystkie permutacje słowa metodą rekurencyjną.
    
    Złożoność czasowa: O(n! * n), gdzie n to długość słowa
    Złożoność pamięciowa: O(n! * n) dla przechowania wszystkich permutacji
    """
    # Przypadek bazowy - słowo puste lub jednoelementowe
    if len(slowo) <= 1:
        return [slowo]
    
    # Lista do przechowywania wyników
    wynik = []
    
    # Dla każdej litery w słowie
    for i in range(len(slowo)):
        # Wybranie bieżącej litery
        obecna = slowo[i]
        # Pozostałe litery (bez obecnej)
        pozostale = slowo[:i] + slowo[i+1:]
        
        # Rekurencyjne generowanie permutacji dla pozostałych liter
        for permutacja in generuj_permutacje(pozostale):
            # Dodanie obecnej litery na początku każdej permutacji
            wynik.append(obecna + permutacja)
    
    return wynik


if __name__ == "__main__":
    # Wczytanie słowa z wejścia
    slowo = input().strip()
    
    # Wygenerowanie wszystkich permutacji
    permutacje = generuj_permutacje(slowo)
    
    # Wypisanie każdej permutacji w osobnej linii
    for permutacja in permutacje:
        print(permutacja)
