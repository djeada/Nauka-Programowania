/*
ZAD-01 — Kwadrat

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i wypisz kwadrat `n × n` zbudowany z gwiazdek `*`.
Każdy wiersz ma zawierać dokładnie `n` gwiazdek (bez spacji).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w każdej dokładnie `n` znaków `*`.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
**
**
```

*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
