/*
ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli `m <= 2`, to:

* `m = m + 12`
* `y = y - 1`

2. Oblicz:

* `K = y % 100`
* `J = y // 100`
* `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`

3. Zmapuj `h` na dzień tygodnia:

* 0 → `Sobota`
* 1 → `Niedziela`
* 2 → `Poniedziałek`
* 3 → `Wtorek`
* 4 → `Środa`
* 5 → `Czwartek`
* 6 → `Piątek`

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).

### Ograniczenia / gwarancje

* Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
* Kalendarz gregoriański.

### Przykład

**Wejście:**

```
9
10
2020
```

**Wyjście:**

```
Piątek
```

*/

// Pobieranie danych od uzytkownika
const dzien = parseInt(prompt("Podaj dzien:"));
const miesiac = parseInt(prompt("Podaj miesiac:"));
const rok = parseInt(prompt("Podaj rok:"));

const A = rok; // 4 - 2 * rok - 1
const B = 5 * rok; // 4
const C = 26 * (miesiac + 1); // 10

const dzien_tygodnia = (A + B + C + dzien) % 7;

if (dzien_tygodnia === 0) {
  console.log("Niedziela");
} else if (dzien_tygodnia === 1) {
  console.log("Poniedzialek");
} else if (dzien_tygodnia === 2) {
  console.log("Wtorek");
} else if (dzien_tygodnia === 3) {
  console.log("Sroda");
} else if (dzien_tygodnia === 4) {
  console.log("Czwartek");
} else if (dzien_tygodnia === 5) {
  console.log("Piatek");
} else {
  console.log("Sobota");
}

