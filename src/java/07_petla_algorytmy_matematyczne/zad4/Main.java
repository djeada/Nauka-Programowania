/*
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

*/
public class Main {
  // Napisz funkcje, ktora przy pomocy petli obliczy silnie
  // z otrzymanej liczby.

  public static int silnia(int a) {

    int wynik = 1;

    while (a > 0) {
      wynik *= a;
      a--;
    }

    return wynik;
  }

  public static void test1() {
    int a = 4;
    int wynik = 24;
    assert silnia(a) == wynik;
  }

  public static void test2() {
    int a = -5;
    int wynik = 1;
    assert silnia(a) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

