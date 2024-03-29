/*
Tytul: Odwroc napis.
Tresc: Zmien otrzymany napis, tak aby zapisany byl on od tylu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "barszcz", powinien zostac zwrocony napis: "zczsrab".

*/
import java.util.*;

public class Main {
  // Odwroc napis.

  public static String odwrocNapisV1(String slowo) {

    char[] in = slowo.toCharArray();
    int begin = 0;
    int end = in.length - 1;
    char temp;
    while (end > begin) {
      temp = in[begin];
      in[begin] = in[end];
      in[end] = temp;
      end--;
      begin++;
    }
    return new String(in);
  }

  public static String odwrocNapisV2(String slowo) {
    return new StringBuilder(slowo).reverse().toString();
  }

  public static void test1() {
    String napis = "adam";
    String wynik = "mada";

    assert odwrocNapisV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "adam";
    String wynik = "mada";

    assert odwrocNapisV2(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

