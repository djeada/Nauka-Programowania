/*
Tytul: Sprawdzenie, czy slowo jest palindromem.
Tresc: Napisz program, ktory sprawdzi, czy slowo jest palindromem. Palindromem jest slowo, ktore brzmi tak samo czytane od lewej do prawej i od prawej do lewej.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanego napisu: “kajak”, powinna zostac zwrocona wartosc logiczna: Prawda.

*/

public class Main {

  public static boolean czyPalindromV1(String slowo) {

    int lewo = -1;
    int prawo = slowo.length();

    while (prawo-- > lewo++) {

      if (slowo.charAt(lewo) != slowo.charAt(prawo)) return false;
    }

    return true;
  }

  public static boolean czyPalindromV2(String slowo) {
    return slowo.equals(new StringBuilder(slowo).reverse().toString());
  }

  public static void main(String[] args) {

    String slowo = "kajak";

    assert czyPalindromV1(slowo);
    assert czyPalindromV2(slowo);

    slowo = "Pan";

    assert !czyPalindromV1(slowo);
    assert !czyPalindromV2(slowo);
  }
}

