/*
Tytul: Podmiana slowa w zdaniu.
Tresc: Masz trzy napisy: zdanie, slowo A i slowo B. Twoim zadaniem jest zamiana wszystkich wystapien slowa A na slowo B w zdaniu.
Dane wejsciowe: Trzy napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrocony napis powinien brzmiec: “Lerzy jerzy na wierzy”.

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

