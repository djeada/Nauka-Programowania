/*
Tytul: Dodawanie i odejmowanie macierzy.
Tresc: Otrzymujesz dwie macierze o tych samych wymiarach. Zwroc dwie macierze bedace:
a) wynikiem dodawania otrzymanych macierzy
b) wynikiem odejmowania drugiej macierzy od pierwszej.
Dane wejsciowe: Dwie listy list liczb naturalnych.
Dane wyjsciowe: Dwie listy list liczb naturalnych.
Przyklad:
Dla otrzymanych dwoch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinny zostac zwrocone nastepujace macierze:
a) [[6, -1], [-1, 7]] - wynik dodawania
b) [[-4, 5], [-3, -7]] - wynik odejmowania drugiej macierzy od pierwszej.

*/
import java.util.*;

public class Main {
  // Dla otrzymanych dwoch list, stworz dwu-kolumnowa macierz,
  // ktorej pierwsza kolumna sklada sie z elementow pierwszej
  // listy, a druga drugiej. Jesli otrzymane listy nie sa rownej
  // dlugosci zwroc pusta macierz.
  private static class Pair<T1, T2> {
    public T1 first;
    public T2 second;

    public Pair(T1 firstValue, T2 secondValue) {
      first = firstValue;
      second = secondValue;
    }

    @Override
    public boolean equals(Object o) {
      return (o instanceof Pair)
          && (this.first == ((Pair) o).first)
          && (this.second == ((Pair) o).second);
    }
  }

  public static ArrayList<Pair<Integer, Integer>> macierz(
      ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    ArrayList<Pair<Integer, Integer>> macierz = new ArrayList<Pair<Integer, Integer>>();

    if (listaA.size() != listaB.size()) {
      return new ArrayList<Pair<Integer, Integer>>(macierz);
    }

    int n = listaA.size();
    macierz.ensureCapacity(n);

    for (int i = 0; i < n; i++) {
      macierz.add(new Pair<Integer, Integer>(listaA.get(i), listaB.get(i)));
    }

    return new ArrayList<Pair<Integer, Integer>>(macierz);
  }

  public static void test1() {
    ArrayList<Pair<Integer, Integer>> wynik =
        new ArrayList<Pair<Integer, Integer>>(
            Arrays.asList(
                new Pair<Integer, Integer>(3, 2),
                new Pair<Integer, Integer>(5, 8),
                new Pair<Integer, Integer>(2, 1)));
    ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 5, 2));
    ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(2, 8, 1));
    assert wynik.equals(macierz(listaA, listaB));
  }

  public static void main(String[] args) {
    test1();
  }
}

