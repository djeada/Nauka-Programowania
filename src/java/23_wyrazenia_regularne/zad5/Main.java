/*
Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.
Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

*/
import java.util.*;

public class Main {

  public static String odfiltrujCyfryV1(String napis) {
    return napis.replaceAll("[^0-9]", "");
  }

  public static void test1() {
    String napis = "numer 32.19 wyzej niz 31.17";
    String wynik = "32193117";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "Lezy jerzy na wiezy";
    String wynik = "";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

