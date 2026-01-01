/*
ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.

### Wejście

* Najpierw:

  * 1 linia: `n`
  * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
* Potem:

  * 1 linia: `m`
  * następnie `m` linii: `klucz v1 v2 v3 ...`

### Wyjście

* `Prawda` lub `Fałsz`

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

*/
import java.util.*;

public class Main {

  public static <A, B> boolean czyIdentyczneV1(
      Map<String, int[]> slownikA, Map<String, int[]> slownikB) {

    if (slownikA.size() != slownikB.size()) return false;

    return slownikA.entrySet().stream()
        .allMatch(e -> Arrays.equals(e.getValue(), slownikB.get(e.getKey())));
  }

  private static void test1() {
    Map<String, int[]> slownikA =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {-3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    Map<String, int[]> slownikB =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    assert !czyIdentyczneV1(slownikA, slownikB);
  }

  private static void test2() {

    Map<String, int[]> slownikC =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {-3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    assert czyIdentyczneV1(slownikA, slownikC);
  }

  private static void test3() {
    Map<String, int[]> slownikA =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {-3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    Map<String, int[]> slownikB =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    Map<String, int[]> slownikC =
        new HashMap<String, int[]>() {
          {
            put("a", new int[] {2, 3, 5});
            put("b", new int[] {-3, 7, 1});
            put("c", new int[] {-8, -4, 3});
            put("x", new int[] {11, 2, 7});
          }
        };

    assert !czyIdentyczneV1(slownikC, slownikB);
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }
}

