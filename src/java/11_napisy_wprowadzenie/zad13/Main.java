/*
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.
Tresc: Otrzymasz napis oraz liczbe k.
a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.
b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.
Dane wejsciowe: Napis oraz liczba.
Dane wyjsciowe: Napis.
Przyklad:
a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis: "z h n".
b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis:
z
h
n

*/
import java.util.*;

public class Main {
  // Otrzymujesz zdanie. Znajdz znaki znajdujace
  // sie na pozycjach bedacych liczbami pierwszymi.

  public static boolean czyPierwsza(int n) {

    if ((n % 2) == 0 && n != 2) {
      return false;
    }

    for (int i = 3; i <= Math.sqrt((double) n); i += 2) {
      if ((n % i) == 0) {
        return false;
      }
    }

    return true;
  }

  public static ArrayList<Character> znaki(final String napis) {

    ArrayList<Character> znaki = new ArrayList<Character>();

    for (int i = 0; i < napis.length(); i++) {
      if (czyPierwsza(i)) {
        znaki.add(napis.charAt(i));
      }
    }

    return new ArrayList<Character>(znaki);
  }

  public static void test1() {
    String napis = "Kaczka lubi wiosne.";
    ArrayList<Character> wynik =
        new ArrayList<Character>(Arrays.asList('a', 'c', 'z', 'a', 'l', ' ', 'i', 'e'));
    assert wynik.equals(znaki(napis));
  }

  public static void main(String[] args) {
    test1();
  }
}

