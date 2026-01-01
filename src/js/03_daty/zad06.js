/*
ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite (w osobnych liniach):

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia / gwarancje

* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)

### Reguły walidacji

1. `m` musi być w zakresie 1–12
2. Ustal liczbę dni w miesiącu:

   * 31: 1,3,5,7,8,10,12
   * 30: 4,6,9,11
   * luty: 28 lub 29 (zależnie od przestępności roku)
3. `d` musi być w zakresie 1–dni_w_miesiącu

### Przykład

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

*/

// Pobieranie danych od uzytkownika
const dzien = parseInt(prompt("Podaj dzien:"));
const miesiac = parseInt(prompt("Podaj miesiac:"));
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy liczby sa poprawne
if (dzien > 0 && miesiac > 0 && rok > 0) {
  // Sprawdzenie, czy miesiac jest poprawny
  if (miesiac < 13) {
    // Sprawdzenie, czy rok jest przestepny
    if ((rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0) {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 30 ||
        (dzien === 30 && miesiac !== 2) ||
        (dzien === 29 && miesiac === 2)
      ) {
        console.log("Data jest poprawna");
      } else {
        console.log("Data jest niepoprawna");
      }
    } else {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 29 ||
        (dzien === 29 && miesiac !== 2) ||
        (dzien === 28 && miesiac === 2)
      ) {
        console.log("Data jest poprawna");
      } else {
        console.log("Data jest niepoprawna");
      }
    }
  } else {
    console.log("Data jest niepoprawna");
  }
} else {
  console.log("Data jest niepoprawna");
}

