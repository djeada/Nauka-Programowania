/*
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

* 1 linia: lista par posortowana jak w podpunkcie a)
* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

*/
import java.util.*;

public class Main {

  // Klasa reprezentująca parę (napis, liczba)
  private static class Para implements Comparable<Para> {
    private final String napis;
    private final int liczba;

    public Para(final String napis, final int liczba) {
      this.napis = napis;
      this.liczba = liczba;
    }

    public String getNapis() {
      return napis;
    }

    public int getLiczba() {
      return liczba;
    }

    @Override
    public int compareTo(final Para o) {
      if (liczba < o.liczba) {
        return -1;
      } else if (liczba > o.liczba) {
        return 1;
      } else {
        return napis.compareTo(o.napis);
      }
    }
  }

  public static void sortujWzgledemLiczb(ArrayList<Para> lista) {
    Collections.sort(
        lista,
        new Comparator<Para>() {
          @Override
          public int compare(final Para o1, final Para o2) {
            return o1.liczba - o2.liczba;
          }
        });
  }

  public static void sortujWzgledemDlugosci(ArrayList<Para> lista) {
    Collections.sort(
        lista,
        new Comparator<Para>() {
          @Override
          public int compare(final Para o1, final Para o2) {
            return o1.napis.length() - o2.napis.length();
          }
        });
  }

  public static void test1() {
    final ArrayList<Para> lista =
        new ArrayList<Para>(
            Arrays.asList(new Para("abc", 3), new Para("bca", 1), new Para("cab", 2)));
    final ArrayList<Para> oczekiwane =
        new ArrayList<Para>(
            Arrays.asList(new Para("bca", 1), new Para("cab", 2), new Para("abc", 3)));

    sortujWzgledemLiczb(lista);

    assert lista.equals(oczekiwane);
  }

  public static void test2() {
    final ArrayList<Para> lista =
        new ArrayList<Para>(Arrays.asList(new Para("ab", 3), new Para("abc", 1), new Para("a", 2)));
    final ArrayList<Para> oczekiwane =
        new ArrayList<Para>(Arrays.asList(new Para("a", 2), new Para("ab", 3), new Para("abc", 1)));

    sortujWzgledemDlugosci(lista);

    assert lista.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

