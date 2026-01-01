/*
ZAD-03A — Dodawanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie operatorów bitowych (i przesunięć).

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

Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np. metoda „shift-and-add”).

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
public class Main {
  // Otrzymujesz liczbe, zamien ja na jej binarny odpowiednik jesli:

  // a) jest liczba parzysta.
  // Otrzymujesz dwie liczby. Uzywajac jedynie operatorow bitowych zaimplementuj:

  // a) dodawanie.
  // Zlozonosc Czasowa: O(log n)
  // Zlozonosc Pamieciowa: O(1)
  private static int suma(int a, int b) {

    while (b != 0) {
      int pom = a & b;
      a = a ^ b;
      b = pom << 1;
    }

    return a;
  }

  // b) odejmowanie.
  // Zlozonosc Czasowa: O(log n)
  // Zlozonosc Pamieciowa: O(1)
  private static int roznica(int a, int b) {

    while (b != 0) {
      int pom = (~a) & b;
      a = a ^ b;
      b = pom << 1;
    }

    return a;
  }

  // c) mnozenie.
  // Zlozonosc Czasowa: O(log n)
  // Zlozonosc Pamieciowa: O(1)
  private static int iloczyn(int a, int b) {

    int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

    if (a < 0) {
      a *= -1;
    }

    if (b < 0) {
      b *= -1;
    }

    int pom = 0;

    while (b != 0) {
      if ((b & 1) != 0) {
        pom += a;
      }
      a <<= 1;
      b >>= 1;
    }

    return znak * pom;
  }

  // d) dzielenie.
  // Zlozonosc Czasowa: O(log^2 n)
  // Zlozonosc Pamieciowa: O(log n) - rekurencja
  private static int wew_iloraz(int dzielna, int dzielnik, int org_b, int reszta) {
    int wynik = 1;

    if (dzielna == dzielnik) {
      reszta = 0;
      return 1;
    } else if (dzielna < dzielnik) {
      reszta = dzielna;
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
  }
  ;

  private static int iloraz(int a, int b) {
    int znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;

    if (a < 0) {
      a *= -1;
    }

    if (b < 0) {
      b *= -1;
    }

    int reszta = 0;

    return znak * wew_iloraz(a, b, b, reszta);
  }

  private static void test1() {
    int a = -2;
    int b = 2;
    int wynik = 0;
    assert suma(a, b) == wynik;
  }

  private static void test2() {
    int a = 3;
    int b = 2;
    int wynik = 5;
    assert suma(a, b) == wynik;
  }

  private static void test3() {
    int a = 3;
    int b = 2;
    int wynik = 1;
    assert roznica(a, b) == wynik;
  }

  private static void test4() {
    int a = 10;
    int b = 15;
    int wynik = 150;
    assert iloczyn(a, b) == wynik;
  }

  private static void test5() {
    int a = -2;
    int b = 2;
    int wynik = -4;
    assert iloczyn(a, b) == wynik;
  }

  private static void test6() {
    int a = 3;
    int b = 2;
    int wynik = 5;
    assert suma(a, b) == wynik;
  }

  private static void test7() {
    int a = 30;
    int b = -3;
    int wynik = -10;
    assert iloraz(a, b) == wynik;
  }

  private static void test8() {
    int a = 10;
    int b = 5;
    int wynik = 2;
    assert iloraz(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();
  }
}

