/*
Tytul: Zamien wszystkie male litery na duze.
Tresc: Otrzymasz napis. Zmien wszystkie male litery na duze.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Rumcajs", powinien zostac zwrocony napis: "RUMCAJS".

*/

public class Main {

  public static String usunSpacjeV1(String zdanie) {
    return zdanie.replaceAll("\\s", "");
  }

  public static void main(String[] args) {

    String zdanie = "lezy jezy na wierzy";
    String wynik = "lezyjezynawierzy";

    assert usunSpacjeV1(zdanie).equals(wynik);

    zdanie = "d";
    wynik = "d";

    assert usunSpacjeV1(zdanie).equals(wynik);
  }
}

