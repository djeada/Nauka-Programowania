/*
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanych dwoch list zwroc liste powstala poprzez:
  // a) dostawienie drugiej listy na koniec pierwszej listy;
  public static ArrayList<Integer> dostaw(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    ArrayList<Integer> wynik = new ArrayList<Integer>(listaA);

    for (var liczba : listaB) {
      wynik.add(liczba);
    }

    return new ArrayList<Integer>(wynik);
  }

  // wstawienie elemntow o indeksach parzystych z drugiej
  // listy na odpowiadajace im indeksy pierwszej listy.
  public static ArrayList<Integer> podmien(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    ArrayList<Integer> wynik = new ArrayList<Integer>(listaA);
    for (int i = 0; i < wynik.size(); i += 2) {
      wynik.set(i, listaB.get(i));
    }

    return new ArrayList<Integer>(wynik);
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(7, 5, 0));

    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6, 7, 5, 0));
    assert wynik.equals(dostaw(listaA, listaB));
  }

  public static void test2() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(7, 5, 0));

    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(7, 8, 0, 6));
    assert wynik.equals(podmien(listaA, listaB));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

