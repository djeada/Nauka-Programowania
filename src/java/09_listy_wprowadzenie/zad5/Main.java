/*
ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę liczb całkowitych. Dla każdego podpunktu utwórz **nową listę** na podstawie listy z poprzedniego podpunktu i wypisz ją w jednej linii (przecinki bez spacji):

a) Zwiększ o 1 elementy o **parzystych indeksach** (0,2,4,...).
b) Ustaw na `0` elementy będące **wielokrotnością 3**.
c) Podnieś do kwadratu elementy **mniejsze niż 10**.
d) Oblicz sumę wszystkich elementów listy i wstaw tę sumę na indeksy, które są **liczbami pierwszymi** (2,3,5,7,11,...) — tylko te, które mieszczą się w zakresie listy.
e) Zamień każdy element na **iloczyn wszystkich pozostałych elementów** listy.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Pięć linii (po kolei: a, b, c, d, e), w każdej lista oddzielona przecinkami.

### Przykład

**Wejście:**

```
5
5
7
9
4
2
```

**Wyjście:**

```
6,7,10,4,3
6,7,0,4,3
36,49,0,16,9
36,49,36,36,9
0,0,0,0,0
```

### Uwagi o formatowaniu

* W podpunkcie (d) indeks 0 i 1 nie są pierwsze.
* W podpunkcie (e) jeśli w liście jest `0`, to wiele wyników będzie `0` — to normalne.
* Nie dodawaj przecinków na końcu linii.

*/
import java.util.*;

// Otrzymujesz liste liczb, wykonaj nastepujace polecenia:
// a)Zwieksz o 1 wszystkie elementy stojace na parzystych indeksach.
// b)Wyzeruj wszystkie wielokrotnosci liczby 3.
// c)Podnies do kwadratu wszystkie elementy mniejsze niz 10.
// d)Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
// e)Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.

public class Main {

  public static ArrayList<Integer> zwieksz(ArrayList<Integer> lista) {
    for (int i = 0; i < lista.size(); i++) {
      if (i % 2 == 0) {
        lista.set(i, lista.get(i) + 1);
      }
    }
    return lista;
  }

  public static ArrayList<Integer> wyzeruj(ArrayList<Integer> lista) {

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) % 3 == 0) {
        lista.set(i, 0);
      }
    }
    return lista;
  }

  public static ArrayList<Integer> kwadrat(ArrayList<Integer> lista) {

    for (int i = 0; i < lista.size(); i++) {

      if (lista.get(i) < 10) {
        lista.set(i, (int) Math.pow(lista.get(i), 2));
      }
    }

    return lista;
  }

  public static boolean czyPierwsza(int n) {

    if ((n % 2 == 0 && n != 2) || n < 1) {
      return false;
    }

    for (int i = 3; i <= Math.sqrt((double) n); i += 2) {
      if ((n % i) == 0) {
        return false;
      }
    }

    return true;
  }

  public static ArrayList<Integer> suma(ArrayList<Integer> lista) {
    int suma = 0;
    for (Integer liczba : lista) suma += liczba;

    for (int i = 0; i < lista.size(); i++) {
      if (czyPierwsza(i)) {
        lista.set(i, suma);
      }
    }

    return lista;
  }

  public static ArrayList<Integer> zamien(ArrayList<Integer> lista) {

    ArrayList<Integer> iloczyny = new ArrayList<Integer>();

    for (int i = 0; i < lista.size(); i++) {
      int iloczyn = 1;

      for (int j = 0; j < lista.size(); j++) {
        if (j == i) {
          continue;
        }

        iloczyn *= lista.get(j);
      }

      iloczyny.add(iloczyn);
    }

    return iloczyny;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(4, 5, -6, 4, 10, -11, 3));

    assert wynik.equals(zwieksz(lista));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(0, 5, -7, 4, 0, -11, 2));
    assert wynik.equals(wyzeruj(lista));
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(3, 5, 5, 5, 9, 5, 2));

    assert wynik.equals(suma(lista));
  }

  public static void test4() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    ArrayList<Integer> wynik =
        new ArrayList<Integer>(Arrays.asList(27720, 16632, -11880, 20790, 9240, -7560, 41580));
    assert wynik.equals(zamien(lista));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
  }
}

