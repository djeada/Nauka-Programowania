/*
Tytul: Sortowanie znakow w napisie.
Tresc: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu "Ala ma kota" powinno zostac zwrocone " Aaaaklmot".

*/
import java.util.*;

public class Main {
  public static sortujSlowoV1(final String slowo) {
    char[] tablica = slowo.toCharArray();
    Arrays.sort(tablica);
    return new String(tablica);
  }

  public static void test1() {

    final String napis = "bcda";
    final String oczekwiane = "abcd";

    final String wynik = sortujSlowoV1(napis);

    assert wynik.equals(oczekwiane);
  }

  public static void main(String[] args) {

    test1();
  }
}

