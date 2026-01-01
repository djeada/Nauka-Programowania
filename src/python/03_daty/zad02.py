"""
ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiaj” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty aktualnej.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ≥ 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych (każda w osobnej linii):

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — aktualny dzień
5. `m2` — aktualny miesiąc
6. `y2` — aktualny rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia / gwarancje

* Obie daty są poprawne (nie musisz walidować).
* Pełnoletność jest osiągana **dokładnie w dniu 18. urodzin**.

### Uwagi (jak to porównać)

Osoba jest pełnoletnia wtedy, gdy data `y1+18, m1, d1` jest **nie późniejsza** niż data aktualna.

### Przykład

**Wejście:**

```
5
12
1999
20
11
2020
```

**Wyjście:**

```
Osoba jest pełnoletnia.
```

"""

if __name__ == "__main__":

    print("Podaj date urodzenia osoby (dzien, miesiac, rok):")
    dzien_urodzenia = int(input())
    miesiac_urodzenia = int(input())
    rok_urodzenia = int(input())

    print("Podaj aktualna date (dzien, miesiac, rok):")
    aktualny_dzien = int(input())
    aktualny_miesiac = int(input())
    aktualny_rok = int(input())

    roznica_lat = aktualny_rok - rok_urodzenia
    roznica_miesiecy = aktualny_miesiac - miesiac_urodzenia
    roznica_dni = aktualny_dzien - dzien_urodzenia

    if roznica_lat > 18:
        print("Osoba jest pelnoletnia.")

    elif roznica_lat == 18:

        if roznica_miesiecy > 0:
            print("Osoba jest pelnoletnia.")

        elif roznica_miesiecy == 0:

            if roznica_dni >= 0:
                print("Osoba jest pelnoletnia.")

            else:
                print("Osoba nie jest pelnoletnia.")
        else:
            print("Osoba nie jest pelnoletnia.")
    else:
        print("Osoba nie jest pelnoletnia.")
