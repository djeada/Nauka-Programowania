/*
ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.

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
public class Main {
  // Znajdz potege dwojki wieksza badz rowna otrzymanej liczbie.
  // Inaczej: zaaokraglij liczbe do nastepnej potegi dwojki.
  // Dla otrzymanej liczby ujemnej zwroc 0.

  public static int nastepnaPotegaDwojkiV1(int liczba) {
    if (liczba <= 0) {
      return 0;
    }

    if (liczba == 1) {
      return 2;
    }

    liczba--;

    while ((liczba & (liczba - 1)) != 0) {
      liczba &= liczba - 1;
    }

    return liczba << 1;
  }

  public static int nastepnaPotegaDwojkiV2(int liczba) {
    if (liczba <= 0) {
      return 0;
    }

    int potega = 2;

    while (liczba > 2) {
      liczba >>= 1;
      potega <<= 1;
    }

    return potega;
  }

  public static void test1() {
    int liczba = 111;
    int wynik = 128;

    assert nastepnaPotegaDwojkiV1(liczba) == wynik;
  }

  public static void test2() {
    int liczba = -30;
    int wynik = 0;

    assert nastepnaPotegaDwojkiV1(liczba) == wynik;
  }

  public static void test3() {
    int liczba = 1;
    int wynik = 2;

    assert nastepnaPotegaDwojkiV1(liczba) == wynik;
  }

  public static void test4() {
    int liczba = 111;
    int wynik = 128;

    assert nastepnaPotegaDwojkiV2(liczba) == wynik;
  }

  public static void test5() {
    int liczba = -30;
    int wynik = 0;

    assert nastepnaPotegaDwojkiV2(liczba) == wynik;
  }

  public static void test6() {
    int liczba = 1;
    int wynik = 2;

    assert nastepnaPotegaDwojkiV2(liczba) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
  }
}

