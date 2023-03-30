/*
Tytul: Odwrocenie sasiadujacych bitow.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Zmien miejscami sasiadujace bity w zapisie binarnym tej liczby i zwroc dziesietna reprezentacje wyniku.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby: 9131, powinna zostac zwrocona liczba: 4951.

*/
import java.util.*;

public class Main {

  public static int zera(int n) {
    int licznik = 0;
    while (n > 0) {
      if (n % 2 == 0) {
        licznik++;
      }
      n /= 2;
    }
    return licznik;
  }

  public static int jedynki(int n) {
    int licznik = 0;
    while (n > 0) {
      if (n % 2 == 1) {
        licznik++;
      }
      n /= 2;
    }
    return licznik;
  }

  public static void test1() {
    int a = -2;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert (wynik == oczekiwane);
  }

  public static void test2() {
    int a = 3;
    int oczekiwane = 2;
    int wynik = jedynki(a);
    assert (wynik == oczekiwane);
  }

  public static void test3() {
    int a = 3;
    int oczekiwane = 0;
    int wynik = zera(a);
    assert (wynik == oczekiwane);
  }

  public static void test4() {
    int a = 7;
    int oczekiwane = 3;
    int wynik = jedynki(a);
    assert (wynik == oczekiwane);
  }

  public static void main(String[] args) {
    test1();
    test2();
    test3();
    test4();
  }
}

