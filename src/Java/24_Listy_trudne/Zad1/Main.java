import java.util.*;

/*
Otrzymujesz tablice skladajaca sie wylacznie z zer i jedynek. Znajdz indeks
zera, ktore po zamianie na jedynke daloby najdluzszy nieprzerwany ciag jedynek.
Zachowanie dla otrzymanej tablicy skladajacej sie z samych zer jest
nieokreslone.
*/

public class Main {
  public static int indeksZera(ArrayList<Integer> lista) {
    int licznikJedynek = 0;
    int licznikZer = 0;

    int indeksZera = -1;
    int poprzedniIndeksZera = -1;

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 1) {
        licznikZer++;
      } else {
        licznikZer = i - poprzedniIndeksZera;
        poprzedniIndeksZera = i;
      }

      if (licznikZer > licznikJedynek) {
        licznikJedynek = licznikZer;
        indeksZera = poprzedniIndeksZera;
      }
    }

    return indeksZera;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(0);
    lista.add(0);
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);

    int oczekiwane = 7;
    int wynik = indeksZera(lista);
    assert(wynik == oczekiwane);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);

    int oczekiwane = -1;
    int wynik = indeksZera(lista);
    assert(wynik == oczekiwane);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);

    int oczekiwane = 1;
    int wynik = indeksZera(lista);
    assert(wynik == oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();

  }
}