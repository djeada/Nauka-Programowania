/*
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let palindrom = true;
for (let i = liczba, j = 0; i > 0; i = Math.floor(i / 10), j++) {
  if (Math.floor(liczba / 10 ** j) % 10 !== i % 10) {
    palindrom = false;
    break;
  }
}

// Wypisanie wyniku
if (palindrom) {
  console.log("Liczba jest palindromem.");
} else {
  console.log("Liczba nie jest palindromem.");
}

