#include <cassert>
#include <cmath>
#include <unordered_map>

/*
Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie
z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi
od otrzymanej liczby oraz wartosci bedacych kwadratami
odpowiadajacych im kluczy.
*/

std::unordered_map<int, int> budujSlownik(int liczba) {
  /*
   * Funkcja tworzy slownik zawierajacy klucze bedace kolejnymi
   * liczbami naturalnymi mniejszymi od podanej liczby n
   * oraz wartosci bedacymi kwadratami kluczy.
   */
  std::unordered_map<int, int> slownik;

  for (int i = 1; i < liczba; i++)
    slownik[i] = pow(i, 2);

  return slownik;
}

void test1() {
  int liczba = 5;
  std::unordered_map<int, int> wynik{{1, 1}, {2, 4}, {3, 9}, {4, 16}};

  assert(budujSlownik(liczba) == wynik);
}

void test2() {
  int liczba = -1;
  std::unordered_map<int, int> wynik;

  assert(budujSlownik(liczba) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}
