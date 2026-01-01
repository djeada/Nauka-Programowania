/*
ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

**Wyjście:**

```
15
```

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
  // ich najwiekszy wspolny dzielnik.

  public static int nwdV1(int a, int b) {

    if (b == 0) {
      return a;
    }

    return nwdV1(b, a % b);
  }

  public static int nwdV2(int a, int b) {

    int c;

    while (b != a % b) {
      c = b;
      b = a % b;
      a = c;

      if (b == 0) {
        break;
      }
    }

    return a;
  }

  public static void test1() {
    int a = 14;
    int b = 21;
    int wynik = 7;

    assert nwdV1(a, b) == wynik;
  }

  public static void test2() {
    int a = 14;
    int b = 21;
    int wynik = 7;

    assert nwdV2(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

