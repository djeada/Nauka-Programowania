/*
Tytul: Polaczenie dwoch list.
Tresc: Dla otrzymanych dwoch list, zwroc liste, ktora powstala poprzez:
a) Dostawienie drugiej listy na koniec pierwszej listy.
b) Wstawienie elementow o indeksach parzystych z drugiej listy na odpowiadajace im indeksy pierwszej listy.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanych list [1, 2, 3] oraz [4, 5, 6], w podpunkcie a) powinna zostac zwrocona lista: [1, 2, 3, 4, 5, 6].
W podpunkcie b) powinna zostac zwrocona lista: [4, 2, 6, 3].

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie posortowane listy rownej
  // dlugosci. Znajdz ich mediane.

  // Zlozonosc obliczeniowa O(m + n)
  // Zlozonosc pamieciowa O(1)
  public static double mediana(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    int i = 0;
    int j = 0;
    int n = listaA.size();
    int m = listaB.size();
    double m1 = -1;
    double m2 = -1;

    for (int licznik = 0; licznik <= (n + m) / 2; licznik++) {
      if ((m + n) % 2 == 0) {
        m2 = m1;
      }

      if (i != n && j != m) {
        m1 = (listaA.get(i) > listaB.get(j)) ? listaB.get(j++) : listaA.get(i++);
      } else if (i < n) {
        m1 = listaA.get(i++);
      } else {
        m1 = listaB.get(j++);
      }
    }

    if ((m + n) % 2 == 1) {
      return m1;
    }

    return (m1 + m2) / 2.00;
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(2, 4, 7));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(3, 5, 9));

    double wynik = 4.5;
    assert mediana(listaA, listaB) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

