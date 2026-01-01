/*
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy znajdz liczbe mniejsza
  // od najwiekszej liczby z listy i jednoczesnie
  // wieksza od wszystkich pozostalych.
  public static double wieksza(ArrayList<Integer> lista) {

    if (lista.isEmpty()) {
      return 0.00;
    }

    if (lista.size() == 1) {
      return lista.get(0) - 1;
    }

    int maks = Integer.MIN_VALUE;
    int maks2 = Integer.MIN_VALUE;

    for (var liczba : lista) {

      if (liczba > maks) {
        maks2 = maks;
        maks = liczba;
      } else if (liczba > maks2) {
        maks2 = liczba;
      }
    }

    return (maks + maks2) / 2.00;
  }

  public static void main(String[] args) {

    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    System.out.print(wieksza(lista));
    System.out.print("\n");

    lista = new ArrayList<Integer>(Arrays.asList(3, -2, 4, 9, -3, -40, 8, 5, -7, -1));
    System.out.print(wieksza(lista));
    System.out.print("\n");
  }
}

