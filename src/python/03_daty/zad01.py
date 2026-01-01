"""
ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz `n` **tylko wtedy**, gdy jest poprawnym numerem:

* dnia tygodnia (1–7) **lub**
* miesiąca (1–12).

W praktyce oznacza to: wypisz `n` tylko wtedy, gdy `1 ≤ n ≤ 12`.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `1 ≤ n ≤ 12`: wypisz `n` w osobnej linii
* W przeciwnym razie: brak wyjścia

### Przykłady

**Wejście:**

```
5
```

**Wyjście:**

```
5
```

**Wejście:**

```
15
```

**Wyjście:** *(brak)*

"""

if __name__ == "__main__":

    print("Podaj liczbe:")

    a = int(input())
    b = int(input())

    if a >= 1 and a <= 7:
        print("Liczba jest poprawnym numerem tygodnia.")
    else:
        print("Liczba nie jest poprawnym numerem tygodnia.")

    if b >= 1 and b <= 12:
        print("Liczba jest poprawnym numerem miesiaca.")
    else:
        print("Liczba nie jest poprawnym numerem miesiaca.")
