/*
ZAD-07 — Sortowanie listy 0/1/2

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1/2) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
7
1 0 1 2 2 0 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 2, 2]
```

*/
import java.util.*;

public class Main {
  public static void sortuj(ArrayList<Integer> lista) {
    int zera = 0;
    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 0) {
        zera++;
      }
    }

    for (int i = 0; i < zera; i++) {
      lista.set(i, 0);
    }

    for (int i = zera; i < lista.size(); i++) {
      lista.set(i, 1);
    }
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 0, 0, 1, 1, 2, 0));
    ArrayList<Integer> oczekiwane = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 1, 1, 1, 2));

    sortuj(lista);

    assert lista.equals(oczekiwane);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1, 1, 1));
    ArrayList<Integer> oczekiwane = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1, 1, 1));

    sortuj(lista);

    assert lista.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

