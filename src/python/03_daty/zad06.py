r"""
ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d`, `m`, `y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Data jest poprawna, gdy:

1. miesiąc `m` jest w zakresie 1–12,
2. dzień `d` jest w zakresie od 1 do liczby dni w miesiącu `m`:
   * 31 dni: miesiące 1, 3, 5, 7, 8, 10, 12,
   * 30 dni: miesiące 4, 6, 9, 11,
   * luty (2): 29 dni w roku przestępnym, 28 w nieprzestępnym (zob. konwencje rozdziału).

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite, każda w osobnej linii:

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia

* $-100 \le d, m \le 100$ (dzień i miesiąc mogą być spoza poprawnego zakresu, także zerowe lub ujemne)
* $1 \le y \le 9999$ (rok zawsze jest poprawny)

### Przykład 1

**Wejście:**

```
31
4
2021
```

**Wyjście:**

```
Data jest niepoprawna.
```

Kwiecień ma tylko 30 dni.

### Przykład 2

**Wejście:**

```
29
2
2024
```

**Wyjście:**

```
Data jest poprawna.
```

Rok 2024 jest przestępny, więc luty ma 29 dni.

"""


def czy_przestepny(rok):
    return rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0)


def dni_w_miesiacu(miesiac, rok):
    if miesiac == 2:
        if czy_przestepny(rok):
            return 29
        return 28
    elif miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11:
        return 30
    else:
        return 31


def czy_poprawna_data(dzien, miesiac, rok):
    if miesiac < 1 or miesiac > 12:
        return False
    return 1 <= dzien <= dni_w_miesiacu(miesiac, rok)


if __name__ == "__main__":
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())

    if czy_poprawna_data(dzien, miesiac, rok):
        print("Data jest poprawna.")
    else:
        print("Data jest niepoprawna.")
