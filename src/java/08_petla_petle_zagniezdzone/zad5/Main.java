/*
ZAD-05 — Litera „X”

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `X` o wysokości `n`, zbudowaną z `*` na obu przekątnych.

W wierszu `i` i kolumnie `j` (indeksy od 0):

* wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`,
* w przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków (`*` lub spacja).

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*   *
 * *
  *
 * *
*   *
```

*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i || j == n - 1 - i) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
