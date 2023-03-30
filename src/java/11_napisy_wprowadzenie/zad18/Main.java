/*
Tytul: Znajdz najdluzsze/najkrotsze slowo w zdaniu.
Tresc: Otrzymasz napis reprezentujacy zdanie. Znajdz:
a) najdluzsze slowo w zdaniu,
b) najkrotsze slowo w zdaniu.
Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe:
a) Napis.
b) Napis.
Przyklad:
a) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "Kaczka".
b) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "lubi".

*/

import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Main {

  public static String odwrocNapisyV1(String napis) {

    String[] slowa = napis.split(" ");
    StringBuilder odwrocony = new StringBuilder();

    for (String word : slowa) {

      StringBuilder reverseWord = new StringBuilder();

      for (int i = word.length() - 1; i >= 0; i--) {
        reverseWord.append(word.charAt(i));
      }

      odwrocony.append(reverseWord).append(" ");
    }

    return odwrocony.toString().trim();
  }

  public static String odwrocNapisyV2(String napis) {
    return Pattern.compile(" +")
        .splitAsStream(napis)
        .map(w -> new StringBuilder(w).reverse())
        .collect(Collectors.joining(" "));
  }

  public static void main(String[] args) {

    String napis = "Cameron Diaz";
    String wynik = "noremaC zaiD";

    assert odwrocNapisyV1(napis).equals(wynik);
    assert odwrocNapisyV2(napis).equals(wynik);
  }
}

