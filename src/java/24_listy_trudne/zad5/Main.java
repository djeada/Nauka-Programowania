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

  // Generuje zbiór potęgowy - wszystkie możliwe (różne) podzbiory listy.
  // Elementy listy są najpierw sortowane, dzięki czemu podzbiory różniące się
  // tylko kolejnością powtórzonych elementów (np. [1, 2] i [2, 1]) są takie same
  // i trafiają do wyniku tylko raz.
  // Złożoność czasowa: O(2^n * n) gdzie n to długość listy
  // Złożoność pamięciowa: O(2^n * n) - przechowuje wszystkie podzbiory
  public static ArrayList<ArrayList<Integer>> zbiorPotegowy(ArrayList<Integer> lista) {
    ArrayList<Integer> posortowana = new ArrayList<Integer>(lista);
    Collections.sort(posortowana);

    int N = 1 << posortowana.size();
    Set<ArrayList<Integer>> zbiorPotegowy = new LinkedHashSet<ArrayList<Integer>>();

    for (int i = 0; i < N; i++) {
      ArrayList<Integer> podzbior = new ArrayList<Integer>();

      for (int j = 0; j < posortowana.size(); j++) {
        if ((i & (1 << j)) != 0)
          podzbior.add(posortowana.get(j));
      }

      zbiorPotegowy.add(podzbior);
    }

    return new ArrayList<ArrayList<Integer>>(zbiorPotegowy);
  }

  // Porównuje dwie kolekcje podzbiorów bez względu na ich kolejność.
  private static boolean takieSamePodzbiory(
      List<ArrayList<Integer>> wynik, List<ArrayList<Integer>> oczekiwane) {
    return wynik.size() == oczekiwane.size()
        && new HashSet<ArrayList<Integer>>(wynik).equals(new HashSet<ArrayList<Integer>>(oczekiwane));
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

    assert takieSamePodzbiory(zbiorPotegowy(lista), wynik);
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

    assert takieSamePodzbiory(zbiorPotegowy(lista), wynik);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();

    ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>>();
    wynik.add(new ArrayList<Integer>(Arrays.asList()));

    assert takieSamePodzbiory(zbiorPotegowy(lista), wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }

}

