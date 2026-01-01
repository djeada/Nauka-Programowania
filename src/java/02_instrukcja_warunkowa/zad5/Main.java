/*
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());
    int c = Integer.parseInt(s.nextLine());

    int[] arr = {a, b, c};
    Arrays.sort(arr);
    System.out.println(arr[0] + " " + arr[1] + " " + arr[2]);
  }
}

