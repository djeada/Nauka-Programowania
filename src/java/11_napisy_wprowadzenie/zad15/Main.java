/*
Tytul: Zamien znaki na kody ASCII.
Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis reprezentajacy zdanie.
  // Zwroc liste skladajaca sie ze slow zdania.
  // Znaki interpunkcyjne nie sa liczone jako slowa.
  public static String wyczysc(String napis) {
    napis = napis.trim();

    return napis.replaceAll("\\p{Punct}", "");
  }

  public static ArrayList<String> slowaV1(String napis) {
    ArrayList<String> wynik = new ArrayList<String>();
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.indexOf(' ', pocz)) != -1) {
      if (konc != pocz) {
        var slowo = napis.substring(pocz, konc);
        slowo = wyczysc(slowo);
        if (!slowo.isEmpty()) {
          wynik.add(slowo);
        }
      }
      pocz = konc + 1;
    }
    if (konc != pocz) {
      var slowo = napis.substring(pocz);
      slowo = wyczysc(slowo);
      if (!slowo.isEmpty()) {
        wynik.add(slowo);
      }
    }

    return new ArrayList<String>(wynik);
  }

  public static void test1() {
    String napis = "We think in generalities, but we live in details";
    ArrayList<String> wynik =
        new ArrayList<String>(
            Arrays.asList(
                "We", "think", "in", "generalities", "but", "we", "live", "in", "details"));

    assert wynik.equals(slowaV1(napis));
  }

  public static void test2() {
    String napis = "";
    ArrayList<String> wynik = new ArrayList<String>();
    assert wynik.equals(slowaV1(napis));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

