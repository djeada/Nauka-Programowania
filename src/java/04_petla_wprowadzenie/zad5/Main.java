/*
ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:

* `lo = min(a, b)`
* `hi = max(a, b)`

Następnie:

a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).

b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).

### Wejście

Dwie liczby naturalne:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

### Uwagi o formatowaniu

* Nie wypisuj nagłówków typu „a)” i „b)”.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
* Nie dodawaj pustej linii między podpunktami.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych dwoch liczb, powinny zostac wyswietlone:

    System.out.print("Podaj dwie liczby: \n");

    int a;
    int b;

    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    if (b < a) {
      int pom = a;
      a = b;
      b = pom;
    }

    // wszystkie liczby naturalne wieksze od mniejszej pobranej
    // liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.
    for (int i = a + 1; i < b; i++) {
      System.out.print(i);
      System.out.print(" ");
    }

    System.out.print("\n");

    // wszystkie liczby naturalne podzielne przez 3
    // wieksze od mniejszej pobranej liczby i jednoczesnie
    // mniejsze od wiekszej pobranej liczby.
    for (int i = a + 1; i < b; i++) {
      if (i % 3 == 0) {
        System.out.print(i);
        System.out.print(" ");
      }
    }
  }
}

