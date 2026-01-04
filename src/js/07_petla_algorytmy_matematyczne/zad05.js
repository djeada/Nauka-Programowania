/*
ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

**Wyjście:**

```
15
```

*/

function zwracajNWD(liczba_a, liczba_b) {
  var dzielnik = 1;
  for (var i = 1; i <= liczba_a; i++) {
    if (liczba_a % i == 0 && liczba_b % i == 0) {
      dzielnik = i;
    }
  }
  return dzielnik;
}

// Testy

function testNWD() {
  console.assert(zwracajNWD(2, 3) == 1);
  console.assert(zwracajNWD(3, 2) == 1);
  console.assert(zwracajNWD(4, 4) == 4);
  console.assert(zwracajNWD(5, 3) == 1);
  console.assert(zwracajNWD(6, 0) == 6);
  console.assert(zwracajNWD(7, 1) == 1);
  console.assert(zwracajNWD(0, 2) == 2);
}

// Funkcja uruchamiajaca testy
function main() {
  testNWD();
}

// Uruchomienie testow
main();

