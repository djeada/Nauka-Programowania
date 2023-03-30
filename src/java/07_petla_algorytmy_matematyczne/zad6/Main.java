/*
Tytul: NWW.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najmniejsza wspolna wielokrotnosc.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 7 i 9, funkcja powinna zwrocic liczbe 63.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
  // ich najmniejsza wspolna wielokrotnosc.

  public static int nwd(int a, int b) {

    int c;

    while (b != a % b) {
      c = b;
      b = a % b;
      a = c;

      if (b == 0) {
        break;
      }
    }

    return a;
  }

  public static int nww(int a, int b) {
    return a * b / nwd(a, b);
  }

  public static void test1() {
    int a = 14;
    int b = 21;
    int wynik = 42;

    assert nww(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

