import java.util.*;

public class Main {
  public static void sortuj(ArrayList<Integer> lista) {

    for (int i = 1; i < lista.size(); i++) {
      var klucz = lista.get(i);
      var j = i - 1;

      while (j >= 0 && lista.get(j) > klucz) {
        lista.set(j + 1, lista.get(j));
        j--;
      }

      lista.set(j + 1, klucz);
    }
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
