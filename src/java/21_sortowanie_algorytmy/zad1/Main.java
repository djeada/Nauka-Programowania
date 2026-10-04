/*
ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania bąbelkowego**.
Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w całym przebiegu nie zajdzie żadna zamiana.

### Wejście

* 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Po każdym pełnym przebiegu największy element „wypływa” na koniec.
* W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.

*/
import java.util.*;

public class Main {
  // Sortowanie bąbelkowe - porównuje sąsiednie elementy i zamienia je miejscami;
  // po każdym przebiegu największy element trafia na koniec. Kończy, gdy w
  // przebiegu nie wykonano żadnej zamiany.
  // Złożoność czasowa: O(n²) - dwie zagnieżdżone pętle, O(n) dla posortowanej listy
  // Złożoność pamięciowa: O(1) - sortowanie w miejscu
  public static void sortuj(ArrayList<Integer> lista) {
    int n = lista.size();

    for (int i = 0; i < n - 1; i++) {
      boolean zamieniono = false;

      for (int j = 0; j < n - 1 - i; j++) {
        if (lista.get(j) > lista.get(j + 1)) {
          var temp = lista.get(j);
          lista.set(j, lista.get(j + 1));
          lista.set(j + 1, temp);
          zamieniono = true;
        }
      }

      if (!zamieniono) {
        break;
      }
    }
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    sortuj(lista);
    assert lista.equals(wynik);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, -1, 3, 0, -1, 7));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(-1, -1, 0, 3, 3, 7));

    sortuj(lista);
    assert lista.equals(wynik);

    ArrayList<Integer> pusta = new ArrayList<Integer>();
    sortuj(pusta);
    assert pusta.isEmpty();
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

