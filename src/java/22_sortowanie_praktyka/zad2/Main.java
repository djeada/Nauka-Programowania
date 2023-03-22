import java.util.*;

/*
Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa.
Posortuj slowa alfabetycznie i zapisz je w liscie. Pamietaj, znaki
interpunkcyjne nie sa liczone jako slowa.
*/

public class Main {

  public static String wyczysc(final String napis) {
    return napis.trim().replaceAll("\\p{Punct}", "");
  }

  public static ArrayList<String> slowa(final String napis) {
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

  public static ArrayList<String> sortuj(final String zdanie) {
    ArrayList<String> wynik = slowa(zdanie);
    Collections.sort(wynik);
    return wynik;
  }

  public static void test1() {
    final String napis = "Lemur wygina smialo cialo";
    final ArrayList<String> oczekiwane =
        new ArrayList<String>(Arrays.asList("Lemur", "cialo", "smialo", "wygina"));
    final ArrayList<String> wynik = sortuj(napis);

    assert oczekiwane.equals(wynik);
  }

  public static void main(String[] args) {

    test1();
  }
}
