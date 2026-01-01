/*
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

*/

// Funkcja zwracajaca a podniesione do b
function podniesDoPotegi(a, b) {
  var wynik = 1;
  for (var i = 0; i < b; i++) {
    wynik *= a;
  }
  return wynik;
}

// Pobieranie danych od uzytkownika
const a = parseInt(prompt("Podaj podstawe:"));
const b = parseInt(prompt("Podaj wykladnik:"));

// Wypisanie wyniku
console.log(podniesDoPotegi(a, b));

