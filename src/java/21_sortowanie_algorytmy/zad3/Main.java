/*
Tytul: Sortowanie przez wstawianie.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wstawianie. Stworz nowa, pusta liste i dodaj do niej pierwszy element listy wejsciowej. Dla kazdego kolejnego elementu znajdz odpowiednie miejsce w posortowanej juz czesci listy i wstaw go tam.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/
import java.util.*;

public class Main {
  public static void sortuj(ArrayList<Integer> lista) {

    for (int i = 1; i < lista.size(); i++) {
      var klucz = lista.get(i);
      var j = i - 1;

      while (j >= 0 && lista.get(j) > klucz) {
        lista.set(j + 1, lista.get(j));
        j--;
      }

      lista.set(j + 1, klucz);
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

