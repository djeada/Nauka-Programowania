/*
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych czterech liczb, znajdz najwieksza liczbe.

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());
    int c = Integer.parseInt(s.nextLine());
    int d = Integer.parseInt(s.nextLine());

    int max = Math.max(Math.max(a, b), Math.max(c, d));
    System.out.println(max);
  }
}

