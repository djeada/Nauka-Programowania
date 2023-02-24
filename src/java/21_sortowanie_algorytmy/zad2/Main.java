import java.util.*;

public class Main {

  public static void sortuj(ArrayList < Integer > lista) {
    for (int i = 0; i < lista.size() - 1; i++) {
      var i_min = i;
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(j) < lista.get(i_min))
          i_min = j;

        var temp = lista.get(i);
        lista.set(i, lista.get(i_min));
        lista.set(i_min, temp);
      }
    }

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