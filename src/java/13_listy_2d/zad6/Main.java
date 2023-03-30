/*
Tytul: Zerowanie macierzy.
Tresc: Otrzymujesz liste list liczb naturalnych reprezentujaca macierz. Jesli element macierzy jest rowny zero, zamien wszystkie elementy tej samej kolumny i wiersza na zera.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostac zwrocona macierz: [[1,0,3], [0,0,0], [7,0,9]].

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste par liczb. Liczby w parze reprezentuja poczatek i
  // koniec przedzialu. Niektore przedzialy moga na siebie nachodzic. W takim
  // przypadku polacz je ze soba i zwroc liste niepokrywajacych sie przedzialow.
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

  public static ArrayList<Pair<Integer, Integer>> polaczPrzedzialyV1(
      ArrayList<Pair<Integer, Integer>> lista) {

    Collections.sort(
        lista,
        new Comparator<Pair<Integer, Integer>>() {
          public int compare(Pair<Integer, Integer> p1, Pair<Integer, Integer> p2) {
            return p1.second.compareTo(p2.first);
          }
        });

    int pocz = lista.get(0).first;
    int koniec = lista.get(0).second;
    lista.remove(0);

    ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>();

    for (var para : lista) {

      if (koniec >= para.first) {
        if (koniec < para.second) {
          koniec = para.second;
        }
      } else {

        wynik.add(new Pair<Integer, Integer>(pocz, koniec));
        pocz = para.first;
        koniec = para.second;
      }
    }

    wynik.add(new Pair<Integer, Integer>(pocz, koniec));

    return wynik;
  }

  public static void test1() {
    ArrayList<Pair<Integer, Integer>> lista =
        new ArrayList<Pair<Integer, Integer>>(
            Arrays.asList(
                new Pair<Integer, Integer>(23, 67),
                new Pair<Integer, Integer>(23, 53),
                new Pair<Integer, Integer>(45, 88),
                new Pair<Integer, Integer>(10, 22),
                new Pair<Integer, Integer>(11, 42),
                new Pair<Integer, Integer>(42, 45)));

    ArrayList<Pair<Integer, Integer>> wynik =
        new ArrayList<Pair<Integer, Integer>>(
            Arrays.asList(new Pair<Integer, Integer>(10, 22), new Pair<Integer, Integer>(23, 88)));

    assert wynik.equals(polaczPrzedzialyV1(lista));
  }

  public static void main(String[] args) {
    test1();
  }
}

