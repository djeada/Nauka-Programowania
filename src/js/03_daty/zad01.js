/*
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

*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Porownanie ze stala
if (liczba >= 1 && liczba <= 12) {
  console.log(liczba);
}

