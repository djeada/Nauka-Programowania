"""
ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

Jedna linia: nazwa dnia lub komunikat o błędzie.

### Przykład

**Wejście:**

```
8
```

**Wyjście:**

```
Niepoprawny numer dnia tygodnia.
```

"""

if __name__ == "__main__":

    print("Podaj liczbe:")
    liczba = int(input())

    if liczba < 0 or liczba > 7:
        print("Liczba niepoprawna")
    elif liczba == 1:
        print("Pierwszym dniem tygodnia jest poniedzialek.")
    elif liczba == 2:
        print("Drugim dniem tygodnia jest wtorek.")
    elif liczba == 3:
        print("Trzecim dniem tygodnia jest sroda.")
    elif liczba == 4:
        print("Czwartym dniem tygodnia jest czwartek.")
    elif liczba == 5:
        print("Piatym dniem tygodnia jest piatek.")
    elif liczba == 6:
        print("Szostym dniem tygodnia jest sobota.")
    elif liczba == 7:
        print("Siodmym dniem tygodnia jest niedziela.")
