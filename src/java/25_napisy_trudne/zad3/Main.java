/*
Tytul: Usun podnapis.
Tresc: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usuniecie wszystkich wystapien drugiego napisu w pierwszym napisie.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy” oraz “zy”, zwrocony napis powinien brzmiec: “Le je na wie”.

*/
import java.util.*;

public class Main {

  public static boolean czyPoczatek(String napis1, String napis2) {
    if (napis1.length() < napis2.length()) return false;

    return napis1.substring(0, napis2.length()).equals(napis2);
  }

  public static void test1() {
    String napis1 = "Dinozaur jest zly";
    String napis2 = "Dino";
    boolean oczekiwane = true;
    String wynik = czyPoczatek(napis1, napis2);

    assert (oczekiwane == wynik);
  }

  public static void test2() {
    String napis1 = "Dinozaur jest zly";
    String napis2 = "Pies";
    boolean oczekiwane = false;
    String wynik = czyPoczatek(napis1, napis2);

    assert (oczekiwane == wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

