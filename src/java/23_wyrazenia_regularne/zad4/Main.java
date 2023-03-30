/*
Tytul: Wiersze konczace sie okreslonym napisem.
Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisow:
> Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota.
oraz
> da
powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

*/
import java.util.regex.Pattern;

public class Main {

  public static boolean czyNalezyV1(String napis, String podnapis) {
    return napis.matches("(?i).*" + Pattern.quote(podnapis) + ".*");
  }

  public static boolean czyNalezyV2(String napis, String podnapis) {
    return napis.indexOf(podnapis) != -1;
  }

  public static void test1() {
    String napis = "Mozart gra na skrzypcach";
    String podnapis = "skrzyp";
    boolean oczekiwane = true;
    boolean wynik = czyNalezyV1(napis, podnapis);
    assert wynik == oczekiwane;
  }

  public static void test2() {
    String napis = "Lezy jerzy na wiezy";
    String podnapis = "nan";
    boolean oczekiwane = true;
    boolean wynik = czyNalezyV1(napis, podnapis);
    assert wynik == oczekiwane;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

