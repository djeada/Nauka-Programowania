#include <cassert>
#include <cmath>

/*
Napisz funkcję, która dla otrzymanej liczby zwróci jej pierwiastek.
*/

const float dokladnosc = 0.0001;

float pierwiastek(int liczba) {

  float wynik = liczba;

  while (abs(liczba - wynik * wynik) > dokladnosc)
    wynik = (wynik + liczba / wynik) / 2;

  return wynik;
}

void testPierwiastek() {
  assert(abs(pierwiastek(1) - 1) < dokladnosc);
  assert(abs(pierwiastek(9) - 3) < dokladnosc);
  assert(abs(pierwiastek(16) - 4) < dokladnosc);
}

int main() {

  testPierwiastek();

  return 0;
}
