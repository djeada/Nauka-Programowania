/*
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb
  // przy pomocy petli obliczy ile wynosi a podniesione do b.

  public static double potega(int a, int b) {
    int wynik = 1;
    for (int i = 0; i < Math.abs(b); i++) {
      wynik *= a;
    }

    if (b < 0) {
      return 1 / wynik;
    }

    return wynik;
  }

  public static void test1() {
    int a = 2;
    int b = 3;
    double wynik = 8.00;

    assert Math.abs(potega(a, b) - wynik) < 0.01;
  }

  public static void test2() {
    int a = 10;
    int b = -5;
    double wynik = 0.00001;

    assert Math.abs(potega(a, b) - wynik) < 0.01;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

