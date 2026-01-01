/*
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.

    System.out.print("podaj trzy liczby:");
    System.out.print("\n");

    int a;
    int b;
    int c;
    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    c = Integer.parseInt(s.nextLine());

    if (a >= b && a >= c) {
      if (b >= c) {
        System.out.print(c + "\n");
        System.out.print(b + "\n");
        System.out.print(a + "\n");
        System.out.print("\n");
      } else {
        System.out.print(b + "\n");
        System.out.print(c + "\n");
        System.out.print(a + "\n");
        System.out.print("\n");
      }
    } else if (c >= b && c >= a) {
      if (a >= b) {
        System.out.print(b + "\n");
        System.out.print(a + "\n");
        System.out.print(c + "\n");
        System.out.print("\n");
      } else {
        System.out.print(a + "\n");
        System.out.print(b + "\n");
        System.out.print(c + "\n");
        System.out.print("\n");
      }
    } else {
      if (a >= c) {
        System.out.print(c + "\n");
        System.out.print(a + "\n");
        System.out.print(b + "\n");
        System.out.print("\n");
      } else {
        System.out.print(a + "\n");
        System.out.print(c + "\n");
        System.out.print(b + "\n");
        System.out.print("\n");
      }
    }
  }
}

