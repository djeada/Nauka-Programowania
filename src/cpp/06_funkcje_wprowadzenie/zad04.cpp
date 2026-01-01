/*
ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb
naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_dwoch(3, 1))
```

**Wyjście:**

```
1
```

ZAD-04B — Maksimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb
naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_dwoch(3, 1))
```

**Wyjście:**

```
3
```

ZAD-04C — Minimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb
naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_trzech(3, 2, 1))
```

**Wyjście:**

```
1
```

ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb
naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_trzech(3, 2, 1))
```

**Wyjście:**

```
3
```

*/
#include <cassert>
#include <cmath>

int min2(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba < drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

int maks2(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

int min3(int pierwszaLiczba, int drugaLiczba, int trzeciaLiczba) {
  int minAB = pierwszaLiczba < drugaLiczba ? pierwszaLiczba : drugaLiczba;
  return minAB < trzeciaLiczba ? minAB : trzeciaLiczba;
}

int maks3(int pierwszaLiczba, int drugaLiczba, int trzeciaLiczba) {
  int maksAB = pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
  return maksAB > trzeciaLiczba ? maksAB : trzeciaLiczba;
}

void testMaks2() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int wynik = pierwszaLiczba;

  assert(maks2(pierwszaLiczba, drugaLiczba) == wynik);
  assert(maks2(drugaLiczba, pierwszaLiczba) == wynik);
}

void testMin2() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int wynik = drugaLiczba;

  assert(min2(pierwszaLiczba, drugaLiczba) == wynik);
  assert(min2(drugaLiczba, pierwszaLiczba) == wynik);
}

void testMaks3() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int trzeciaLiczba = 11;
  int wynik = trzeciaLiczba;

  assert(maks3(pierwszaLiczba, drugaLiczba, trzeciaLiczba) == wynik);
  assert(maks3(drugaLiczba, pierwszaLiczba, trzeciaLiczba) == wynik);
}

void testMin3() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int trzeciaLiczba = 11;
  int wynik = drugaLiczba;

  assert(min3(pierwszaLiczba, drugaLiczba, trzeciaLiczba) == wynik);
  assert(min3(drugaLiczba, pierwszaLiczba, trzeciaLiczba) == wynik);
}

int main() {
  testMaks2();
  testMin2();
  testMaks3();
  testMin3();

  return 0;
}
