/*
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

*/

function czyPierwsza(liczba) {
  if (liczba < 2) {
    return false;
  }
  for (var i = 2; i < liczba; i++) {
    if (liczba % i == 0) {
      return false;
    }
  }
  return true;
}

// Testy

function testCzyPierwsza() {
  console.assert(czyPierwsza(2) == true);
  console.assert(czyPierwsza(3) == true);
  console.assert(czyPierwsza(4) == false);
  console.assert(czyPierwsza(7) == true);
  console.assert(czyPierwsza(9) == false);
  console.assert(czyPierwsza(11) == true);
  console.assert(czyPierwsza(13) == true);
  console.assert(czyPierwsza(14) == false);
  console.assert(czyPierwsza(16) == false);
  console.assert(czyPierwsza(19) == true);
}

// Funkcja uruchamiajaca testy
function main() {
  testCzyPierwsza();
}

// Uruchomienie testow
main();

