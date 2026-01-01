/*
ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry w kolejności od cyfry jedności (czyli w odwrotnej kolejności niż w zapisie liczby). Każdą cyfrę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Kolejne cyfry `n` w odwrotnej kolejności, każda w nowej linii.

### Przykład

**Wejście:**

```
8214
```

**Wyjście:**

```
4
1
2
8
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz jedną linię z `0`.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, powinny zostac zwrocone
    // cyfry pobranej liczby poczynajac od cyfry jednosci.

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    while (a > 0) {
      System.out.print(a % 10);
      System.out.print("\n");
      a = a / 10;
    }
  }
}

