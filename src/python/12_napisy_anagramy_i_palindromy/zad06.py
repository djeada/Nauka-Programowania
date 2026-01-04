"""
ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Uwagi

* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
* Generuj palindromy z połówek (bez wypisywania duplikatów).

"""

from collections import Counter


def generuj_palindromy(slowo):
    """
    Generuje wszystkie unikalne palindromy będące permutacjami słowa.

    Złożoność czasowa: O((n/2)! * n), gdzie n to długość słowa
    Złożoność pamięciowa: O((n/2)! * n) dla przechowania wyników
    """
    # Zliczenie wystąpień każdej litery
    licznik = Counter(slowo)

    # Sprawdzenie warunku istnienia palindromu
    # Co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień
    nieparzysty_znak = None
    liczba_nieparzystych = 0

    for znak, liczba in licznik.items():
        if liczba % 2 == 1:
            nieparzysty_znak = znak
            liczba_nieparzystych += 1

    # Jeśli więcej niż jeden znak ma nieparzystą liczbę wystąpień,
    # nie można utworzyć palindromu
    if liczba_nieparzystych > 1:
        return []

    # Utworzenie połówki palindromu (po połowie z każdego znaku)
    polowka_liter = []
    for znak, liczba in licznik.items():
        polowka_liter.extend([znak] * (liczba // 2))

    # Generowanie wszystkich unikalnych permutacji połówki
    wynik = set()

    def generuj_permutacje(elementy, obecna_permutacja):
        """Rekurencyjnie generuje wszystkie permutacje."""
        if not elementy:
            # Utworzenie palindromu z połówki
            polowka = "".join(obecna_permutacja)
            srodek = nieparzysty_znak if nieparzysty_znak else ""
            palindrom = polowka + srodek + polowka[::-1]
            wynik.add(palindrom)
            return

        # Użycie zbioru do uniknięcia duplikatów na tym poziomie
        uzyto = set()
        for i in range(len(elementy)):
            if elementy[i] not in uzyto:
                uzyto.add(elementy[i])
                generuj_permutacje(
                    elementy[:i] + elementy[i + 1 :], obecna_permutacja + [elementy[i]]
                )

    generuj_permutacje(polowka_liter, [])
    return sorted(wynik)


if __name__ == "__main__":
    # Wczytanie słowa z wejścia
    slowo = input().strip()

    # Wygenerowanie wszystkich unikalnych palindromów
    palindromy = generuj_palindromy(slowo)

    # Wypisanie każdego palindromu w osobnej linii
    for palindrom in palindromy:
        print(palindrom)
