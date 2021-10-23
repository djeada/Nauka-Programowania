import java.util.*;

public class Main {

  public static void sortuj(ArrayList < Integer > lista) {
    _sortuj(lista, 0, lista.size() - 1);
  }

  public static void _sortuj(ArrayList < Integer > lista, int indeksPoczatkowy, int indeksKoncowy) {

    var indeks = rozdziel(lista, indeksPoczatkowy, indeksKoncowy);

    if (indeksPoczatkowy < indeks - 1) {
      _sortuj(lista, indeksPoczatkowy, indeks - 1);
    }

    if (indeksKoncowy > indeks) {
      _sortuj(lista, indeks, indeksKoncowy);
    }
  }

  public static int rozdziel(ArrayList < Integer > lista, int lewyIndeks, int prawyIndeks) {
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
    ArrayList < Integer > lista = new ArrayList < Integer > (Arrays.asList(4, 2, 5, 3, 1));
    ArrayList < Integer > wynik = new ArrayList < Integer > (Arrays.asList(1, 2, 3, 4, 5));

    sortuj(lista);
    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();

  }
}

