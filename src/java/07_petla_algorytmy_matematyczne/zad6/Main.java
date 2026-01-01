/*
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
  // ich najmniejsza wspolna wielokrotnosc.

  public static int nwd(int a, int b) {

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

  public static int nww(int a, int b) {
    return a * b / nwd(a, b);
  }

  public static void test1() {
    int a = 14;
    int b = 21;
    int wynik = 42;

    assert nww(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

