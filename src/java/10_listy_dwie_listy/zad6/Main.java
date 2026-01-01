/*
ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych. Wypisz listę elementów, które występują w obu listach:

* zachowaj **kolejność występowania w pierwszej liście**,
* jeśli element z pierwszej listy występuje w drugiej liście, dodaj go do wyniku,
* jeśli nie ma elementów wspólnych — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[2, 4]
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie listy. Znajdz elementy wystepujace
  // zarowno w pierwszej jak i w drugiej liscie.

  // Zlozonosc obliczeniowa O(n^2)
  // Zlozonosc pamieciowa O(n)
  public static ArrayList<Integer> czescWspolnaV1(
      ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    ArrayList<Integer> wynik = new ArrayList<Integer>();

    for (var liczba : listaA) {
      if (listaB.contains(liczba)) {
        wynik.add(liczba);
      }
    }

    return new ArrayList<Integer>(wynik);
  }

  public static boolean wektoryRowne(ArrayList<Integer> v1, ArrayList<Integer> v2) {
    Collections.sort(v1);
    Collections.sort(v2);
    return v1.equals(v2);
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 6, 2, 7, 9));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(4, 2, 3, 5, 6));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(3, 6, 2));

    assert wektoryRowne(czescWspolnaV1(listaA, listaB), new ArrayList<Integer>(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

