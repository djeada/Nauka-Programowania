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

