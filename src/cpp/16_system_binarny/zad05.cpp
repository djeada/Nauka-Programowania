/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia
instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.

ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i
bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

*/
#include <cassert>

int znak(int n) {
  /*
   * Funkcja zwraca znak liczby n.
   */
  return (n >> 31) & 0x01;
}

int maks(int a, int b) {
  /*
   * Funkcja zwraca maksimum dwoch liczb.
   * dla a >= b: znak_a = 1, znak_b = 0;
   * dla a < b: znak_a = 0, znak_b = 1;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakA * a + znakB * b;
}

int min(int a, int b) {
  /*
   * Funkcja zwraca minimum dwoch liczb.
   * dla a >= b: znak_a = 0, znak_b = 1;
   * dla a < b: znak_a = 1, znak_b = 0;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakB * a + znakA * b;
}

void testMaks() {
  int a = 10;
  int b = 8;
  int wynik = a;

  assert(maks(a, b) == wynik);
}

void testMin() {
  int a = 10;
  int b = 8;
  int wynik = b;

  assert(min(a, b) == wynik);
}

int main() {
  testMaks();
  testMin();

  return 0;
}
