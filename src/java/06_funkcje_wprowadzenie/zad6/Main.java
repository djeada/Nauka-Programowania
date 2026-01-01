/*
ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

### Wejście

Jeden argument: `n` (`n ≥ 0`)

### Wyjście

Funkcja zwraca sumę cyfr.

### Przykład

**Wywołanie funkcji:**

```python
print(suma_cyfr(13231))
```

**Wyjście:**

```
10
```

### Uwagi

* Dla `n = 0` suma cyfr to `0`.

*/
import java.util.*;

public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

  public static int sumaCyfr(int a) {
    int suma = 0;

    while (a > 0) {
      suma += (a % 10);
      a /= 10;
    }

    return suma;
  }

  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    System.out.println(sumaCyfr(n));
  }
}

