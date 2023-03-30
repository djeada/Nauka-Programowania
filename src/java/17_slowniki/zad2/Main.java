/*
Tytul: Lista pracownikow z najwiekszymi zyskami.
Tresc: Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwisko pracownika, drugim zysk z transakcji, jaka dany pracownik przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.
Dane wejsciowe: Lista par napisow i liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy:
[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]
zostanie zwrocony napis: “Barnaba Barabash”.

*/
import java.util.*;

public class Main {
  // Otrzymujesz dwie listy. Zbuduj slownik skladajacy sie z kluczy bedacych
  // elementami pierwszej listy i wartosciami bedacymi elementami drugiej listy.
  // Jesli listy sa roznej dlugosci zwroc pusty slownik.
  public static HashMap<Integer, Integer> budujSlownik(
      ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
    HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer>();

    if (listaA.size() != listaB.size()) {
      return new HashMap<Integer, Integer>(slownik);
    }

    for (int i = 0; i < listaA.size(); i++) {
      slownik.put(listaA.get(i), listaB.get(i));
    }

    return new HashMap<Integer, Integer>(slownik);
  }

  public static void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 5, 8));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, 2, -1));
    HashMap<Integer, Integer> wynik =
        new HashMap<Integer, Integer>(
            Map.ofEntries(Map.entry(3, 1), Map.entry(5, 2), Map.entry(8, -1)));

    assert wynik.equals(budujSlownik(listaA, listaB));
  }

  public static void test2() {
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(0, 1));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, 0));
    HashMap<Integer, Integer> wynik =
        new HashMap<Integer, Integer>(Map.ofEntries(Map.entry(0, 1), Map.entry(1, 0)));

    assert wynik.equals(budujSlownik(listaA, listaB));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

