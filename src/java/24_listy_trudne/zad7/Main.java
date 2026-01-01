/*
ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.

### Wejście

* 1 linia: lista wysokości `H`

### Wyjście

* 1 linia: jedna liczba naturalna — ilość wody

### Przykład

**Wejście:**

```
[3, 0, 1, 0, 2]
```

**Wyjście:**

```
5
```

*/
import java.util.*;

public class Main {
  // Oblicza ile wody może zgromadzić się między słupkami
  // Złożoność czasowa: O(n) gdzie n to liczba słupków
  // Złożoność pamięciowa: O(n) - tablice pomocnicze
  public static int ileWodyV1(ArrayList<Integer> slupki) {
    int n = slupki.size();
    int woda = 0;

    ArrayList<Integer> lewy = new ArrayList<Integer>();
    lewy.add(Integer.MIN_VALUE);

    for (int i = 0; i < n; i++) lewy.add(Math.max(lewy.get(i), slupki.get(i)));

    int prawy = Integer.MIN_VALUE;

    for (int i = n - 1; i >= 0; i--) {
      prawy = Math.max(prawy, slupki.get(i));

      if (Math.min(lewy.get(i), prawy) > slupki.get(i))
        woda += Math.min(lewy.get(i), prawy) - slupki.get(i);
    }

    return woda;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(3);
    lista.add(0);
    lista.add(1);
    lista.add(0);
    lista.add(2);
    int wynik = 5;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(9);
    lista.add(2);
    lista.add(3);
    lista.add(9);
    lista.add(0);
    lista.add(2);
    int wynik = 15;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(1);
    int wynik = 0;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

