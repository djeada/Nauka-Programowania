import java.util.*;

public class GlobalMembers {
  public static void sortuj(ArrayList < Integer > lista) {

    for (int i = 0; i < lista.size(); i++) {
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(i) > lista.get(j)) {
          var temp = lista.get(i);
          lista.set(i, lista.get(j));
          lista.set(j, temp);
        }
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