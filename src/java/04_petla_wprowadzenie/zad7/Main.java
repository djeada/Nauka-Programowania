/*
ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz `1.00`.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wyswietl liczbe Pi podniesiona
    // do potegi rownej pobranej liczbie. Wynik powinien byc
    // zaokraglony do dwoch miejsc po przecinku.

    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    float wynik = (float) 1.0;
    for (int i = 0; i < n; i++) {
      wynik *= 3.14;
    }

    System.out.printf("%.2f", wynik);
    System.out.printf("\n");
  }
}

