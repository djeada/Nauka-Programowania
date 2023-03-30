/*
Tytul: Polacz posortowane listy w posortowana liste.
Tresc: Dla otrzymanych dwoch posortowanych list, polacz je w jedna posortowana liste.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinna zostac zwrocona lista: [2, 3, 4, 7, 9].

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie listy. Znajdz elementy
  // ktore nie sa czescia wspolna obu list.

  // Zlozonosc obliczeniowa O(n^2)
  // Zlozonosc pamieciowa O(n)
  public static ArrayList<Integer> roznicaV1(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    ArrayList<Integer> wynik = new ArrayList<Integer>();

    for (var liczba : listaA) {
      if (!listaB.contains(liczba)) {
        wynik.add(liczba);
      }
    }

    for (var liczba : listaB) {
      if (!listaA.contains(liczba)) {
        wynik.add(liczba);
      }
    }

    return new ArrayList<Integer>(wynik);
  }

  public static boolean wektoryRowne(ArrayList<Integer> v1, ArrayList<Integer> v2) {
    Collections.sort(v1);
    Collections.sort(v2);
    return v1.equals(v2);
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(9, 2, 5, 4));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(4, 2, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(9, 5, 1));

    assert wektoryRowne(roznicaV1(listaA, listaB), new ArrayList<Integer>(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

