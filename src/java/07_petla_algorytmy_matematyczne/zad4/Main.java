/*
Tytul: Silnia.
Tresc: Napisz funkcje, ktora obliczy silnie otrzymanej liczby naturalnej, przy pomocy petli.
Dane wejsciowe: liczba naturalna
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanej liczby 3, funkcja powinna zwrocic liczbe 6.

*/
public class Main {
  // Napisz funkcje, ktora przy pomocy petli obliczy silnie
  // z otrzymanej liczby.

  public static int silnia(int a) {

    int wynik = 1;

    while (a > 0) {
      wynik *= a;
      a--;
    }

    return wynik;
  }

  public static void test1() {
    int a = 4;
    int wynik = 24;
    assert silnia(a) == wynik;
  }

  public static void test2() {
    int a = -5;
    int wynik = 1;
    assert silnia(a) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

