/*
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca
cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

*/
#include <cassert>
#include <cmath>

bool pierwszaWieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba;
}

bool sumaMniejsza10(int pierwszaLiczba, int drugaLiczba) {
  int suma = pierwszaLiczba + drugaLiczba;
  return suma < 10;
}

bool obieNieparzyste(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba % 2 == 1 && drugaLiczba % 2 == 1;
}

int wieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

bool wiekszaMniejszaPierwszaKwadrat(int pierwszaLiczba, int drugaLiczba) {
  return wieksza(pierwszaLiczba, drugaLiczba) < pow(pierwszaLiczba, 2);
}

void testPierwszaWieksza() {
  assert(!pierwszaWieksza(1, 2));
  assert(pierwszaWieksza(2, 1));
}

void testSumaMniejsza10() {
  assert(!sumaMniejsza10(1, 2));
  assert(sumaMniejsza10(1, 9));
  assert(sumaMniejsza10(9, 1));
}

void testObieNieparzyste() {
  assert(!obieNieparzyste(1, 2));
  assert(obieNieparzyste(1, 1));
  assert(obieNieparzyste(2, 2));
}

void testWiekszaMniejszaPierwszaKwadrat() {
  assert(!wiekszaMniejszaPierwszaKwadrat(1, 2));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 1));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 2));
}

int main() {
  testPierwszaWieksza();
  testSumaMniejsza10();
  testObieNieparzyste();
  testWiekszaMniejszaPierwszaKwadrat();

  return 0;
}
