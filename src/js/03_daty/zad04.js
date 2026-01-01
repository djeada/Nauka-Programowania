/*
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

*/

// Pobieranie danych od uzytkownika
const dzien_tygodnia = parseInt(prompt("Podaj dzien tygodnia:"));

// Sprawdzenie, czy liczba jest poprawna
if (dzien_tygodnia > 0 && dzien_tygodnia < 8) {
  // Sprawdzenie, ktory dzien tygodnia odpowiada liczbie
  if (dzien_tygodnia === 1) {
    console.log("Poniedzialek");
  } else if (dzien_tygodnia === 2) {
    console.log("Wtorek");
  } else if (dzien_tygodnia === 3) {
    console.log("Sroda");
  } else if (dzien_tygodnia === 4) {
    console.log("Czwartek");
  } else if (dzien_tygodnia === 5) {
    console.log("Piatek");
  } else if (dzien_tygodnia === 6) {
    console.log("Sobota");
  } else {
    console.log("Niedziela");
  }
} else {
  console.log("Liczba jest niepoprawna");
}

