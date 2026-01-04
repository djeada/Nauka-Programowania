/*
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

*/

function silnia(liczba) {
  var wynik = 1;
  for (var i = 1; i <= liczba; i++) {
    wynik *= i;
  }
  return wynik;
}

// Testy

function testSilnia() {
  console.assert(silnia(2) == 2);
  console.assert(silnia(3) == 6);
  console.assert(silnia(4) == 24);
  console.assert(silnia(5) == 120);
  console.assert(silnia(6) == 720);
  console.assert(silnia(7) == 5040);
  console.assert(silnia(8) == 40320);
}

// Funkcja uruchamiajaca testy
function main() {
  testSilnia();
}

// Uruchomienie testow
main();

