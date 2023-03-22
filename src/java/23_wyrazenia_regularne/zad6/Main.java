import java.util.*;

/*
Otrzymujesz dwa napisy. Znajdz wiersze w pierwszym napisie
konczace sie drugim napisem. Wiersz moze byc zakonczony
dowolnym znakiem interpunkcyjnym.
*/

public class Main {
  public static ArrayList<String> znajdzWierszeV1(String napis, String podnapis) {
    ArrayList<String> wynik = new ArrayList<String>();
    String[] tablica = napis.split("\n");
    for (String wiersz : tablica) {
      if (wiersz.endsWith(podnapis)) {
        wynik.add(wiersz);
      }
    }
    return wynik;
  }

  public static ArrayList<String> znajdzWierszeV2(String napis, String podnapis) {
    // using regex
    ArrayList<String> wynik = new ArrayList<String>();
    String regex = ".*" + Pattern.quote(podnapis) + ".*";
    String[] tablica = napis.split("\n");
    for (String wiersz : tablica) {
      if (wiersz.matches(regex)) {
        wynik.add(wiersz);
      }
    }

    return wynik;
  }

  public static void test1() {
    String tekst =
        "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
            + "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
            + "tu cnota,\nMilosci pragna nie pragna tu zlota";
    String napis = "ada";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Folgujmy paniom nie sobie, ma rada;");
    oczekiwane.add("Milujmy wiernie nie jest w nich przysada.");
    assert (znajdzWierszeV1(tekst, napis).equals(oczekiwane));
  }

  public static void test2() {
    String tekst =
        "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
            + "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
            + "tu cnota,\nMilosci pragna nie pragna tu zlota";
    String napis = "ada";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Folgujmy paniom nie sobie, ma rada;");
    oczekiwane.add("Milujmy wiernie nie jest w nich przysada.");
    assert (znajdzWierszeV2(tekst, napis).equals(oczekiwane));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}
