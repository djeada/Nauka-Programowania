/*
Tytul: Macierz z parami elementow odpowiadajacych sobie z dwoch list.
Tresc: Dla otrzymanych dwoch list, stworz dwukolumnowa macierz, ktorej pierwsza kolumna sklada sie z elementow pierwszej listy, a druga kolumna z elementow drugiej listy. Jesli otrzymane listy nie sa rownej dlugosci, zwroc pusta macierz.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista list liczb naturalnych lub pusta macierz (w przypadku nierownych dlugosci list).
Przyklad:
Dla otrzymanych dwoch list: [3, 5, 2] oraz [2, 8, 1], powinna zostac zwrocona macierz: [[3, 2], [5, 8], [2, 1]

*/
import java.util.*;

public class Main {
  // Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca
  // sie z liczby kolumn i wierszy rownej otrzymanej liczbie
  // ktorej kazdy element jest iloczynem jego wspolrzednych.

  public static ArrayList<ArrayList<Integer>> macierz(int n) {

    ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>>();
    macierz.ensureCapacity(n);

    for (int i = 0; i < n; i++) {
      ArrayList<Integer> wiersz = new ArrayList<Integer>();
      for (int j = 0; j < n; j++) {
        wiersz.add(i * j);
      }
      macierz.add(wiersz);
    }

    return new ArrayList<ArrayList<Integer>>(macierz);
  }

  public static void test1() {
    int n = 4;
    ArrayList<ArrayList<Integer>> wynik =
        new ArrayList<ArrayList<Integer>>(
            Arrays.asList(
                new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0)),
                new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3)),
                new ArrayList<Integer>(Arrays.asList(0, 2, 4, 6)),
                new ArrayList<Integer>(Arrays.asList(0, 3, 6, 9))));
    assert wynik.equals(macierz(n));
  }

  public static void main(String[] args) {
    test1();
  }
}

