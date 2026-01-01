/*
ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko dodawania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a * b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 2))
```

**Wyjście:**

```
6
```

ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko odejmowania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a // b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 2))
```

**Wyjście:**

```
1
```

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb,
  // przy pomocy dodawania badz odejmowania oraz petli zrealizuje:

  // a) mnozenie;
  public static int mnozenie(int a, int b) {
    int wynik = 0;
    for (int i = 0; i < b; i++) {
      wynik += a;
    }

    return wynik;
  }

  // b) dzielenie
  public static int dzielenie(int a, int b) {
    int wynik = 0;
    while (a >= b) {
      a -= b;
      wynik++;
    }

    return wynik;
  }

  public static void test1() {
    int a = 2;
    int b = 3;

    int wynik = 6;
    assert mnozenie(a, b) == wynik;
  }

  public static void test2() {
    int a = 30;
    int b = 6;

    int wynik = 5;
    assert dzielenie(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

