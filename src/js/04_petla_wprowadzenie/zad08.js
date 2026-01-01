/*
ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `układ równań`, `arytmetyka`

### Treść

Na farmie są kury i owce. Wiadomo, że:

* łączna liczba głów wynosi `a`,
* łączna liczba nóg wynosi `b`,
* kura ma 2 nogi, owca ma 4 nogi,
* każda ma dokładnie 1 głowę.

Oblicz liczbę kur oraz liczbę owiec.

### Wejście

Dwie liczby naturalne:

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Ograniczenia / gwarancje

* Istnieje rozwiązanie w liczbach całkowitych nieujemnych.

### Wyjście

Dwie liczby naturalne, każda w oddzielnej linii:

1. liczba kur
2. liczba owiec

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

### Uwagi o formatowaniu

* Nie wypisuj dodatkowych opisów — tylko liczby.

*/

// Pobieranie danych od uzytkownika
const a = parseInt(prompt("Podaj liczbe glow:"));
const b = parseInt(prompt("Podaj liczbe nog:"));

// Petla
for (let i = 0; i <= a; i++) {
  if (i * 2 + (a - i) * 4 === b) {
    console.log(i);
    console.log(a - i);
  }
}

