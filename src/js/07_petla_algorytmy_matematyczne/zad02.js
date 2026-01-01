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

// Testy

function testPotega() {
  console.assert(podniesDoPotegi(2, 3) == 8);
  console.assert(podniesDoPotegi(3, 2) == 9);
  console.assert(podniesDoPotegi(4, 4) == 256);
  console.assert(podniesDoPotegi(5, 3) == 125);
  console.assert(podniesDoPotegi(6, 0) == 1);
  console.assert(podniesDoPotegi(7, 1) == 7);
  console.assert(podniesDoPotegi(0, 2) == 0);
}

// Funkcja uruchamiajaca testy
function main() {
  testPotega();
}

// Uruchomienie testow
main();

