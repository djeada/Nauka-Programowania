/*
ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

* obie są posortowane rosnąco,
* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
4.5
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie posortowane listy rownej
  // dlugosci. Znajdz ich mediane.

  // Zlozonosc obliczeniowa O(m + n)
  // Zlozonosc pamieciowa O(1)
  public static double mediana(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    int i = 0;
    int j = 0;
    int n = listaA.size();
    int m = listaB.size();
    double m1 = -1;
    double m2 = -1;

    for (int licznik = 0; licznik <= (n + m) / 2; licznik++) {
      if ((m + n) % 2 == 0) {
        m2 = m1;
      }

      if (i != n && j != m) {
        m1 = (listaA.get(i) > listaB.get(j)) ? listaB.get(j++) : listaA.get(i++);
      } else if (i < n) {
        m1 = listaA.get(i++);
      } else {
        m1 = listaB.get(j++);
      }
    }

    if ((m + n) % 2 == 1) {
      return m1;
    }

    return (m1 + m2) / 2.00;
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(2, 4, 7));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(3, 5, 9));

    double wynik = 4.5;
    assert mediana(listaA, listaB) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

