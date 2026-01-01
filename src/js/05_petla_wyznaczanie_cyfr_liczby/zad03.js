/*
ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

### Uwagi o formatowaniu

* Dla `n = 0` suma cyfr wynosi `0`.

*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let suma = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  suma += i % 10;
}

// Wypisanie wyniku
console.log(suma);

