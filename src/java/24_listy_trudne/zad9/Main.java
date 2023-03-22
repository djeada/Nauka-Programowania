import java.util.*;

/*
Otrzymujesz liste liczb. Znajdz najdluzszy naprzemienny podciag w liscie.
*/

public class Main {
  public static ArrayList<Integer> najdluzszyNaprzemiennyPodciagV1(ArrayList<Integer> lista) {
    if (lista.isEmpty()) return new ArrayList<Integer>();

    int n = lista.size();

    int dlugoscMaks = 1;
    int indeksKoncowy = 0;
    int dlugosc = 1;

    for (int i = 0; i < n; i++) {
      if (lista.get(i) * lista.get(i + 1) < 0) {
        dlugosc++;

        if (dlugosc > dlugoscMaks) {
          dlugoscMaks = dlugosc;
          indeksKoncowy = i + 1;
        }
      } else dlugosc = 1;
    }

    ArrayList<Integer> wynik =
        new ArrayList<Integer>(lista.subList(indeksKoncowy - dlugoscMaks + 1, indeksKoncowy + 1));

    if (wynik.size() > 1) return wynik;

    return new ArrayList<Integer>();
  }

  // Testy Poprawnosci
  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, -2, 6, 4, -3, 2, -4, -3));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(4, -3, 2, -4));

    assert (najdluzszyNaprzemiennyPodciagV1(lista).equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));
    ArrayList<Integer> wynik = new ArrayList<Integer>();

    assert (najdluzszyNaprzemiennyPodciagV1(lista).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}
