/*
Tytul: Sprawdz czy slowo wystepuje w zdaniu.
Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

*/
import java.util.*;

public class Main {

  public static boolean poprawneHaslo(String haslo) {
    if (haslo.matches("[a-z]+") && haslo.matches("[A-Z]+")) {
      if (haslo.matches("[0-9]+") && haslo.matches("[!#$%&'*+-/=?^_`{|}~]+"))
        return haslo.length() >= 8 && haslo.length() <= 20;
    }

    return false;
  }

  public static void test1() {
    List<String> poprawneHasla =
        Arrays.asList(
            "HulaKula123!",
            "$$KAsiORA302$$",
            "X'nQz{sH:6k4*3+T",
            "=3Xv+D]?''(_",
            "Mt`VXsD^47+'H-",
            "]t'N\"mtH'W9p<_<Vc)=",
            "b5TMq2L:'{f&",
            "_t}s%Ymu2YP>w",
            "'zGFbJg)~6;}",
            "\"Tuqb}h7)2Gv",
            "Ng2+]zLR7)nX7UXM]`T",
            ",{QPW7H+7za?95K&:wP");

    for (String haslo : poprawneHasla) assert (poprawneHaslo(haslo));
  }

  public static void test2() {
    List<String> niepoprawneHasla =
        Arrays.asList(
            "123456",
            "proste_haslo123",
            "haslo",
            "pizza&*!",
            "!!!!!!!!",
            "_____123_____",
            "...",
            "abcd32",
            "AB***DB",
            "22tajnE",
            "Ab6*");

    for (String haslo : niepoprawneHasla) assert (!poprawneHasla(haslo));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

