/*
Tytul: Znajdz mediane dwoch posortowanych list.
Tresc: Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci. Znajdz ich mediane.
Dane wejsciowe: Dwie listy liczb calkowitych o rownej dlugosci.
Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinno zostac zwrocone: 4.5.

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie listy. Usun z pierwszej listy te
  // elementy, ktore wystepuja rowniez w drugiej liscie.

  // Zlozonosc obliczeniowa O(n^2)
  // Zlozonosc pamieciowa O(n)
  public static ArrayList<Integer> usunCzescWspolnaV1(
      ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    for (int i = 0; i < listaA.size(); i++) {
      if (listaB.contains(listaA.get(i))) {
        listaA.remove(i);
        i--;
      }
    }

    return listaA;
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 6, 2, 7, 9));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(4, 2, 3, 5, 6));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(7, 9));

    assert wynik.equals(usunCzescWspolnaV1(listaA, listaB));
  }

  public static void main(String[] args) {

    test1();
  }
}

