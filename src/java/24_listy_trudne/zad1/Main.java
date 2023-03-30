/*
Tytul: Najdluzszy ciag jedynek.
Tresc: Otrzymujesz liste skladajaca sie wylacznie z zer i jedynek. Znajdz indeks zera, ktore po zamianie na jedynke daloby najdluzszy ciag jedynek. Jesli lista sklada sie wylacznie z zer lub wylacznie z jedynek, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1], powinna zostac zwrocona liczba: 7.

*/
import java.util.*;

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
    assert (wynik == oczekiwane);
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
    assert (wynik == oczekiwane);
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
    assert (wynik == oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

