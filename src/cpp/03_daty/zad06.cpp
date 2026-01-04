/*
ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu
gregoriańskim.

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

* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w
całym zbiorze)

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
#include <iostream>

int main() {
  int dzien, miesiac, rok;
  std::cin >> dzien >> miesiac >> rok;

  bool poprawna = false;

  if (miesiac < 1 || miesiac > 12) {
    poprawna = false;
  } else {
    int max_dni = 31;
    if (miesiac == 4 || miesiac == 6 || miesiac == 9 || miesiac == 11) {
      max_dni = 30;
    } else if (miesiac == 2) {
      if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0) {
        max_dni = 29;
      } else {
        max_dni = 28;
      }
    }
    if (dzien >= 1 && dzien <= max_dni) {
      poprawna = true;
    }
  }

  if (poprawna)
    std::cout << "Data jest poprawna." << std::endl;
  else
    std::cout << "Data jest niepoprawna." << std::endl;

  return 0;
}
