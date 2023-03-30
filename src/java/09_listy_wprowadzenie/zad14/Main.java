/*
Tytul: Czy srednia elementow znajduje sie w liscie?
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.
Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.
Przyklad:
Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy skladajacej sie z nieparzystej
  // liczby elementow znajdz element bez pary. Przez pary
  // elementow rozumiemy tutaj elementy o rownej wartosci.

  // Zlozonosc czasowa O(n)
  // Zlozonosc pamieciowa O(n)
  public static int elementBezParyV1(ArrayList<Integer> lista) {
    ArrayList<Integer> pom = new ArrayList<Integer>();

    for (var liczba : lista) {
      if (pom.contains(liczba)) {
        pom.remove(liczba);
      } else {
        pom.add(liczba);
      }
    }

    return pom.get(0);
  }

  // Zlozonosc czasowa O(n)
  // Zlozonosc pamieciowa O(n)
  public static int elementBezParyV2(ArrayList<Integer> lista) {
    int wynik = 0;

    for (var liczba : lista) {
      wynik ^= liczba;
    }

    return wynik;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
    int wynik = 7;
    assert elementBezParyV1(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
    int wynik = 7;
    assert elementBezParyV2(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

