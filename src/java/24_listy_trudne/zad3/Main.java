/*
Tytul: Minimalny iloczyn.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najmniejszy iloczyn dla trzech liczb wybranych z listy. Jesli lista sklada sie z mniej niz trzech liczb, zwroc iloczyn wszystkich elementow listy.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy: [3, -1, -3, 2, 9, 4], powinna zostac zwrocona liczba: -108.

*/
import java.util.*;

public class Main {

  public static int minIloczynV1(ArrayList<Integer> lista) {

    int n = lista.size();

    if (n <= 2) throw new IllegalArgumentException("Lista musi miec co najmniej 3 elementy.");

    Collections.sort(lista);

    return Math.min(
        lista.get(n - 1) * lista.get(n - 2) * lista.get(0),
        lista.get(0) * lista.get(1) * lista.get(2));
  }

  public static int minIloczynV2(ArrayList<Integer> lista) {

    int n = lista.size();

    if (n <= 2) throw new IllegalArgumentException("Lista musi miec co najmniej 3 elementy.");

    ArrayList<Integer> maksLewo = new ArrayList<>();
    ArrayList<Integer> maksPrawo = new ArrayList<>();
    ArrayList<Integer> minLewo = new ArrayList<>();
    ArrayList<Integer> minPrawo = new ArrayList<>();

    int minimum = Integer.MAX_VALUE;
    int maksimum = Integer.MIN_VALUE;

    for (int i = 0; i < n; i++) {
      minLewo.add(minimum);
      maksLewo.add(maksimum);

      minimum = Math.min(minimum, lista.get(i));
      maksimum = Math.max(maksimum, lista.get(i));
    }

    minimum = Integer.MAX_VALUE;
    maksimum = Integer.MIN_VALUE;

    for (int i = n - 1; i >= 0; i--) {
      minPrawo.add(minimum);
      maksPrawo.add(maksimum);

      minimum = Math.min(minimum, lista.get(i));
      maksimum = Math.max(maksimum, lista.get(i));
    }

    int wynik = Integer.MAX_VALUE;

    for (int i = 0; i < n - 2; i++)
      wynik =
          Math.min(
              wynik,
              Math.min(
                  lista.get(i + 1) * minLewo.get(i + 1) * minPrawo.get(i + 1),
                  lista.get(i + 1) * minLewo.get(i + 1) * maksPrawo.get(i + 1),
                  lista.get(i + 1) * maksLewo.get(i + 1) * minPrawo.get(i + 1),
                  lista.get(i + 1) * maksLewo.get(i + 1) * maksPrawo.get(i + 1)));

    return wynik;
  }

  public static int minIloczynV3(ArrayList<Integer> lista) {

    int n = lista.size();

    if (n <= 2) throw new IllegalArgumentException("Lista musi miec co najmniej 3 elementy.");

    int min1 = Integer.MAX_VALUE;
    int min2 = Integer.MAX_VALUE;
    int min3 = Integer.MAX_VALUE;
    int maks1 = Integer.MIN_VALUE;
    int maks2 = Integer.MIN_VALUE;

    for (int i = 0; i < n; i++) {

      if (lista.get(i) < min1) {
        min3 = min2;
        min2 = min1;
        min1 = lista.get(i);
      } else if (lista.get(i) < min2) {
        min3 = min2;
        min2 = lista.get(i);
      } else if (lista.get(i) < min3) min3 = lista.get(i);

      if (lista.get(i) > maks1) {
        maks2 = maks1;
        maks1 = lista.get(i);
      } else if (lista.get(i) > maks2) maks2 = lista.get(i);
    }

    return Math.min(maks1 * maks2 * min1, min1 * min2 * min3);
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<>();
    lista.add(3);
    lista.add(-1);
    lista.add(-3);
    lista.add(2);
    lista.add(9);
    lista.add(4);
    int wynik = -108;

    assert (minIloczynV1(lista) == wynik);
    assert (minIloczynV2(lista) == wynik);
    assert (minIloczynV3(lista) == wynik);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<>();
    lista.add(3);
    lista.add(2);
    lista.add(1);
    lista.add(7);
    lista.add(8);
    int wynik = 6;

    assert (minIloczynV1(lista) == wynik);
    assert (minIloczynV2(lista) == wynik);
    assert (minIloczynV3(lista) == wynik);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<>();
    lista.add(1);
    lista.add(20);
    lista.add(2);
    lista.add(-2);
    lista.add(-4);
    lista.add(-3);
    int wynik = -160;

    assert (minIloczynV1(lista) == wynik);
    assert (minIloczynV2(lista) == wynik);
    assert (minIloczynV3(lista) == wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }
}

