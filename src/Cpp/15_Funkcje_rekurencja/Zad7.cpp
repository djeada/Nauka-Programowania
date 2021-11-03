#include <cassert>

/*
Otrzymujesz listę liczb naturalnych oraz klucz.
Przy użyciu rekurencji znajdź indeks odpowiadający 
pierwszemu wystąpieniu klucza w liście. Jeśli 
klucz nie wystęþuje w liście, zwróć -1.
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
