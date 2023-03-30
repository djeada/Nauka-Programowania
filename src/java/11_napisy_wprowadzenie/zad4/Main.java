/*
Tytul: Znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
Tresc: Otrzymasz napis. Znajdz znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista znakow.
Przyklad:
Dla otrzymanego napisu: "Slon", powinna zostac zwrocona lista: ['o', 'n'].

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis. Zamien wszystkie
  // male litery na wielkie.

  public static String naWielkieV1(String slowo) {

    return slowo.toUpperCase();
  }

  public static void test1() {
    String napis = "pacZka!";
    String wynik = "PACZKA!";

    assert naWielkieV1(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
  }
}

