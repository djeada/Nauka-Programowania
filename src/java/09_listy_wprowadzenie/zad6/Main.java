/*
Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.
Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy, skladajacej sie z nieuporzadkowanych
  // kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego,
  // znajdz brakujacy element.

  public static int sumaCiaguArt(ArrayList<Integer> lista) {
    int min = Collections.min(lista);
    int maks = Collections.max(lista);
    return (lista.size() + 1) * (min + maks) / 2;
  }

  public static int znajdzBrakujacyElement(ArrayList<Integer> lista) {

    int suma = 0;

    for (var liczba : lista) {
      suma += liczba;
    }

    int sumaPrzedzialu = sumaCiaguArt(lista);

    return sumaPrzedzialu - suma;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 8, 4, 10, 14, 2));
    int wynik = 12;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 4, 5, 6));
    int wynik = 3;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

