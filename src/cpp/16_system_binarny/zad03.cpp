/*
ZAD-03A — Dodawanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie
operatorów bitowych (i przesunięć).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a + b`.

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
5
```

ZAD-03B — Odejmowanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj `a` i `b`. Oblicz `a - b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a - b`.

### Ograniczenia / gwarancje

* Zakładamy, że `a ≥ b` (wynik jest naturalny).

### Przykład

**Wejście:**

```
7
5
```

**Wyjście:**

```
2
```

ZAD-03C — Mnożenie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np.
metoda „shift-and-add”).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a * b`.

### Przykład

**Wejście:**

```
4
4
```

**Wyjście:**

```
16
```

ZAD-03D — Dzielenie całkowite bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj `a` i `b`. Oblicz `a // b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Jedna liczba naturalna: `a // b`.

### Przykład

**Wejście:**

```
9
3
```

**Wyjście:**

```
3
```

*/
#include <cassert>
#include <functional>

int suma(int a, int b) {
  /*
   * Funkcja dodaje dwie liczby naturalne.
   */

  while (b != 0) {
    int pom = a & b;
    a = a ^ b;
    b = pom << 1;
  }

  return a;
}

int roznica(int a, int b) {
  /*
   * Funkcja odejmuje dwie liczby naturalne.
   */

  while (b != 0) {
    int pom = (~a) & b;
    a = a ^ b;
    b = pom << 1;
  }

  return a;
}

int iloczyn(int a, int b) {
  /*
   * Funkcja mnozy dwie liczby naturalne.
   */

  int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

  if (a < 0) a *= -1;

  if (b < 0) b *= -1;

  int pom = 0;

  while (b != 0) {
    if (b & 1) pom += a;
    a <<= 1;
    b >>= 1;
  }

  return znak * pom;
}

int iloraz(int a, int b) {
  /*
   * Funkcja zwraca iloraz a przez b, gdzie a i b sa liczbami naturalnymi.
   */

  std::function<int(int, int, int, int *)> wew_iloraz;
  wew_iloraz = [&wew_iloraz](int dzielna, int dzielnik, int org_b,
                             int *reszta) -> int {
    /*
     * Funkcja wewnetrzna funkcji iloraz.
     */
    int wynik = 1;

    if (dzielna == dzielnik) {
      *reszta = 0;
      return 1;
    }

    else if (dzielna < dzielnik) {
      *reszta = dzielna;
      return 0;
    }

    while (dzielnik <= dzielna) {
      dzielnik = dzielnik << 1;
      wynik = wynik << 1;
    }

    if (dzielna < dzielnik) {
      dzielnik >>= 1;
      wynik >>= 1;
    }

    wynik = wynik + wew_iloraz(dzielna - dzielnik, org_b, org_b, reszta);

    return wynik;
  };

  int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

  if (a < 0) a *= -1;

  if (b < 0) b *= -1;

  int reszta = 0;

  return znak * wew_iloraz(a, b, b, &reszta);
}

void test1() {
  int a = -2;
  int b = 2;
  int wynik = 0;
  assert(suma(a, b) == wynik);
}

void test2() {
  int a = 3;
  int b = 2;
  int wynik = 5;
  assert(suma(a, b) == wynik);
}

void test3() {
  int a = 3;
  int b = 2;
  int wynik = 1;
  assert(roznica(a, b) == wynik);
}

void test4() {
  int a = 10;
  int b = 15;
  int wynik = -5;
  assert(roznica(a, b) == wynik);
}

void test5() {
  int a = 3;
  int b = 2;
  int wynik = 6;
  assert(iloczyn(a, b) == wynik);
}

void test6() {
  int a = 10;
  int b = -2;
  int wynik = -20;
  assert(iloczyn(a, b) == wynik);
}

void test7() {
  int a = 9;
  int b = 3;
  int wynik = 3;
  assert(iloraz(a, b) == wynik);
}

void test8() {
  int a = 25;
  int b = -5;
  int wynik = -5;
  assert(iloraz(a, b) == wynik);
}

int main() {
  test1();
  test2();
  test3();
  test4();
  test5();
  test6();
  test7();
  test8();

  return 0;
}
