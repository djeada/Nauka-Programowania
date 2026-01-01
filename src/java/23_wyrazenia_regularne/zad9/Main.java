/*
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.

### Wejście

Dwie części:

1. Tekst (może mieć wiele wierszy)
2. W osobnej linii: `klucz`

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści zadania — długi tekst)*

*/
import java.util.*;

public class Main {

  public static String wczyscTekstV1(String tekst, String napis) {
    String wynik = "";
    String wzorzec = napis + "(.*)";
    String[] _wiersze = tekst.split("\n");
    for (String wiersz : _wiersze) {
      wynik += wiersz.replaceAll(wzorzec, "\n");
    }
    return wynik;
  }

  public static void test1() {
    String tekst =
        "Turned it up should no valley cousin he.\nSpeaking numerous ask did "
            + "horrible packages set.\nAshamed herself has distant can studied "
            + "mrs.\nLed therefore its middleton perpetual fulfilled provision "
            + "frankness.\nSmall he drawn after among every three no.\nAll having "
            + "but you edward genius though remark one.\nRooms oh fully taken by "
            + "worse do.\nPoints afraid but may end law lasted.\nWas out laughter "
            + "raptures returned outweigh.\nLuckily cheered colonel me do we "
            + "attacks on highest enabled.\nTried law yet style child.\nBore of true "
            + "of no be deal.\nFrequently sufficient in be unaffected.\nThe "
            + "furnished she concluded depending procuring concealed.";
    String napis = "a";
    String wynik =
        "Turned it up should no v\nSpe\nAsh\nLed therefore its middleton "
            + "perpetu\nSm\nAll h\nRooms oh fully t\nPoints \nW\nLuckily cheered "
            + "colonel me do we \nTried l\nBore of true of no be de\nFrequently "
            + "sufficient in be un\nThe furnished she concluded depending procuring "
            + "conce\n";

    assert (wczyscTekstV1(tekst, napis) == wynik);
  }

  public static void main(String[] args) {
    test1();
  }
}

