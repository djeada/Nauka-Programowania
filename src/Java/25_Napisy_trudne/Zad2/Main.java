import java.util.*;

/*
Dla otrzymanych dwoch napisow, znajdz i usun w pierwszym z nich wystapienia
drugiego.
*/

public class Main {

  public static String usunWystapienia(String napis1, String napis2) {
    String wynik = napis1;

    while (wynik.contains(napis2)) {
      int indeks = wynik.indexOf(napis2);
      wynik = wynik.substring(0, indeks) + wynik.substring(indeks + napis2.length());
    }

    return wynik;
  }

  public static void test1() {
    String napis1 = "Lezy jezy na wiezy";
    String napis2 = "zy";
    String wynik = "Le je na wie";

    assert(usunWystapienia(napis1, napis2).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}