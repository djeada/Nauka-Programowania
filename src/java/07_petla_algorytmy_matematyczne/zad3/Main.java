/*
Tytul: Mnozenie i dzielenie.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych a i b, przy pomocy dodawania lub odejmowania oraz petli, obliczy:
a) iloczyn tych liczb
b) iloraz liczby a przez liczbe b
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranych liczb 3 i 2, funkcja powinna zwrocic liczbe:
a) 6;
b) 2.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanych dwoch liczb,
  // przy pomocy dodawania badz odejmowania oraz petli zrealizuje:

  // a) mnozenie;
  public static int mnozenie(int a, int b) {
    int wynik = 0;
    for (int i = 0; i < b; i++) {
      wynik += a;
    }

    return wynik;
  }

  // b) dzielenie
  public static int dzielenie(int a, int b) {
    int wynik = 0;
    while (a >= b) {
      a -= b;
      wynik++;
    }

    return wynik;
  }

  public static void test1() {
    int a = 2;
    int b = 3;

    int wynik = 6;
    assert mnozenie(a, b) == wynik;
  }

  public static void test2() {
    int a = 30;
    int b = 6;

    int wynik = 5;
    assert dzielenie(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

