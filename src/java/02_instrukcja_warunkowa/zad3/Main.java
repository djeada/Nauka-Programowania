/*
ZAD-03 — Określanie znaku liczby

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `string`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:

* dla `x < 0`: `Liczba jest ujemna.`
* dla `x > 0`: `Liczba jest dodatnia.`
* dla `x = 0`: `Liczba jest zerem.`

### Wejście

* 1 linia: `x` (liczba całkowita)

### Wyjście

Jedna linia — dokładnie jeden komunikat.

### Przykłady

**Wejście:**

```
-5
```

**Wyjście:**

```
Liczba jest ujemna.
```

**Wejście:**

```
0
```

**Wyjście:**

```
Liczba jest zerem.
```

**Wejście:**

```
2
```

**Wyjście:**

```
Liczba jest dodatnia.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

    System.out.print("podaj liczbe:\n");

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    if (a < 0) {
      System.out.print("liczba jest ujemna\n");
    } else if (a > 0) {
      System.out.print("liczba jest dodatnia\n");
    } else {
      System.out.print("liczba jest zerem\n");
    }
  }
}

