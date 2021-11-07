#include <cassert>

/*
Otrzymujesz liste liczb naturalnych oraz klucz.
Przy uzyciu rekurencji znajdz indeks odpowiadajacy
pierwszemu wystapieniu klucza w liscie. Jesli
klucz nie wysteþuje w liscie, zwroc -1.
*/

int ciagV1(int n) {
  /**
   *
   */
  if (n == 1)
    return 1;

  return 1 + ciagV1(n - 1) * 2;
}

void test1() {
  int n = 5;
  int wynik = 31;

  assert(ciagV1(n) == wynik);
}

int main() {

  test1();

  return 0;
}
