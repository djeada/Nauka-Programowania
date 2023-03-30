/*
Tytul: Najdluzszy wspolny przedrostek.
Tresc: Dostajesz liste napisow. Znajdz najdluzszy wspolny przedrostek dla wszystkich napisow na liscie.
Dane wejsciowe: Lista napisow.
Dane wyjsciowe: Napis.
Przyklad:
Dla listy ["Remolada", "Remux", "Remmy"] powinien zostac zwrocony napis "Rem".

*/
import java.util.*;

public class Main {
  public static String najdluzszyPrzedrostek(List<String> napisy) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napisy.size(); i++) {
      wynik_tmp = "";
      for (int j = 0; j < napisy.get(i).length(); j++) {
        wynik_tmp += napisy.get(i).charAt(j);
        if (wynik_tmp.length() > wynik.length()) {
          wynik = wynik_tmp;
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    List<String> napisy = Arrays.asList("abcdefgh", "abcefgh", "abcd");
    String wynik = "abc";

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void test2() {
    List<String> napisy = Arrays.asList("flower", "flow", "flight", "flix");
    String wynik = "fl";

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void test3() {
    List<String> napisy = Arrays.asList("student", "studio", "stress", "lol");
    String wynik;

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

