/*
Tytul: Liczba mniejsza od najwiekszej i wieksza od wszystkich pozostalych.
Tresc: Otrzymujesz liste liczb naturalnych. Znajdz najwieksza i druga co do wielkosci liczbe w liscie, a nastepnie oblicz srednia arytmetyczna tych dwoch liczb i zwroc ja jako liczbe zmiennoprzecinkowa.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba zmiennoprzecinkowa oznaczajaca srednia arytmetyczna najwiekszej i drugiej co do wielkosci liczby z listy.
Przyklad:
Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostac zwrocona liczba 8.0.

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy liczb naturalnych, znajdz elemnt
  // dominujacy. Element dominujacy to element, ktorego liczba
  // wystapien w liscie jest wieksza niz polowa dlugosci listy.
  // Jesli lista nie ma elementu dominujacego, zwroc -1.

  public static int elementDominujacyV1(ArrayList<Integer> lista) {
    int n = lista.size();

    for (int i = 0; i <= n / 2; i++) {
      int licznik = 1;
      for (int j = i + 1; j < n; j++) {
        if (lista.get(j) == lista.get(i)) {
          licznik++;
        }
      }

      if (licznik > n / 2) {
        return lista.get(i);
      }
    }

    return -1;
  }

  public static int elementDominujacyV2(ArrayList<Integer> lista) {

    HashMap<Integer, Integer> histo = new HashMap<Integer, Integer>();

    for (var liczba : lista) {
      if (histo.containsKey(liczba)) histo.put(liczba, histo.get(liczba) + 1);
      else histo.put(liczba, 1);
    }

    for (Map.Entry<Integer, Integer> para : histo.entrySet()) {
      if (para.getValue() > lista.size() / 2) {
        return para.getKey();
      }
    }

    return -1;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 7, 4, 4, 2));
    int wynik = 4;
    assert elementDominujacyV1(lista) == wynik;
    assert elementDominujacyV2(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 4, 5, 6));
    int wynik = -1;
    assert elementDominujacyV1(lista) == wynik;
    assert elementDominujacyV2(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

