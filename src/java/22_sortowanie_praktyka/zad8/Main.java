import java.util.*;

/*
Otrzymuejsz cyklicznie posortowana liste oraz klucz.
Znajdz indeks pierwszego wystapienia klucza w liscie.
Jesli klucz nie wystepuje w liscie zwroc -1.
*/

public class Main {
  public static int znajdzKlucz(List<Integer> lista, int klucz) {
    int lewo = 0;
    int prawo = lista.size() - 1;

    while (lewo <= prawo) {

      int sr = (lewo + prawo) / 2;

      if (klucz == lista.get(sr)) return sr;

      if (lista.get(sr) <= lista.get(prawo)) {

        if (lista.get(sr) < klucz && klucz <= lista.get(prawo)) lewo = sr + 1;
        else prawo = sr - 1;
      } else {

        if (lista.get(lewo) <= klucz && klucz < lista.get(sr)) prawo = sr - 1;
        else lewo = sr + 1;
      }
    }

    return -1;
  }

  public static void test1() {
    List<Integer> lista = new ArrayList<Integer>(Arrays.asList(27, 31, 32, 3, 5, 9, 10, 15));
    int klucz = 31;
    int oczekiwane = 1;

    assert znajdzKlucz(lista, klucz) == oczekiwane;
  }

  public static void test2() {
    List<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 7, 12, 32, 51, 90, 100, 1, 2));
    int klucz = -5;
    int oczekiwane = -1;

    assert znajdzKlucz(lista, klucz) == oczekiwane;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}
