/*
ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. `a + b`
2. `a - b`
3. `a * b`
4. `a // b` (dzielenie całkowite)
5. `a % b`
6. `a^b`

### Wejście

* 1. linia: `a` (liczba całkowita)
* 2. linia: `b` (liczba całkowita)

### Wyjście

6 linii — wyniki działań w kolejności 1–6.

### Ograniczenia / gwarancje

* `a ≥ 0`
* `b > 0` (żeby dzielenie i modulo były poprawne)

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
5
1
6
1
1
9
```

*/
import java.util.*;

public class Main {

  public static void main(String[] args) {

    int x;
    int y;
    Scanner s = new Scanner(System.in);

    System.out.print("Podaj dwie liczby: \n");

    x = Integer.parseInt(s.nextLine());
    y = Integer.parseInt(s.nextLine());

    System.out.print("Suma " + x + " oraz " + y + " wynosi " + (x + y) + "\n");
    System.out.print("Roznica " + x + " i " + y + " wynosi " + (x - y) + "\n");
    System.out.print("Iloczyn " + x + " i " + y + " wynosi " + (x * y) + "\n");
    System.out.print("Iloraz " + x + " przez " + y + " wynosi " + (x / y) + "\n");
    System.out.print("Reszta z dzielenia " + x + " przez " + y + " wynosi " + (x % y) + "\n");
    System.out.print(x + " podniesione do " + y + " wynosi " + Math.pow(x, y) + "\n");
  }
}

