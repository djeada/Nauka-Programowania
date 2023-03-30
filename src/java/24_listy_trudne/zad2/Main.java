/*
Tytul: Przesun zera.
Tresc: Otrzymujesz liste liczb calkowitych. Przesun wszystkie zera na koniec listy.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0], powinna zostac zwrocona lista: [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0].

*/
import java.util.*;

public class Main {

  public static void zeraV1(ArrayList<Integer> lista) {
    int N = lista.size();

    for (int i = 0; i < N; i++) {
      if (lista.get(i) == 0) {
        int j = i + 1;

        while (lista.get(j) == 0 && j < N) j++;

        Collections.swap(lista, i, j);
      }
    }
  }

  public static void test1() {
    ArrayList<Integer> lista =
        new ArrayList<Integer>(Arrays.asList(0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0));
    ArrayList<Integer> wynik =
        new ArrayList<Integer>(Arrays.asList(1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));

    zeraV1(lista);
    assert (lista.equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

