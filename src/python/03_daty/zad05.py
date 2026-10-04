r"""
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu:

* 31 dni: styczeń (1), marzec (3), maj (5), lipiec (7), sierpień (8), październik (10), grudzień (12),
* 30 dni: kwiecień (4), czerwiec (6), wrzesień (9), listopad (11),
* 28 dni: luty (2).

Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` — liczba całkowita, $0 \le m \le 1000$

### Wyjście

Jedna linia: liczba dni **albo** komunikat o błędzie.

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


def dni_w_miesiacu(miesiac):
    if miesiac == 2:
        return "28"
    elif miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11:
        return "30"
    elif 1 <= miesiac <= 12:
        return "31"
    else:
        return "Niepoprawny numer miesiąca."


if __name__ == "__main__":
    miesiac = int(input())
    print(dni_w_miesiacu(miesiac))
