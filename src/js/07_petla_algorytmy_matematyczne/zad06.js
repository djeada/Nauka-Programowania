/*
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

*/

// Funkcja zwracajaca NWW
function zwracajNWW(liczba_a, liczba_b) {
  var nww = 1;
  var i = 1;
  while (nww == 1) {
    if (i % liczba_a == 0 && i % liczba_b == 0) {
      nww = i;
    }
    i++;
  }
  return nww;
}

// Testy

function testNWW() {
  console.assert(zwracajNWW(2, 3) == 6);
  console.assert(zwracajNWW(3, 2) == 6);
  console.assert(zwracajNWW(4, 4) == 4);
  console.assert(zwracajNWW(5, 3) == 15);
  console.assert(zwracajNWW(6, 0) == 0);
  console.assert(zwracajNWW(7, 1) == 7);
  console.assert(zwracajNWW(0, 2) == 0);
}

// Funkcja uruchamiajaca testy
function main() {
  testNWW();
}

// Uruchomienie testow
main();

