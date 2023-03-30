/*
Tytul: Macierz z identycznymi wierszami, skladajacymi sie z liczb od 0 do b.
Tresc: Otrzymujesz dwie liczby naturalne, a i b. Stworz macierz, skladajaca sie z a identycznych wierszy, ktore skladaja sie z liczb od 0 do b.
Dane wejsciowe: Dwie liczby naturalne, a i b.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona macierz: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

*/
import java.util.*;

public class Main {
  // Otrzymjesz dwie liczby, a oraz b. Stworz macierz a
  // identycznych wierszy skladajacych sie z liczb od 0 do b.

  public static ArrayList<ArrayList<Integer>> macierz(int a, int b) {

    ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>>();
    ArrayList<Integer> wiersz = new ArrayList<Integer>();

    for (int i = 0; i <= b; i++) {
      wiersz.add(i);
    }

    for (int i = 0; i < a; i++) {
      macierz.add(wiersz);
    }

    return new ArrayList<ArrayList<Integer>>(macierz);
  }

  public static void test1() {
    ArrayList<ArrayList<Integer>> wynik =
        new ArrayList<ArrayList<Integer>>(
            Arrays.asList(
                new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4, 5)),
                new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4, 5)),
                new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4, 5))));
    int a = 3;
    int b = 5;
    assert wynik.equals(macierz(a, b));
  }

  public static void test2() {
    ArrayList<ArrayList<Integer>> wynik =
        new ArrayList<ArrayList<Integer>>(
            Arrays.asList(
                new ArrayList<Integer>(Arrays.asList(0, 1, 2)),
                new ArrayList<Integer>(Arrays.asList(0, 1, 2))));
    int a = 2;
    int b = 2;
    assert wynik.equals(macierz(a, b));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

