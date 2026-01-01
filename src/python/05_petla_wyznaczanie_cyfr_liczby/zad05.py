"""
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    liczba_pomocnicza = liczba
    odwrocona = 0

    while liczba_pomocnicza > 0:
        odwrocona = odwrocona * 10 + liczba_pomocnicza % 10
        liczba_pomocnicza //= 10

    if liczba == odwrocona:
        print("Liczba jest palindromem.")
    else:
        print("Liczba nie jest palindromem.")
