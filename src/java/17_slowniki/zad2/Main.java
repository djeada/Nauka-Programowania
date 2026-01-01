/*
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie listy. Zbuduj slownik skladajacy sie z kluczy bedacych
  // elementami pierwszej listy i wartosciami bedacymi elementami drugiej listy.
  // Jesli listy sa roznej dlugosci zwroc pusty slownik.
  
  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static HashMap<Integer, Integer> budujSlownik(
      ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer>();

    if (listaA.size() != listaB.size()) {
      return new HashMap<Integer, Integer>(slownik);
    }

    for (int i = 0; i < listaA.size(); i++) {
      slownik.put(listaA.get(i), listaB.get(i));
    }

    return new HashMap<Integer, Integer>(slownik);
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 5, 8));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, 2, -1));
    HashMap<Integer, Integer> wynik =
        new HashMap<Integer, Integer>(
            Map.ofEntries(Map.entry(3, 1), Map.entry(5, 2), Map.entry(8, -1)));

    assert wynik.equals(budujSlownik(listaA, listaB));
  }

  public static void test2() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(0, 1));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, 0));
    HashMap<Integer, Integer> wynik =
        new HashMap<Integer, Integer>(Map.ofEntries(Map.entry(0, 1), Map.entry(1, 0)));

    assert wynik.equals(budujSlownik(listaA, listaB));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

