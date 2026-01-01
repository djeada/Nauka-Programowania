/*
ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz `1.00`.

*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let wynik = Math.PI;
for (let i = 1; i < liczba; i++) {
  wynik *= Math.PI;
}

// Wypisanie wyniku
console.log(wynik.toFixed(2));

