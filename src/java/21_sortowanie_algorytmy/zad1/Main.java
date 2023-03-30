/*
Tytul: Sortowanie babelkowe.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania babelkowego. Porownaj sasiednie liczby z listy i zamien je miejscami, jesli pierwsza jest wieksza od drugiej. Powtarzaj operacje, az przejdziesz przez cala liste bez dokonywania zmian.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/
import java.util.*;

public class Main {
  public static void sortuj(ArrayList<Integer> lista) {

    for (int i = 0; i < lista.size(); i++) {
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(i) > lista.get(j)) {
          var temp = lista.get(i);
          lista.set(i, lista.get(j));
          lista.set(j, temp);
        }
      }
    }
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    sortuj(lista);
    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

