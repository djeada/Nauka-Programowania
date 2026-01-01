/*
ZAD-04 — Tabliczka mnożenia N × N

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `formatowanie`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz tabliczkę mnożenia `N × N`.

W wierszu `i` i kolumnie `j` (licząc od 1) ma znaleźć się wartość `i*j`.
Liczby w jednym wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

`N` linii, w każdej `N` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1 2 3
2 4 6
3 6 9
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                System.out.print(i * j);
                if (j < n) System.out.print(" ");
            }
            System.out.println();
        }
    }
}
