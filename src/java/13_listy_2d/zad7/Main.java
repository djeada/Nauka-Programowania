/*
ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* `n` wierszy zmodyfikowanej macierzy

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste 2d. Jesli element macierzy jest
  // rowny zero, zamien wszystkie elementy w tej samej
  // kolumnie i tym samym wierszu na zera.

  // Zlozonosc Czasowa: O(n * m)
  // Zlozonosc Pamieciowa: O(n + m)
  public static void wyzerujV1(ArrayList<ArrayList<Integer>> macierz) {

    if (macierz.isEmpty()) {
      return;
    }

    int M = macierz.size();
    int N = macierz.get(0).size();

    int[] wiersze = new int[N];
    int[] kolumny = new int[M];

    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (macierz.get(i).get(j) == 0) {
          wiersze[i] = 1;
          kolumny[j] = 1;
        }
      }
    }

    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (wiersze[i] == 1 || kolumny[j] == 1) {
          macierz.get(i).set(j, 0);
        }
      }
    }
  }

  public static void test1() {

    ArrayList<ArrayList<Integer>> macierz =
        new ArrayList<ArrayList<Integer>>(
            Arrays.asList(
                new ArrayList<Integer>(Arrays.asList(1, 2, 3)),
                new ArrayList<Integer>(Arrays.asList(4, 0, 6)),
                new ArrayList<Integer>(Arrays.asList(7, 8, 9))));

    ArrayList<ArrayList<Integer>> wynik =
        new ArrayList<ArrayList<Integer>>(
            Arrays.asList(
                new ArrayList<Integer>(Arrays.asList(1, 0, 3)),
                new ArrayList<Integer>(Arrays.asList(0, 0, 0)),
                new ArrayList<Integer>(Arrays.asList(7, 0, 9))));

    wyzerujV1(macierz);

    assert wynik.equals(macierz);
  }

  public static void main(String[] args) {

    test1();
  }
}

