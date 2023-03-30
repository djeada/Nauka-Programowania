/*
Tytul: Usun podnapis.
Tresc: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usuniecie wszystkich wystapien drugiego napisu w pierwszym napisie.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy” oraz “zy”, zwrocony napis powinien brzmiec: “Le je na wie”.

*/
import java.util.*;

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

    assert (usunWystapienia(napis1, napis2).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

