/*
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

*/
import java.util.*;

public class Main {
  // Znajdz takie pary elementow w liscie, ktorych suma jest rowna liczbie.
  // Element nie moze byc w parze sam ze soba.

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

  public static ArrayList<Pair<Integer, Integer>> znajdzParyV1(ArrayList<Integer> lista, int suma) {

    ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>();

    for (int i = 0; i < lista.size(); i++) {
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(i) + lista.get(j) == suma) {
          Pair<Integer, Integer> para = new Pair<Integer, Integer>(lista.get(i), lista.get(j));
          wynik.add(para);
        }
      }
    }

    return new ArrayList<Pair<Integer, Integer>>(wynik);
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(0, 4, 5, 6, 2, 9, 2, 3));
    ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>();
    wynik.add(new Pair<Integer, Integer>(0, 5));
    wynik.add(new Pair<Integer, Integer>(2, 3));
    wynik.add(new Pair<Integer, Integer>(2, 3));

    int suma = 5;

    assert wynik.equals(znajdzParyV1(lista, suma));
  }

  public static void main(String[] args) {

    test1();
  }
}

