/*
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy skladajacej sie z nieparzystej
  // liczby elementow znajdz element bez pary. Przez pary
  // elementow rozumiemy tutaj elementy o rownej wartosci.

  // Zlozonosc czasowa O(n)
  // Zlozonosc pamieciowa O(n)
  public static int elementBezParyV1(ArrayList<Integer> lista) {
    ArrayList<Integer> pom = new ArrayList<Integer>();

    for (var liczba : lista) {
      if (pom.contains(liczba)) {
        pom.remove(liczba);
      } else {
        pom.add(liczba);
      }
    }

    return pom.get(0);
  }

  // Zlozonosc czasowa O(n)
  // Zlozonosc pamieciowa O(n)
  public static int elementBezParyV2(ArrayList<Integer> lista) {
    int wynik = 0;

    for (var liczba : lista) {
      wynik ^= liczba;
    }

    return wynik;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
    int wynik = 7;
    assert elementBezParyV1(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
    int wynik = 7;
    assert elementBezParyV2(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

