/*
Tytul: Potega.
Tresc: Otrzymujesz dwie liczby, a i b. Przy uzyciu rekurencji oblicz a
podniesione do b. Dane wejsciowe: Dwie liczby naturalne a i b. Dane wyjsciowe:
Liczba naturalna. Przyklad: Dla a = 2 i b = 3, powinna zostac zwrocona
liczba: 8.

*/
#include <cassert>

int sumaV1(int N) {
  /**
   * Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu
   * przez liczbe x.
   */
  if (N <= 0)
    return 0;

  return N + sumaV1(N - 1);
}

void test1() {
  int N = 10;
  int wynik = 55;

  assert(sumaV1(N) == wynik);
}

int main() {

  test1();

  return 0;
}

