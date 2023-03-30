/*
Tytul: Operacje arytmetyczne.
Tresc: Otrzymujesz dwie liczby naturalne. Uzywajac jedynie operatorow bitowych, zaimplementuj:
a) Dodawanie.
b) Odejmowanie.
c) Mnozenie.
d) Dzielenie.
Dane wejsciowe: Dwie liczby naturalne w kazdym podpunkcie.
Dane wyjsciowe: Liczba naturalna w kazdym podpunkcie.
Przyklad:
a) Dla otrzymanych liczb: 2 i 3, powinna zostac zwrocona liczba: 5.
b) Dla otrzymanych liczb: 7 i 5, powinna zostac zwrocona liczba: 2.
c) Dla otrzymanych liczb: 4 i 4, powinna zostac zwrocona liczba: 16.
d) Dla otrzymanych liczb: 9 i 3, powinna zostac zwrocona liczba: 3.

*/
import java.util.BitSet;

public class Main {
  // Czy liczba jest palindromem?

  public static final int liczbaBitow = 8;

  public static boolean czyPalindromV1(int liczba) {
    BitSet bity = BitSet.valueOf(new long[] {liczba});

    for (int i = 0; i < liczbaBitow / 2 - 1; i++) {
      int val1 = bity.get(i) ? 1 : 0;
      int val2 = bity.get(liczbaBitow - 1 - i) ? 1 : 0;

      if ((val1 ^ val2) != 0) {
        return false;
      }
    }

    return true;
  }

  public static void test1() {
    int liczba = 231;
    assert czyPalindromV1(liczba);
  }

  public static void test2() {
    int liczba = 17;
    assert !czyPalindromV1(liczba);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

