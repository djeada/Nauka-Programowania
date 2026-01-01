/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste n wspolczynnikow wielomianu postaci
  // a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
  // Oblicz wartosc wspolczynnikow wielomianu po
  // przemnozeniu przez liczbe x.
  
  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static ArrayList<Integer> iloczyn(ArrayList<Integer> lista, int x) {

    ArrayList<Integer> wynik = new ArrayList<Integer>();

    for (var liczba : lista) {
      wynik.add(liczba * x);
    }

    return new ArrayList<Integer>(wynik);
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 2, 1));
    int x = 2;
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 4, 2));
    assert wynik.equals(iloczyn(lista, x));
  }

  public static void main(String[] args) {

    test1();
  }
}

