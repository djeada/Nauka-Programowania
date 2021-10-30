#include <cassert>
#include <cmath>

/*
Napisz funkcję, która dla otrzymanej liczby zwróci sumę cyfr tej liczby.
*/

int sumaCyfr(int liczba) {
  int suma = 0;

  while (liczba > 0) {
    suma += (liczba % 10);
    liczba /= 10;
  }

  return suma;
}

void testSumaCyfr(){
  assert(sumaCyfr(123) == 6);
  assert(sumaCyfr(0) == 0);
  assert(sumaCyfr(1) == 1);
}

int main() {
  
  testSumaCyfr();

  return 0;
}
