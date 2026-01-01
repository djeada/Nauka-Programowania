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

    System.out.print("podaj cztery liczby:");
    System.out.print("\n");

    int a;
    int b;
    int c;
    int d;

    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    c = Integer.parseInt(s.nextLine());
    d = Integer.parseInt(s.nextLine());

    int maksAB = a > b ? a : b;
    int maksCD = c > d ? c : d;
    int maks = maksAB > maksCD ? maksAB : maksCD;

    System.out.print(maks);
    System.out.print("\n");
  }
}

