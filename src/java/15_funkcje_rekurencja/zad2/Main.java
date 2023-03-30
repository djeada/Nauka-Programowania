/*
Tytul: Potega.
Tresc: Otrzymujesz dwie liczby, a i b. Przy uzyciu rekurencji oblicz a podniesione do b.
Dane wejsciowe: Dwie liczby naturalne a i b.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla a = 2 i b = 3, powinna zostac zwrocona liczba: 8.

*/
public class Main {

  public static int sumaV1(int N) {

    if (N <= 0) {
      return 0;
    }

    return N + sumaV1(N - 1);
  }

  public static void test1() {
    int N = 10;
    int wynik = 55;

    assert sumaV1(N) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

