/*
ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość`.
a) Wypisz listę par posortowaną rosnąco po kluczach.
b) Wypisz listę par posortowaną rosnąco po wartościach.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`

### Wyjście

* 1 linia: lista par dla a)
* 2 linia: lista par dla b)

### Przykład

**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

**Wyjście:**

```
[('a', -2), ('b', 4), ('c', 3), ('x', 5)]
[('a', -2), ('c', 3), ('b', 4), ('x', 5)]
```

*/
import java.util.*;

public class Main {

  public static List<String> sortujWzgledemKluczyV1(Map<String, Integer> slownik) {

    List<String> lista = new ArrayList<String>();

    for (String key : slownik.keySet()) lista.add(key);

    Collections.sort(lista);

    return lista;
  }

  public static List<Integer> sortujWzgledemWartosciV1(Map<String, Integer> slownik) {

    List<Integer> lista = new ArrayList<Integer>();

    for (String key : slownik.keySet()) lista.add(slownik.get(key));

    Collections.sort(lista);

    return lista;
  }

  private static void test1() {
    Map<String, Integer> slownik =
        new HashMap<String, Integer>() {
          {
            put("c", 3);
            put("x", 5);
            put("a", -2);
            put("b", 4);
          }
        };

    List<Integer> wynik = Arrays.asList(-2, 3, 4, 5);

    assert sortujWzgledemWartosciV1(slownik).equals(wynik);
  }

  private static void test2() {
    Map<String, Integer> slownik =
        new HashMap<String, Integer>() {
          {
            put("c", 3);
            put("x", 5);
            put("a", -2);
            put("b", 4);
          }
        };

    List<Integer> wynik = Arrays.asList(-2, 3, 4, 5);

    assert sortujWzgledemWartosciV1(slownik).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

