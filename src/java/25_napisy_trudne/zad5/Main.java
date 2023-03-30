/*
Tytul: Usun powtorzenia znakow.
Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen kazdego znaku w napisie. Kazdy znak moze wystapic tylko raz.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis powinien brzmiec: “AB”.

*/
import java.util.*;

public class Main {

  public static String usunPowtorzeniaV1(String napis) {
    String wynik = "";
    char ostatniUsunietyZnak = ' ';

    for (int i = 0; i < napis.length(); i++) {
      if (napis.charAt(i) != ostatniUsunietyZnak) {
        wynik += napis.charAt(i);
        ostatniUsunietyZnak = napis.charAt(i);
      }
    }

    return wynik;
  }

  public static void test1() {
    String napis = "AAAAAAAAAABBBBBBBBA";
    String wynik = "ABA";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test2() {
    String napis = "XXXYYASFBY";
    String wynik = "XYASFBY";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test3() {
    String napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC";
    String wynik = "C";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test4() {
    String napis = "AAABB";
    String wynik = "AB";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test5() {
    String napis = "";
    String wynik = "";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
    test5();
  }
}

