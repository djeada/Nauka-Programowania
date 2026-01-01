"""
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

"""

if __name__ == "__main__":

    print("Podaj numer miesiaca:")
    miesiac = int(input())

    if miesiac == 1:
        print("Styczen ma 31 dni.")
    elif miesiac == 2:
        print("Luty ma 28 lub 29 dni.")
    elif miesiac == 3:
        print("Marzec ma 31 dni.")
    elif miesiac == 4:
        print("Kwiecien ma 30 dni.")
    elif miesiac == 5:
        print("Maj ma 31 dni.")
    elif miesiac == 6:
        print("Czerwiec ma 30 dni.")
    elif miesiac == 7:
        print("Lipiec ma 31 dni.")
    elif miesiac == 8:
        print("Sierpien ma 31 dni.")
    elif miesiac == 9:
        print("Wrzesien ma 30 dni.")
    elif miesiac == 10:
        print("Pazdziernik ma 31 dni.")
    elif miesiac == 11:
        print("Listopad ma 30 dni.")
    elif miesiac == 12:
        print("Grudzien ma 31 dni.")
    else:
        print("Niepoprawny numer miesiaca.")
