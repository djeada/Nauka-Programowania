/*
ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu linii.
* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.

*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        
        int count = 0;
        int num = 2;
        
        while (count < n) {
            if (isPrime(num)) {
                if (count > 0) System.out.print(" ");
                System.out.print(num);
                count++;
            }
            num++;
        }
        System.out.println();
    }
    
    static boolean isPrime(int x) {
        if (x < 2) return false;
        if (x == 2) return true;
        if (x % 2 == 0) return false;
        
        for (int i = 3; i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}
