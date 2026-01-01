/*
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste par liczb. Liczby w parze reprezentuja poczatek i
  // koniec przedzialu. Niektore przedzialy moga na siebie nachodzic. W takim
  // przypadku polacz je ze soba i zwroc liste niepokrywajacych sie przedzialow.
  private static class Pair<T1, T2> {
    public T1 first;
    public T2 second;

    public Pair(T1 firstValue, T2 secondValue) {
      first = firstValue;
      second = secondValue;
    }

    @Override
    public boolean equals(Object o) {
      return (o instanceof Pair)
          && (this.first == ((Pair) o).first)
          && (this.second == ((Pair) o).second);
    }
  }

  // Zlozonosc Czasowa: O(n log n)
  // Zlozonosc Pamieciowa: O(n)
  public static ArrayList<Pair<Integer, Integer>> polaczPrzedzialyV1(
      ArrayList<Pair<Integer, Integer>> lista) {

    Collections.sort(
        lista,
        new Comparator<Pair<Integer, Integer>>() {
          public int compare(Pair<Integer, Integer> p1, Pair<Integer, Integer> p2) {
            return p1.second.compareTo(p2.first);
          }
        });

    int pocz = lista.get(0).first;
    int koniec = lista.get(0).second;
    lista.remove(0);

    ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>();

    for (var para : lista) {

      if (koniec >= para.first) {
        if (koniec < para.second) {
          koniec = para.second;
        }
      } else {

        wynik.add(new Pair<Integer, Integer>(pocz, koniec));
        pocz = para.first;
        koniec = para.second;
      }
    }

    wynik.add(new Pair<Integer, Integer>(pocz, koniec));

    return wynik;
  }

  public static void test1() {
    ArrayList<Pair<Integer, Integer>> lista =
        new ArrayList<Pair<Integer, Integer>>(
            Arrays.asList(
                new Pair<Integer, Integer>(23, 67),
                new Pair<Integer, Integer>(23, 53),
                new Pair<Integer, Integer>(45, 88),
                new Pair<Integer, Integer>(10, 22),
                new Pair<Integer, Integer>(11, 42),
                new Pair<Integer, Integer>(42, 45)));

    ArrayList<Pair<Integer, Integer>> wynik =
        new ArrayList<Pair<Integer, Integer>>(
            Arrays.asList(new Pair<Integer, Integer>(10, 22), new Pair<Integer, Integer>(23, 88)));

    assert wynik.equals(polaczPrzedzialyV1(lista));
  }

  public static void main(String[] args) {
    test1();
  }
}

