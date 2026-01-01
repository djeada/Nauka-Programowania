/*
ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**

### Przykład

**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanych dwoch list wypisz na przemian elemnty pierwszej
  // i drugiej listy. Jesli listy nie sa rownej dlugosci, po wyczerpaniu
  // elementow krotszej listy, wypisuj tylko elementy dluzszej listy.

  public static void wypisz(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    int n = listaA.size() < listaB.size() ? listaA.size() : listaB.size();

    for (int i = 0; i < n; i++) {
      System.out.print(listaA.get(i));
      System.out.print(", ");
      System.out.print(listaB.get(i));
      System.out.print(", ");
    }

    for (int i = n; i < listaA.size(); i++) {
      System.out.print(listaA.get(i));
      System.out.print(", ");
    }

    for (int i = n; i < listaB.size(); i++) {
      System.out.print(listaB.get(i));
      System.out.print(", ");
    }
  }

  public static void main(String[] args) {

    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(5, 3, 7, 2));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, -2, 3));

    wypisz(listaA, listaB);
  }
}

