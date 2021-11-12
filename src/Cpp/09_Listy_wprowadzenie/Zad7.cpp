#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

/*
Dla otrzymanej listy liczb naturalnych znajdz
srednia arytmetyczna najwiekszej i drugiej najwiekszej
liczby w liscie.
*/

double sredniaDwochNajwiekszych(std::vector<int> &lista) {

  if (lista.empty())
    return 0.00;

  if (lista.size() == 1)
    return lista.front() - 1;

  int maks = std::numeric_limits<int>::min();
  int maks2 = std::numeric_limits<int>::min();

  for (auto &liczba : lista) {

    if (liczba > maks) {
      maks2 = maks;
      maks = liczba;
    }

    else if (liczba > maks2)
      maks2 = liczba;
  }

  return (maks + maks2) / 2.00;
}

void test_srednia_dwoch_najwiekszych() {

  assert(sredniaDwochNajwiekszych({}) == 0.00);
  assert(sredniaDwochNajwiekszych({1}) == 0.00);
  assert(sredniaDwochNajwiekszych({1, 2}) == 1.50);
  assert(sredniaDwochNajwiekszych({3, 5, -7, 4, 9, -11, 2}) == 7.00);
  assert(sredniaDwochNajwiekszych(
             {3, -2, 4, 9, -3, -40, 8, 5, -7, 4, 9, -11, 2}) == 6.50);
}

int main() {

  test_srednia_dwoch_najwiekszych();

  return 0;
}
