#include <cassert>

/*
Otrzymuje dwie liczby a i b. Przy użyciu rekurencji 
oblicz ile wynosi a podniesione do b.
*/

int potegaV1(int a, int b) {
  /**
   *
   */
  if (b == 0)
    return 1;

  return a * potegaV1(a, b - 1);
}

void test1() {
  int a = 3;
  int b = 2;
  int wynik = 9;

  assert(potegaV1(a, b) == wynik);
}

int main() {

  test1();

  return 0;
}
