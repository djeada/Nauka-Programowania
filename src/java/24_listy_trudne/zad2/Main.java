/*
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

*/
import java.util.*;

public class Main {

  // Przenosi wszystkie zera na koniec listy zachowując kolejność pozostałych elementów:
  // każdy niezerowy element zamieniamy z pierwszą wolną pozycją na początku listy
  // Złożoność czasowa: O(n) gdzie n to długość listy
  // Złożoność pamięciowa: O(1) - modyfikuje listę w miejscu
  public static void zeraV1(ArrayList<Integer> lista) {
    int pozycja = 0;

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) != 0) {
        Collections.swap(lista, pozycja, i);
        pozycja++;
      }
    }
  }

  public static void test1() {
    ArrayList<Integer> lista =
        new ArrayList<Integer>(Arrays.asList(0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0));
    ArrayList<Integer> wynik =
        new ArrayList<Integer>(Arrays.asList(1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

