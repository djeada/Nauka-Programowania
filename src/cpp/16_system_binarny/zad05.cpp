/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia
instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji
`min`, `max`, `abs`, `sorted`.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna
wartość).

### Ograniczenia

* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

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
* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w
zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)`
jest równe `d` albo `0`.
* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia
instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji
`abs`, `min`, `max`, `sorted`.

### Wejście

* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

**Wejście:**

```
-12
```

**Wyjście:**

```
12
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są
potrzebne.
* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same
jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity,
czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch).
Wystarczy więc obliczyć `(x ^ m) - m`.

*/
#include <cassert>

int znak(int n) {
  /*
   * Funkcja zwraca znak liczby n.
   */
  return (n >> 31) & 0x01;
}

long long wartoscBezwzgledna(long long x) {
  /*
   * ZAD-05B: wartosc bezwzgledna bez instrukcji warunkowych.
   * maska = x >> 63 to -1 dla x < 0 i 0 dla x >= 0,
   * wiec (x ^ maska) - maska to x albo -x.
   */
  long long maska = x >> 63;
  return (x ^ maska) - maska;
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

void testWartoscBezwzgledna() {
  assert(wartoscBezwzgledna(-12) == 12);
  assert(wartoscBezwzgledna(7) == 7);
  assert(wartoscBezwzgledna(0) == 0);
  assert(wartoscBezwzgledna(-1000000000) == 1000000000);
}

void testMin() {
  int a = 10;
  int b = 8;
  int wynik = b;

  assert(min(a, b) == wynik);
}

int main() {
  testWartoscBezwzgledna();
  testMin();

  return 0;
}
