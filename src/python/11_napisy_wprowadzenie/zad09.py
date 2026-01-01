"""
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

"""


def rozdziel_informacje(napis):
    lista = napis.split(";")
    return lista


def wypisz_informacje(napis):
    informacje = rozdziel_informacje(napis)
    print("Imie: {}".format(informacje[0]))
    print("Nazwisko: {}".format(informacje[1]))
    print("Miejsce urodzenia: {}".format(informacje[2]))
    print("Stanowisko: {}".format(informacje[3]))
    print("Zarobki: {}".format(informacje[4]))


if __name__ == "__main__":

    informacje = "Jan;Kowalski;Warszawa;kierownik;2000"
    wypisz_informacje(informacje)
