/*
ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — liczba cyfr w `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Ograniczenia / gwarancje

* `n` mieści się w typowym zakresie liczb całkowitych.

### Uwagi o formatowaniu

* Dla `n = 0` poprawna odpowiedź to `1` (liczba „0” ma jedną cyfrę).

*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let cyfry = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  cyfry++;
}

// Wypisanie wyniku
console.log(cyfry);

