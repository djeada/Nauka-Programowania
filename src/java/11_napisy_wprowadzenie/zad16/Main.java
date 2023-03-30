/*
Tytul:Wypisz pionowo slowa, z ktorych sklada sie zdanie.
Tresc: Otrzymasz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Kilka napisow.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinno zostac wypisane: "Ala", "ma", "kota".

*/
public class Main {
  // Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej
  // dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne
  // znaki.

  public static int odlegloscHammingaV1(final String napisA, final String napisB) {
    if (napisA.length() != napisB.length()) {
      return -1;
    }

    int wynik = 0;

    for (int i = 0; i < napisA.length(); i++) {
      if (napisA.charAt(i) != napisB.charAt(i)) {
        wynik++;
      }
    }

    return wynik;
  }

  public static void test1() {
    String napisA = "xxbab";
    String napisB = "bbabb";
    int wynik = 4;
    assert odlegloscHammingaV1(napisA, napisB) == wynik;
  }

  public static void test2() {
    String napisA = "xxbab";
    String napisB = "bbabb";
    int wynik = 4;
    assert odlegloscHammingaV1(napisA, napisB) == wynik;
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

