/*
Tytul: Sortowanie przez scalanie.
Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania przez scalanie.
1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Podziel liste na dwie rowne (lub prawie rowne) czesci.
3. Wywolaj rekurencyjnie sortowanie przez scalanie dla obu czesci listy.
4. Scal obie posortowane czesci listy w jedna posortowana liste.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/
import java.util.*;

public class Main {

  public static ArrayList<Integer> sortuj(ArrayList<Integer> lista) {
    if (lista.size() <= 1) {
      return lista;
    }
    ArrayList<Integer> posortowana = new ArrayList<Integer>();

    ArrayList<Integer> lewaLista = new ArrayList<Integer>();
    ArrayList<Integer> prawaLista = new ArrayList<Integer>();
    int middle = lista.size() / 2;

    for (int i = 0; i < lista.size(); i++) {
      if (i < middle) {
        lewaLista.add(lista.get(i));
      } else {
        prawaLista.add(lista.get(i));
      }
    }
    lewaLista = sortuj(lewaLista);
    prawaLista = sortuj(prawaLista);

    posortowana = polacz(lewaLista, prawaLista);
    return posortowana;
  }

  public static ArrayList<Integer> polacz(
      ArrayList<Integer> lewaLista, ArrayList<Integer> prawaLista) {
    ArrayList<Integer> polaczonaLista = new ArrayList<Integer>();
    while (lewaLista.size() > 0 || prawaLista.size() > 0) {
      if (lewaLista.size() > 0 && prawaLista.size() > 0) {
        if (lewaLista.get(0) < prawaLista.get(0)) {
          polaczonaLista.add(lewaLista.get(0));
          lewaLista.remove(0);
        } else {
          polaczonaLista.add(prawaLista.get(0));
          prawaLista.remove(0);
        }
      } else if (lewaLista.size() > 0) {
        polaczonaLista.add(lewaLista.get(0));
        lewaLista.remove(0);
      } else if (prawaLista.size() > 0) {
        polaczonaLista.add(prawaLista.get(0));
        prawaLista.remove(0);
      }
    }
    return polaczonaLista;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    lista = sortuj(lista);
    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

