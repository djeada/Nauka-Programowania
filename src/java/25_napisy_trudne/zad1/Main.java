import java.util.*;

/*
Otrzymujesz trzy napisy. Pierwszy napis reprezentuje zdanie. Drugi reprezentuje
slowo A wystepujace w zdaniu. Trzeci reprezentuje slowo B, na ktore ma zostac
zamienione slowo A. Podmien w zdaniu wszystkie wystapienia slowa A na slowo B.
*/

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

    assert(podmienNapis(napis, slowoA, slowoB).equals(wynik));
  }

  public static void main(String[] args) {

    test1();

  }
}