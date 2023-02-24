import java.util.*;

/*
Otrzymujesz liste liczb. Znajdz jej zbior potegowy, czyli zbior wszystkich jej
podzbiorow.
*/

public class Main {

  public static (ArrayList<Integer> zbiorPotegowy(ArrayList<Integer> lista) {
    int N = (int) Math.pow(2, lista.size());
    ArrayList<Integer> zbiorPotegowy = new ArrayList<Integer>();

    for (int i = 0; i < N; i++) {
      ArrayList<Integer> podzbior = new ArrayList<Integer>();

      for (int j = 0; j < lista.size(); j++) {
        if ((i & (1 << j)) != 0)
          podzbior.add(lista.get(j));
      }

      zbiorPotegowy.add(podzbior);
    }

    return zbiorPotegowy;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(2);
    lista.add(1);

    ArrayList<Integer> wynik = new ArrayList<Integer>();
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 1, 2)));
    wynik.add(new ArrayList<Integer>(Arrays.asList()));
    wynik.add(new ArrayList<Integer>(Arrays.asList(1, 1)));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(5);
    lista.add(3);

    ArrayList<Integer> wynik = new ArrayList<Integer>();
    wynik.add(new ArrayList<Integer>(Arrays.asList(3)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(3, 5)));
    wynik.add(new ArrayList<Integer>(Arrays.asList(5)));
    wynik.add(new ArrayList<Integer>(Arrays.asList()));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();

    ArrayList<Integer> wynik = new ArrayList<Integer>();
    wynik.add(new ArrayList<Integer>(Arrays.asList()));

    assert(zbiorPotegowy(lista).equals(wynik));
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }

}

