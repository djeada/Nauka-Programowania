"""
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

"""

def czy_palindrom(slowo):
    """
    Sprawdza czy słowo jest palindromem (ignorując wielkość liter).
    
    Złożoność czasowa: O(n), gdzie n to długość słowa
    Złożoność pamięciowa: O(1)
    """
    slowo_male = slowo.lower()
    return slowo_male == slowo_male[::-1]


def wyczysc_slowo(slowo):
    """
    Usuwa interpunkcję z brzegów słowa.
    
    Złożoność czasowa: O(n), gdzie n to długość słowa
    Złożoność pamięciowa: O(n) dla wyniku
    """
    # Usunięcie niealfanumerycznych znaków z początku i końca
    poczatek = 0
    koniec = len(slowo) - 1
    
    while poczatek <= koniec and not slowo[poczatek].isalnum():
        poczatek += 1
    
    while koniec >= poczatek and not slowo[koniec].isalnum():
        koniec -= 1
    
    return slowo[poczatek:koniec + 1]


if __name__ == "__main__":
    # Wczytanie zdania z wejścia
    zdanie = input().strip()
    
    # Podział na słowa
    slowa = zdanie.split()
    
    # Złożoność całkowita: O(m * n), gdzie m to liczba słów, n to średnia długość słowa
    # Przetwarzanie każdego słowa
    for slowo in slowa:
        # Usunięcie interpunkcji z brzegów
        slowo_czyste = wyczysc_slowo(slowo)
        
        # Sprawdzenie czy czyste słowo jest palindromem i nie jest puste
        if slowo_czyste and czy_palindrom(slowo_czyste):
            print(slowo_czyste)
