/*
ZAD-06 — Połączenie posortowanych list (unikalne)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.

### Wejście

* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

*/
import java.util.*;

public class Main {
  private static class Wezel implements Comparable<Wezel> {
    int wartosc;
    int i;
    int j;

    public Wezel(int wartosc, int i, int j) {
      this.wartosc = wartosc;
      this.i = i;
      this.j = j;
    }

    @Override
    public int compareTo(Wezel o) {
      return this.wartosc - o.wartosc;
    }
  }

  // Scala k posortowanych list w jedną posortowaną listę używając kopca
  // Złożoność czasowa: O(n log k) gdzie n to łączna liczba elementów, k to liczba list
  // Złożoność pamięciowa: O(n + k)
  public static ArrayList<Integer> polaczListyV1(ArrayList<ArrayList<Integer>> lista) {
    ArrayList<Integer> wynik = new ArrayList<Integer>();
    PriorityQueue<Wezel> kolejka = new PriorityQueue<Wezel>();

    for (int i = 0; i < lista.size(); i++) kolejka.add(new Wezel(lista.get(i).get(0), i, 0));

    while (!kolejka.isEmpty()) {
      Wezel min = kolejka.poll();
      wynik.add(min.wartosc);

      if (min.j + 1 < lista.get(min.i).size()) {
        min.j++;
        min.wartosc = lista.get(min.i).get(min.j);
        kolejka.add(min);
      }
    }

    return wynik;
  }

  public static void test1() {
    ArrayList<ArrayList<Integer>> lista = new ArrayList<ArrayList<Integer>>();
    lista.add(new ArrayList<Integer>(Arrays.asList(-6, 23, 29, 33)));
    lista.add(new ArrayList<Integer>(Arrays.asList(6, 22, 35, 71)));
    lista.add(new ArrayList<Integer>(Arrays.asList(5, 19, 21, 37)));
    lista.add(new ArrayList<Integer>(Arrays.asList(-12, -7, -3, 28)));

    ArrayList<Integer> wynik =
        new ArrayList<Integer>(
            Arrays.asList(-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71));

    assert (polaczListyV1(lista).equals(wynik));
  }

  public static void test2() {
    ArrayList<ArrayList<Integer>> lista = new ArrayList<ArrayList<Integer>>();
    lista.add(new ArrayList<Integer>(Arrays.asList(1, 2, 3)));
    lista.add(new ArrayList<Integer>(Arrays.asList(4, 5, 6)));

    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));

    assert (polaczListyV1(lista).equals(wynik));
  }

  public static void test3() {
    ArrayList<ArrayList<Integer>> lista = new ArrayList<ArrayList<Integer>>();
    ArrayList<Integer> wynik = new ArrayList<Integer>();

    assert (polaczListyV1(lista).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

