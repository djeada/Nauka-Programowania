/*
ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

*/
import java.util.*;

public class Main {
  public static ArrayList<Integer> najdluzszyNaprzemiennyPodciagV1(ArrayList<Integer> lista) {
    if (lista.isEmpty()) return new ArrayList<Integer>();

    int n = lista.size();

    int dlugoscMaks = 1;
    int indeksKoncowy = 0;
    int dlugosc = 1;

    for (int i = 0; i < n; i++) {
      if (lista.get(i) * lista.get(i + 1) < 0) {
        dlugosc++;

        if (dlugosc > dlugoscMaks) {
          dlugoscMaks = dlugosc;
          indeksKoncowy = i + 1;
        }
      } else dlugosc = 1;
    }

    ArrayList<Integer> wynik =
        new ArrayList<Integer>(lista.subList(indeksKoncowy - dlugoscMaks + 1, indeksKoncowy + 1));

    if (wynik.size() > 1) return wynik;

    return new ArrayList<Integer>();
  }

  // Testy Poprawnosci
  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, -2, 6, 4, -3, 2, -4, -3));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(4, -3, 2, -4));

    assert (najdluzszyNaprzemiennyPodciagV1(lista).equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));
    ArrayList<Integer> wynik = new ArrayList<Integer>();

    assert (najdluzszyNaprzemiennyPodciagV1(lista).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

