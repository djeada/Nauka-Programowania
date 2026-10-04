r"""
ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. `Poniedziałek`
2. `Wtorek`
3. `Środa`
4. `Czwartek`
5. `Piątek`
6. `Sobota`
7. `Niedziela`

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` — liczba całkowita, $0 \le n \le 1000$

### Wyjście

Jedna linia: nazwa dnia (wielką literą, z polskimi znakami) lub komunikat o błędzie.

### Przykład 1

**Wejście:**

```
5
```

**Wyjście:**

```
Piątek
```

### Przykład 2

**Wejście:**

```
8
```

**Wyjście:**

```
Niepoprawny numer dnia tygodnia.
```

"""


def nazwa_dnia(n):
    if n == 1:
        return "Poniedziałek"
    elif n == 2:
        return "Wtorek"
    elif n == 3:
        return "Środa"
    elif n == 4:
        return "Czwartek"
    elif n == 5:
        return "Piątek"
    elif n == 6:
        return "Sobota"
    elif n == 7:
        return "Niedziela"
    else:
        return "Niepoprawny numer dnia tygodnia."


if __name__ == "__main__":
    n = int(input())
    print(nazwa_dnia(n))
