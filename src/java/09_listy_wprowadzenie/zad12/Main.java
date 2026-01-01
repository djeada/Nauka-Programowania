/*
ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

* `kierunek = 0` → rotacja w lewo,
* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* kolejna linia: `kierunek` (0 lub 1)
* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

* Zredukuj `K` przez `K % N`.

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste liczb, kierunek przesuniec (1 odpowiada przesunieciu
  // w prawo, a 0 w lewo) oraz liczbe miejsc o jaka maja zostac przesuniete
  // elementy. Przykladowo dla przesuwania w prawo pierwszy element trafia
  // na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego.
  // Przesun elementy listy w danym kierunku.

  // Zlozonosc czasowa O(n)
  // Zlozonosc pamieciowa O(n)
  public static ArrayList<Integer> rotacjaV1(
      ArrayList<Integer> lista, final String kierunek, int liczba) {
    if (kierunek.equals("prawo")) {
      for (int i = 0; i < liczba; i++) {
        lista.add(0, lista.get(lista.size() - 1));
        lista.remove(lista.size() - 1);
      }
    } else {
      for (int i = 0; i < liczba; i++) {
        lista.add(lista.get(0));
        lista.remove(0);
      }
    }

    return lista;
  }

  public static void test1() {

    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(5, 27, 6, 2, 1, 10, 8));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 2, 1, 10, 8, 5, 27));
    String kierunek = "lewo";
    int liczba = 2;

    assert wynik.equals(rotacjaV1(lista, kierunek, liczba));
  }

  public static void test2() {

    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(9, 9, 42, 47, 5, 6, 19, 7));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 19, 7, 9, 9, 42, 47, 5));
    String kierunek = "prawo";
    int liczba = 3;

    assert wynik.equals(rotacjaV1(lista, kierunek, liczba));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

