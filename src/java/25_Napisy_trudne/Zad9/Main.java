import java.util.*;

/*
Otrzymujesz dwa napisy. Znajdz ich najdluzszy wspolny podnapis.
*/

public class Main {
  public static String najdluzszyPodnapis(String napis1, String napis2) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napis1.length(); i++) {
      wynik_tmp = "";
      for (int j = i; j < napis1.length(); j++) {
        wynik_tmp += napis1.charAt(j);
        if (napis2.contains(wynik_tmp)) {
          if (wynik_tmp.length() > wynik.length()) {
            wynik = wynik_tmp;
          }
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    String napis1 = "abcdxyz";
    String napis2 = "xyzabcd";
    String wynik = "abcd";

    assert(najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void test2() {
    String napis1 = "hhaall";
    String napis2 = "hhaall";
    String wynik = "hhaall";

    assert(najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void test3() {
    String napis1;
    String napis2;
    String wynik;

    assert(najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}