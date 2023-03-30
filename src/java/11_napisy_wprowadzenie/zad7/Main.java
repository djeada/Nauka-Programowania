/*
Tytul: Odleglosc Hamminga.
Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych napisy maja rozne znaki.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych napisow: “adam” i “axam”, powinna zostac zwrocona liczba: 1.

*/
public class Main {
  // Otrzymujesz napis. Zamien wszystkie znaki napisu
  // na odpowiadajace im numery w tablicy ASCII. Podmien
  // otrzymany napis na uzyskane numery oddzielone przecinkami.

  public static String zamienV1(String napis) {

    if (napis.length() == 0) {
      return "";
    }

    String wynik = "";

    for (int numer : napis.toCharArray()) {
      wynik += String.valueOf(numer) + ", ";
    }

    return wynik.substring(0, wynik.length() - 2);
  }

  public static void test1() {
    String napis = "pacZka!";
    String wynik = "112, 97, 99, 90, 107, 97, 33";

    assert zamienV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "";
    String wynik = "";

    assert zamienV1(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

