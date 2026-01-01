/*
ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każda w osobnej linii).

### Wejście

Dwie liczby całkowite:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia / gwarancje

* `a`, `b` mieszczą się w typowym zakresie int (np. 32-bit).

### Przykład

**Wejście:**

```
-7
4
```

**Wyjście:**

```
4
-7
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    int a;
    int b;

    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    System.out.print(b);
    System.out.print("\n");
    System.out.print(a);
    System.out.print("\n");
  }
}

