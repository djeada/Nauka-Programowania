/*
ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest
**większa lub równa** `n`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsze `2^k ≥ n`.

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* Dla `n = 0` przyjmij wynik `1`.

*/
#include <cassert>

int nastepnaPotegaDwojkiV1(int liczba) {
  /*
   * Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
   * Zasada dzialania opiera sie na zmniejszaniu liczby, az liczba bedzie
   * podzielna przez 2.
   */
  if (liczba <= 0) return 0;

  if (liczba == 1) return 2;

  liczba--;

  while (liczba & (liczba - 1)) liczba &= liczba - 1;

  return liczba << 1;
}

int nastepnaPotegaDwojkiV2(int liczba) {
  /*
   * Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
   * Zasada dzialania opiera sie na obliczeniu nastepnych poteg dwojki,
   * az otrzymamy liczbe wieksza lub rowna podanej liczbie.
   */
  if (liczba <= 0) return 0;

  int potega = 2;

  while (liczba > 2) {
    liczba >>= 1;
    potega <<= 1;
  }

  return potega;
}

void testNastepnaPotegaDwojkiV1() {
  assert(nastepnaPotegaDwojkiV1(111) == 128);
  assert(nastepnaPotegaDwojkiV1(-30) == 0);
  assert(nastepnaPotegaDwojkiV1(1) == 2);
}

void testNastepnaPotegaDwojkiV2() {
  assert(nastepnaPotegaDwojkiV2(111) == 128);
  assert(nastepnaPotegaDwojkiV2(-30) == 0);
  assert(nastepnaPotegaDwojkiV2(1) == 2);
}

int main() {
  testNastepnaPotegaDwojkiV1();
  testNastepnaPotegaDwojkiV2();

  return 0;
}
