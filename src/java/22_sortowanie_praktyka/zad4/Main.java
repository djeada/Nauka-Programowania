/*
ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: napis (bez spacji)

### Wyjście

* 1 linia: lista napisów posortowana jak w przykładzie

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
['a', 'ab', 'abc', 'abcd']
```

*/
import java.util.*;

public class Main {

  public static void sortujWzgledemDlugosci(ArrayList<String> lista) {
    Collections.sort(
        lista,
        new Comparator<String>() {
          @Override
          public int compare(final String o1, final String o2) {
            return o1.length() - o2.length();
          }
        });
  }

  public static void test1() {
    ArrayList<String> lista = new ArrayList<String>(Arrays.asList("abcd", "ab", "a", "abc"));
    ArrayList<String> oczekiwane = new ArrayList<String>(Arrays.asList("a", "ab", "abc", "abcd"));

    sortujWzgledemDlugosci(lista);

    assert lista.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}

