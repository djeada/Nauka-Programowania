/*
ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.

ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

*/
import java.util.*;

public class Main {

  public static int zera(int n) {
    int licznik = 0;
    while (n > 0) {
      if (n % 2 == 0) {
        licznik++;
      }
      n /= 2;
    }
    return licznik;
  }

  public static int jedynki(int n) {
    int licznik = 0;
    while (n > 0) {
      if (n % 2 == 1) {
        licznik++;
      }
      n /= 2;
    }
    return licznik;
  }

  public static void test1() {
    int a = -2;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert (wynik == oczekiwane);
  }

  public static void test2() {
    int a = 3;
    int oczekiwane = 2;
    int wynik = jedynki(a);
    assert (wynik == oczekiwane);
  }

  public static void test3() {
    int a = 3;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert (wynik == oczekiwane);
  }

  public static void test4() {
    int a = 7;
    int oczekiwane = 3;
    int wynik = jedynki(a);
    assert (wynik == oczekiwane);
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
    test4();
  }
}

