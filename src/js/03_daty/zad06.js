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

// Sprawdzenie, czy miesiac jest poprawny
if (miesiac < 1 || miesiac > 12) {
  console.log("Data jest niepoprawna.");
} else {
  // Ustalenie liczby dni w miesiącu
  let dni_w_miesiacu;
  if (miesiac === 2) {
    // Luty - sprawdzamy czy rok przestepny
    const przestepny = (rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0;
    dni_w_miesiacu = przestepny ? 29 : 28;
  } else if ([4, 6, 9, 11].includes(miesiac)) {
    dni_w_miesiacu = 30;
  } else {
    dni_w_miesiacu = 31;
  }
  
  // Sprawdzenie, czy dzien jest poprawny
  if (dzien >= 1 && dzien <= dni_w_miesiacu) {
    console.log("Data jest poprawna.");
  } else {
    console.log("Data jest niepoprawna.");
  }
}

