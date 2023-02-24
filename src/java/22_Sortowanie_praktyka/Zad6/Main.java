import java.util.*;

/*
Otrzymujesz liste liczb, skladajaca sie wylacznie z zer i jedynek. Posortuj liste.
*/

public class Main {
  public static void sortuj(ArrayList<Integer> lista) {
    int zera = 0;
    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 0) {
        zera++;
      }
    }

    for (int i = 0; i < zera; i++) {
      lista.set(i, 0);
    }

    for (int i = zera; i < lista.size(); i++) {
      lista.set(i, 1);
    }
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 0, 0, 1, 1, 1, 0));
    ArrayList<Integer> oczekiwane = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 1, 1, 1, 1));

    sortuj(lista);

    assert lista.equals(oczekiwane);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1, 1, 1));
    ArrayList<Integer> oczekiwane = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 1, 1, 1));

    sortuj(lista);

    assert lista.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();

  }
}