/*
ZAD-02 — Porównanie dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

**Wejście:**

```
7
4
```

**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
Liczby są identyczne.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    if (a == b) {
      System.out.println("Liczby są identyczne.");
    } else {
      System.out.println("Liczby są różne.");
    }
  }
}

