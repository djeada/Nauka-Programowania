/*
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

*/
import java.util.*;

public class Main {

  // Generuje zbiór potęgowy - wszystkie możliwe podzbiory listy
  // Złożoność czasowa: O(2^n * n) gdzie n to długość listy
  // Złożoność pamięciowa: O(2^n * n) - przechowuje wszystkie podzbiory
  public static ArrayList<ArrayList<Integer>> zbiorPotegowy(ArrayList<Integer> lista) {
    int N = (int) Math.pow(2, lista.size());
    ArrayList<ArrayList<Integer>> zbiorPotegowy = new ArrayList<ArrayList<Integer>>();

    for (int i = 0; i < N; i++) {
      ArrayList<Integer> podzbior = new ArrayList<Integer>();

      for (int j = 0; j < lista.size(); j++) {
        if ((i & (1 << j)) != 0)
          podzbior.add(lista.get(j));
      }

      zbiorPotegowy.add(podzbior);
    }

    return zbiorPotegowy;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(2);
    lista.add(1);

    ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>>();
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 1, 2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList()));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 1)));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(5);
    lista.add(3);

    ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>>();
    wynik.add(new ArrayList<Integer>(Arrays.asList(3)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(3, 5)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(5)));
    wynik.add(new ArrayList<Integer>(Arrays.asList()));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();

    ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>>();
    wynik.add(new ArrayList<Integer>(Arrays.asList()));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }

}

