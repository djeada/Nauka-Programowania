#include <cassert>
#include <cmath>

/*
Napisz funkcję, która dla otrzymanych dwóch liczb przy
pomocy pętli obliczy ile wynosi a podniesione do b.
*/

double potega(int podstawa, int wykladnik) {
  int wynik = 1;
  for (int i = 0; i < abs(wykladnik); i++)
    wynik *= podstawa;

  if (wykladnik < 0)
    return 1 / wynik;

  return wynik;
}

void testPotega() {
  assert(potega(2, 3) == 8);
  assert(potega(2, -3) == 0.125);
}

int main() {

  testPotega();

  return 0;
}
