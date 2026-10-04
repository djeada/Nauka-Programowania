r"""
ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę całkowitą `n` i sprawdź, czy może być numerem dnia tygodnia (1–7) i czy może być numerem miesiąca (1–12). Wypisz:

* `Liczba jest numerem dnia tygodnia i numerem miesiąca.` — gdy $1 \le n \le 7$,
* `Liczba jest tylko numerem miesiąca.` — gdy $8 \le n \le 12$,
* `Liczba nie jest numerem dnia tygodnia ani miesiąca.` — w pozostałych przypadkach.

### Wejście

* 1 linia: `n` — liczba całkowita, $-1000 \le n \le 1000$

### Wyjście

Jedna linia — dokładnie jeden z trzech komunikatów.

### Przykład 1

**Wejście:**

```
5
```

**Wyjście:**

```
Liczba jest numerem dnia tygodnia i numerem miesiąca.
```

### Przykład 2

**Wejście:**

```
15
```

**Wyjście:**

```
Liczba nie jest numerem dnia tygodnia ani miesiąca.
```

"""


def opis_numeru(n):
    if 1 <= n <= 7:
        return "Liczba jest numerem dnia tygodnia i numerem miesiąca."
    elif 8 <= n <= 12:
        return "Liczba jest tylko numerem miesiąca."
    else:
        return "Liczba nie jest numerem dnia tygodnia ani miesiąca."


if __name__ == "__main__":
    n = int(input())
    print(opis_numeru(n))
