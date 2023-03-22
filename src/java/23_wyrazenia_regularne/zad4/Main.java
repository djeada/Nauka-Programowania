import java.util.regex.Pattern;

/*
Otrzymujesz dwa napisy. Sprawdz czy drugi napis wystepuje w pierwszym napisie.
*/

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
