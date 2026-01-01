/*
ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

### Wejście

Jeden argument: `n` (`n ≥ 0`)

### Wyjście

Funkcja zwraca sumę cyfr.

### Przykład

**Wywołanie funkcji:**

```python
print(suma_cyfr(13231))
```

**Wyjście:**

```
10
```

### Uwagi

* Dla `n = 0` suma cyfr to `0`.

*/

// Funkcja zwracajaca sume cyfr liczby
function sumaCyfrLiczby(liczba) {
  var suma = 0;
  var liczbaTekst = liczba.toString();
  for (var i = 0; i < liczbaTekst.length; i++) {
    suma += parseInt(liczbaTekst[i]);
  }
  return suma;
}

// Pobieranie danych od uzytkownika i walidacja
var liczba = parseInt(prompt("Podaj liczbe:"));
while (isNaN(liczba)) {
  liczba = parseInt(prompt("Podaj poprawna liczbe:"));
}

// Wypisanie wyniku
console.log(sumaCyfrLiczby(liczba));

