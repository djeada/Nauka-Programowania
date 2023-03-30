/*
Tytul: Sortowanie przez wybieranie.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wybieranie. Znajdz najwiekszy element w liscie i zapisz go do zmiennej. Nastepnie znajdz najmniejszy element w pozostalej czesci listy i zamien go z pierwszym elementem nieposortowanej czesci. Powtarzaj operacje, az lista bedzie posortowana.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/
import java.util.*;

public class Main {

  public static void sortuj(ArrayList<Integer> lista) {
    for (int i = 0; i < lista.size() - 1; i++) {
      var i_min = i;
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(j) < lista.get(i_min)) i_min = j;

        var temp = lista.get(i);
        lista.set(i, lista.get(i_min));
        lista.set(i_min, temp);
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

