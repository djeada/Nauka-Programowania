
/*
Otrzymujesz dwie listy binarne, A oraz B.
Znajdz dlugosc takich podciagow obu list o rownej sumie, ktorych suma jest
najwieksza. Podciagi nie musza byc takie same.
*/

public class Main {

  public static int znajdzPodciagV1(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

    if (listaA.size() != listaB.size())
      throw new IllegalArgumentException("Listy musza byc rownej dlugosci.");

    HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer>();
    slownik.put(0, -1);

    int wynik = 0;
    int sumaA = 0;
    int sumaB = 0;

    for (int i = 0; i <= listaA.size(); i++) {
      sumaA += listaA.get(i);
      sumaB += listaB.get(i);

      int roznica = sumaA - sumaB;

      if (!slownik.containsKey(roznica)) slownik.put(roznica, i);
      else wynik = Math.max(wynik, i - slownik.get(roznica));
    }

    return wynik;
  }

  // Testy Poprawnosc
  void test1() {
    ArrayList<Integer> listaA = new ArrayList<Integer>();
    listaA.add(0);
    listaA.add(0);
    listaA.add(1);
    listaA.add(1);
    listaA.add(1);
    listaA.add(1);

    ArrayList<Integer> listaB = new ArrayList<Integer>();
    listaB.add(0);
    listaB.add(1);
    listaB.add(1);
    listaB.add(0);
    listaB.add(1);
    listaB.add(0);

    int wynik = 5;

    assert (znajdzPodciagV1(listaA, listaB) == wynik);
  }

  void test2() {
    ArrayList<Integer> listaA = new ArrayList<Integer>();
    listaA.add(0);
    listaA.add(0);
    listaA.add(1);
    listaA.add(1);

    ArrayList<Integer> listaB = new ArrayList<Integer>();
    listaB.add(0);
    listaB.add(1);
    listaB.add(1);
    listaB.add(0);
    listaB.add(1);
    listaB.add(0);

    try {
      znajdzPodciagV1(listaA, listaB);
      assert (false);
    } catch (Exception e) {
      assert (true);
    }
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}
