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
    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    // a_n = n/(n+1)
    float suma = (float) 0.0;
    for (float i = 1; i <= n; i++) {
      float a = i / (i + 1);
      suma += a;
    }
    System.out.printf("%.2f", suma);
    System.out.printf("\n");

    // a_n = (n^2+5)/n
    suma = (float) 0.0;
    for (float i = 1; i <= n; i++) {
      float a = (float) ((Math.pow(i, 2) + 5) / i);
      suma += a;
    }
    System.out.printf("%.2f", suma);
    System.out.printf("\n");

    // a_n = n + 2^n
    suma = (float) 0.0;
    for (int i = 1; i <= n; i++) {
      int a = (int) (i + Math.pow(2, i));
      suma += a;
    }

    System.out.printf("%.2f", suma);
    System.out.printf("\n");
  }
}

