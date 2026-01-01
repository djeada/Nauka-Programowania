/*
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby n, wyswietl sume n
    // pierwszych wyrazow ciagu danego wzorem:
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    // a) sum k^2 + k + 1
    int sum1 = 0;
    for (int k = 1; k <= n; k++) {
      sum1 += k * k + k + 1;
    }
    System.out.println(sum1);

    // b) sum k^2 + 5k
    int sum2 = 0;
    for (int k = 1; k <= n; k++) {
      sum2 += k * k + 5 * k;
    }
    System.out.println(sum2);

    // c) sum 3k
    int sum3 = 0;
    for (int k = 1; k <= n; k++) {
      sum3 += 3 * k;
    }
    System.out.println(sum3);
  }
}

