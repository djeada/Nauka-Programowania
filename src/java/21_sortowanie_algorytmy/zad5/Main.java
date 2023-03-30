/*
Tytul: Sortowanie szybkie.
Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania szybkiego.
1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Wybierz element rozdzielajacy, nazywany pivotem.
3. Podziel liste na trzy czesci: elementy mniejsze od pivota, pivot oraz elementy wieksze od pivota.
4. Wywolaj rekurencyjnie sortowanie szybkie dla czesci z elementami mniejszymi od pivota i wiekszymi od pivota.
5. Scal posortowane czesci listy w jedna posortowana liste.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/
import java.util.*;

public class Main {

  public static void sortuj(ArrayList<Integer> lista) {
    _sortuj(lista, 0, lista.size() - 1);
  }

  public static void _sortuj(ArrayList<Integer> lista, int indeksPoczatkowy, int indeksKoncowy) {

    var indeks = rozdziel(lista, indeksPoczatkowy, indeksKoncowy);

    if (indeksPoczatkowy < indeks - 1) {
      _sortuj(lista, indeksPoczatkowy, indeks - 1);
    }

    if (indeksKoncowy > indeks) {
      _sortuj(lista, indeks, indeksKoncowy);
    }
  }

  public static int rozdziel(ArrayList<Integer> lista, int lewyIndeks, int prawyIndeks) {
    var piwot = lista.get(lewyIndeks);

    while (lewyIndeks <= prawyIndeks) {

      while (lista.get(lewyIndeks) < piwot) {
        lewyIndeks++;
      }
      while (lista.get(prawyIndeks) > piwot) {
        prawyIndeks--;
      }

      if (lewyIndeks <= prawyIndeks) {
        var tmp = lista.get(lewyIndeks);
        lista.set(lewyIndeks, lista.get(prawyIndeks));
        lista.set(prawyIndeks, tmp);

        lewyIndeks++;
        prawyIndeks--;
      }
    }
    return lewyIndeks;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    sortuj(lista);
    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

