/*
ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości** `(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w osobnej linii jako:
`a b`

Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Wiele linii — po jednej parze na linię.
Jeśli brak par — brak wyjścia.

### Przykład

**Wejście:**

```
5
1
2
4
3
7
5
```

**Wyjście:**

```
1 4
2 3
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy oraz liczby X, znajdz indeksy pierwszej
  // pary elementow listy, ktorych suma jest rowna liczbie X.
  // Jesli w liscie nie ma takiej pary, zwroc pare (-1, -1)

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

  public static Pair<Integer, Integer> sumaDwochV1(ArrayList<Integer> lista, int liczba) {
    int n = lista.size();

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (lista.get(j) + lista.get(i) == liczba) {
          return new Pair<Integer, Integer>(i, j);
        }
      }
    }

    return new Pair<Integer, Integer>(-1, -1);
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 4, 5, 2));
    int liczba = 5;
    Pair<Integer, Integer> wynik = new Pair<Integer, Integer>(0, 2);
    assert sumaDwochV1(lista, liczba).equals(wynik);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(2, -6, 10, 21, 8));
    int liczba = 7;
    Pair<Integer, Integer> wynik = new Pair<Integer, Integer>(-1, -1);
    assert sumaDwochV1(lista, liczba).equals(wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

