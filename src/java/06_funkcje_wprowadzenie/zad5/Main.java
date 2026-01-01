/*
ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

* najpierw nowa wartość `a` (czyli stare `b`)
* potem nowa wartość `b` (czyli stare `a`)

### Przykład

**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

**Wyjście:**

```
a = 5
b = 8
```

*/
import java.util.*;

public class Main {
  // Napisz funkcje, ktora:

  // a) dla podanych dwoch liczb, zwroci mniejsza
  public static int min2(int a, int b) {
    return a < b ? a : b;
  }

  // b) dla podanych dwoch liczb, zwroci wieksza
  public static int maks2(int a, int b) {
    return a > b ? a : b;
  }

  // c) dla podanych trzech liczb, zwroci najmniejsza
  public static int min3(int a, int b, int c) {
    int minAB = a < b ? a : b;
    return minAB < c ? minAB : c;
  }

  // d) dla podanych trzech liczb, zwroci najwieksza
  public static int maks3(int a, int b, int c) {
    int maksAB = a > b ? a : b;
    return maksAB > c ? maksAB : c;
  }

  public static void main(String[] args) {

    System.out.print("Podaj dwie liczby: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.print("mniejsza liczba to: " + min2(a, b) + "\n");
    System.out.print("wieksza liczba to: " + maks2(a, b) + "\n");

    System.out.print("Podaj trzy liczby: \n");
    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    int c = Integer.parseInt(s.nextLine());

    System.out.print("najmniejsza liczba to: " + min3(a, b, c) + "\n");
    System.out.print("najwieksza liczba to " + maks3(a, b, c) + "\n");
  }
}

