r"""
ZAD-09 — Ocena z punktów

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `zakresy`

### Treść

Wczytaj liczbę punktów zdobytych na sprawdzianie i wypisz ocenę według progów:

* 0–49 punktów → `2`
* 50–69 punktów → `3`
* 70–84 punktów → `4`
* 85–100 punktów → `5`

Jeśli liczba punktów jest spoza zakresu 0–100, wypisz:
`Niepoprawna liczba punktów.`

### Wejście

* 1 linia: `punkty` — liczba całkowita, $-1000 \le punkty \le 1000$

### Wyjście

Jedna linia: ocena (`2`, `3`, `4` albo `5`) lub komunikat o błędzie.

### Przykład 1

**Wejście:**

```
77
```

**Wyjście:**

```
4
```

### Przykład 2

**Wejście:**

```
120
```

**Wyjście:**

```
Niepoprawna liczba punktów.
```

### Uwagi

* Najpierw obsłuż punkty spoza zakresu, a potem sprawdzaj progi po kolei w łańcuchu `if`/`elif` — każdy kolejny warunek może wtedy zakładać, że poprzednie nie zaszły.
* Python pozwala łączyć porównania: `50 <= punkty <= 69` znaczy to samo co `50 <= punkty and punkty <= 69`.

"""


def ocena(punkty):
    if punkty < 0 or punkty > 100:
        return "Niepoprawna liczba punktów."
    elif punkty < 50:
        return "2"
    elif punkty < 70:
        return "3"
    elif punkty < 85:
        return "4"
    else:
        return "5"


if __name__ == "__main__":
    punkty = int(input())
    print(ocena(punkty))
