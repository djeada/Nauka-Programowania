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
  public static String podmienNapis(String napis, String slowoA, String slowoB) {
    String wynik = napis.replaceAll(slowoA, slowoB);
    return wynik;
  }

  // Testy Poprawnosci
  public static void test1() {
    String napis = "Ala ma kota, kot ma Ale";
    String slowoA = "kot";
    String slowoB = "pies";
    String wynik = "Ala ma piesa, pies ma Ale";

    assert (podmienNapis(napis, slowoA, slowoB).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

