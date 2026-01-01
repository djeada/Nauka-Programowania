/*
ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        
        int[][] triangle = new int[n][];
        
        for (int i = 0; i < n; i++) {
            triangle[i] = new int[i + 1];
            triangle[i][0] = 1;
            triangle[i][i] = 1;
            
            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
            
            for (int j = 0; j <= i; j++) {
                System.out.print(triangle[i][j]);
                if (j < i) System.out.print(" ");
            }
            System.out.println();
        }
    }
}
