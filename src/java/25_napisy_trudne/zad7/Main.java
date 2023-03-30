/*
Tytul: Powtarzajace sie podnapisy.
Tresc: Dostajesz napis. Znajdz wszystkie powtarzajace sie podnapisy w tym napisie.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu "pythonpython" powinna zostac zwrocona lista zawierajaca napis "python".

*/
import java.util.*;

public class Main {
  public static String najdluzszePowtorzenie(String napis) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napis.length(); i++) {
      wynik_tmp = "";
      for (int j = i; j < napis.length(); j++) {
        wynik_tmp += napis.charAt(j);
        if (wynik_tmp.length() > wynik.length()) {
          wynik = wynik_tmp;
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    String slowo = "98432934021742343230";
    String wynik = "432";

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void test2() {
    String slowo = "abcdef";
    String wynik;

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void test3() {
    String slowo = "Arnold i Arnold";
    String wynik = "Arnold";

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

