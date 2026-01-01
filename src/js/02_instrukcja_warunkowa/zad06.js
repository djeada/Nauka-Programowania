/*
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));
const liczba_c = parseInt(prompt("Podaj trzecia liczbe:"));
const liczba_d = parseInt(prompt("Podaj czwarta liczbe:"));

// Znalezienie maksimum przy pomocy instrukcji warunkowej
const maks_ab = liczba_a > liczba_b ? liczba_a : liczba_b;
const maks_cd = liczba_c > liczba_d ? liczba_c : liczba_d;
const maks = maks_ab > maks_cd ? maks_ab : maks_cd;

// Wypisanie wyniku
console.log(maks);

