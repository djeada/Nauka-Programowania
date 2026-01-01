/*
ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli `a = b`, wypisz `a b` (czyli dwie takie same liczby).

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia:
`max(a, b) min(a, b)`

### Przykłady

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

    System.out.print("podaj dwie liczby:\n");

    int a;
    int b;
    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    if (a > b) {
      System.out.print(a + "\n");
      System.out.print(b + "\n");
      System.out.print("pierwsza liczba jest wieksza od drugiej\n");

    } else {
      System.out.print(b + "\n");
      System.out.print(a + "\n");
      System.out.print("pierwsza liczba nie jest wieksza od drugiej\n");
    }
  }
}

