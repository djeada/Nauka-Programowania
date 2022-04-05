import java.util.*;

/*
Otrzymujesz dwa napisy. Sprawdz czy napisy sa swoimi rotacjami.
*/

public class Main {
  public static boolean czyRotacja(String napis1, String napis2) {
    if (napis1.length() != napis2.length())
      return false;

    String napis1_rot = napis1 + napis1;
    return napis1_rot.contains(napis2);
  }

  public static void test1() {
    String napis1 = "malpka";
    String napis2 = "kamapl"; 
    boolean oczekiwane = false;
    boolean wynik = czyRotacja(napis1, napis2);

    assert(wynik == oczekiwane);
  }

  public static void test2() {
    String napis1 = "malpka";
    String napis2 = "pkamal";
    boolean oczekiwane = true;
    boolean wynik = czyRotacja(napis1, napis2);

    assert(wynik == oczekiwane);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }

}