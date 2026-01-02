"""
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

"""

def czy_anagramy(slowo1, slowo2):
    """
    Sprawdza czy dwa słowa są anagramami (ignorując wielkość liter).
    
    Złożoność czasowa: O(n log n), gdzie n to długość słowa
    Złożoność pamięciowa: O(n) dla posortowanych kopii
    """
    slowo1_male = slowo1.lower()
    slowo2_male = slowo2.lower()
    
    return sorted(slowo1_male) == sorted(slowo2_male)


def wyczysc_slowo(slowo):
    """
    Usuwa interpunkcję z brzegów słowa.
    
    Złożoność czasowa: O(n), gdzie n to długość słowa
    Złożoność pamięciowa: O(n) dla wyniku
    """
    poczatek = 0
    koniec = len(slowo) - 1
    
    while poczatek <= koniec and not slowo[poczatek].isalnum():
        poczatek += 1
    
    while koniec >= poczatek and not slowo[koniec].isalnum():
        koniec -= 1
    
    return slowo[poczatek:koniec + 1]


if __name__ == "__main__":
    # Wczytanie zdania i słowa-klucza z wejścia
    zdanie = input().strip()
    klucz = input().strip()
    
    # Podział zdania na słowa
    slowa = zdanie.split()
    
    # Złożoność całkowita: O(m * n log n), gdzie m to liczba słów, n to średnia długość słowa
    # Przetwarzanie każdego słowa
    for slowo in slowa:
        # Usunięcie interpunkcji z brzegów
        slowo_czyste = wyczysc_slowo(slowo)
        
        # Sprawdzenie czy słowo jest anagramem klucza
        if slowo_czyste and czy_anagramy(slowo_czyste, klucz):
            print(slowo_czyste)
