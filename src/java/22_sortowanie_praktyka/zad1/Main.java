import java.util.*;

/*
Dla otrzymanego napisu, posortuj alfabetycznie jego znaki.
*/

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